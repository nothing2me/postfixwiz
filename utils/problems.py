"""
Problem generation utilities for practice mode
"""

import random
from enum import Enum

class ProblemType(Enum):
    EVALUATE = "evaluate"
    CONVERT = "convert"
    BOTH = "both"

def generate_simple_infix(use_variables=False):
    """Generate a simple infix expression (easy difficulty)"""
    operators = ['+', '-', '*']
    
    if use_variables:
        # Use letters a-z
        available_vars = list('abcdefghijklmnopqrstuvwxyz')
        num_operands = random.randint(2, 3)
        vars_needed = random.sample(available_vars, num_operands)
        ops = random.sample(operators, num_operands - 1)
        
        expr = vars_needed[0]
        for i in range(num_operands - 1):
            expr += f" {ops[i]} {vars_needed[i+1]}"
    else:
        # Use numbers
        operands = list(range(1, 10))
        num_operands = random.randint(2, 3)
        ops = random.sample(operators, num_operands - 1)
        nums = random.sample(operands, num_operands)
        
        expr = str(nums[0])
        for i in range(num_operands - 1):
            expr += f" {ops[i]} {nums[i+1]}"
    
    return expr

def generate_medium_infix(use_variables=False):
    """Generate a medium complexity infix expression"""
    operators = ['+', '-', '*', '/']
    
    if use_variables:
        available_vars = list('abcdefghijklmnopqrstuvwxyz')
        num_operands = random.randint(3, 4)
        vars_needed = random.sample(available_vars, num_operands)
        ops = random.sample(operators, num_operands - 1)
        
        expr = vars_needed[0]
        for i in range(num_operands - 1):
            expr += f" {ops[i]} {vars_needed[i+1]}"
    else:
        operands = list(range(1, 20))
        num_operands = random.randint(3, 4)
        ops = random.sample(operators, num_operands - 1)
        nums = random.sample(operands, num_operands)
        
        expr = str(nums[0])
        for i in range(num_operands - 1):
            expr += f" {ops[i]} {nums[i+1]}"
    
    return expr

def generate_hard_infix(use_variables=False):
    """Generate a hard complexity infix expression with parentheses"""
    operators = ['+', '-', '*', '/', '^']
    
    if use_variables:
        available_vars = list('abcdefghijklmnopqrstuvwxyz')
        num_operands = random.randint(4, 5)
        vars_needed = random.sample(available_vars, num_operands)
        ops = random.sample(operators, num_operands - 1)
        
        expr_parts = [vars_needed[0]]
        i = 0
        
        while i < num_operands - 1:
            if random.random() < 0.3 and i < num_operands - 2:  # 30% chance to add paren
                expr_parts.append(f"({vars_needed[i+1]} {ops[i]} {vars_needed[i+2]})")
                i += 2  # Skip next iteration
            else:
                expr_parts.append(f"{ops[i]} {vars_needed[i+1]}")
                i += 1
    else:
        operands = list(range(1, 30))
        num_operands = random.randint(4, 5)
        ops = random.sample(operators, num_operands - 1)
        nums = random.sample(operands, num_operands)
        
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

def generate_problem(difficulty='easy', problem_type='both', use_variables=False):
    """
    Generate a random problem for practice mode.
    
    Args:
        difficulty: 'easy', 'medium', or 'hard'
        problem_type: 'evaluate', 'convert', or 'both'
        use_variables: If True, use letters (a, b, c, ...) instead of numbers
    
    Returns:
        Dictionary with problem data
    """
    from utils.infix_to_postfix import infix_to_postfix
    from utils.postfix import evaluate_postfix
    
    # Determine actual problem type
    if problem_type == 'both':
        actual_type = random.choice(['evaluate', 'convert'])
    else:
        actual_type = problem_type
    
    # If evaluate type, force use_variables to False (can't evaluate variables)
    if actual_type == 'evaluate':
        use_variables = False
    
    # Generate infix expression based on difficulty
    if difficulty == 'easy':
        infix_expr = generate_simple_infix(use_variables)
    elif difficulty == 'medium':
        infix_expr = generate_medium_infix(use_variables)
    else:  # hard
        infix_expr = generate_hard_infix(use_variables)
    
    if actual_type == 'evaluate':
        # Convert to postfix and evaluate (must use numbers)
        postfix_expr = infix_to_postfix(infix_expr.replace(' ', ''))
        try:
            result = evaluate_postfix(postfix_expr)
        except:
            # If evaluation fails, generate a simpler one with numbers
            if difficulty == 'easy':
                infix_expr = generate_simple_infix(False)
            elif difficulty == 'medium':
                infix_expr = generate_medium_infix(False)
            else:
                infix_expr = generate_hard_infix(False)
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

