"""
Problem generation utilities for practice mode
"""

import random
from enum import Enum

class ProblemType(Enum):
    EVALUATE = "evaluate"
    CONVERT = "convert"
    BOTH = "both"

def generate_simple_infix():
    """Generate a simple infix expression (easy difficulty)"""
    operators = ['+', '-', '*']
    operands = list(range(1, 10))
    
    num_operands = random.randint(2, 3)
    ops = random.sample(operators, num_operands - 1)
    nums = random.sample(operands, num_operands)
    
    expr = str(nums[0])
    for i in range(num_operands - 1):
        expr += f" {ops[i]} {nums[i+1]}"
    
    return expr

def generate_medium_infix():
    """Generate a medium complexity infix expression"""
    operators = ['+', '-', '*', '/']
    operands = list(range(1, 20))
    
    num_operands = random.randint(3, 4)
    ops = random.sample(operators, num_operands - 1)
    nums = random.sample(operands, num_operands)
    
    expr = str(nums[0])
    for i in range(num_operands - 1):
        expr += f" {ops[i]} {nums[i+1]}"
    
    return expr

def generate_hard_infix():
    """Generate a hard complexity infix expression with parentheses"""
    operators = ['+', '-', '*', '/', '^']
    operands = list(range(1, 30))
    
    num_operands = random.randint(4, 5)
    ops = random.sample(operators, num_operands - 1)
    nums = random.sample(operands, num_operands)
    
    # Build expression with optional parentheses
    expr_parts = [str(nums[0])]
    i = 0
    
    while i < num_operands - 1:
        if random.random() < 0.3 and i < num_operands - 2:  # 30% chance to add paren
            expr_parts.append(f"({nums[i+1]} {ops[i]} {nums[i+2]})")
            i += 2  # Skip next iteration
        else:
            expr_parts.append(f"{ops[i]} {nums[i+1]}")
            i += 1
    
    expr = ' '.join(expr_parts)
    return expr

def generate_problem(difficulty='easy', problem_type='both'):
    """
    Generate a random problem for practice mode.
    
    Args:
        difficulty: 'easy', 'medium', or 'hard'
        problem_type: 'evaluate', 'convert', or 'both'
    
    Returns:
        Dictionary with problem data
    """
    from utils.infix_to_postfix import infix_to_postfix
    from utils.postfix import evaluate_postfix
    
    # Generate infix expression based on difficulty
    if difficulty == 'easy':
        infix_expr = generate_simple_infix()
    elif difficulty == 'medium':
        infix_expr = generate_medium_infix()
    else:  # hard
        infix_expr = generate_hard_infix()
    
    # Determine actual problem type
    if problem_type == 'both':
        actual_type = random.choice(['evaluate', 'convert'])
    else:
        actual_type = problem_type
    
    if actual_type == 'evaluate':
        # Convert to postfix and evaluate
        postfix_expr = infix_to_postfix(infix_expr.replace(' ', ''))
        try:
            result = evaluate_postfix(postfix_expr)
        except:
            # If evaluation fails, generate a simpler one
            infix_expr = generate_simple_infix()
            postfix_expr = infix_to_postfix(infix_expr.replace(' ', ''))
            result = evaluate_postfix(postfix_expr)
        
        return {
            'type': 'evaluate',
            'question': f'Evaluate the following postfix expression:',
            'expression': postfix_expr,
            'correct_answer': result,
            'hint': 'Remember: process left to right, push operands, pop two when you see an operator'
        }
    
    else:  # convert
        postfix_expr = infix_to_postfix(infix_expr.replace(' ', ''))
        
        return {
            'type': 'convert',
            'question': f'Convert the following infix expression to postfix:',
            'expression': infix_expr,
            'correct_answer': postfix_expr,
            'hint': 'Use the stack algorithm: operands go to output, operators go to stack based on precedence'
        }

