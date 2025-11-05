"""
Infix to Postfix conversion utilities
"""

def get_operator_precedence(op):
    """Get operator precedence (higher number = higher precedence)"""
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '(': 0,
        ')': 0
    }
    return precedence.get(op, 0)

def is_left_associative(op):
    """Check if operator is left-associative"""
    return op != '^'

def infix_to_postfix(infix_expr):
    """
    Convert infix expression to postfix notation.
    
    Args:
        infix_expr: String of infix expression (e.g., "a + b * c")
    
    Returns:
        Postfix expression as string
    """
    # Remove spaces and prepare tokens
    tokens = tokenize(infix_expr)
    
    output = []
    stack = []
    
    for token in tokens:
        if token.isalnum() or token.replace('.', '').replace('-', '').isdigit():
            # Operand
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()  # Remove '('
        elif token in ['+', '-', '*', '/', '^']:
            # Operator
            while (stack and 
                   stack[-1] != '(' and
                   (get_operator_precedence(stack[-1]) > get_operator_precedence(token) or
                    (get_operator_precedence(stack[-1]) == get_operator_precedence(token) and 
                     is_left_associative(token)))):
                output.append(stack.pop())
            stack.append(token)
    
    # Pop remaining operators
    while stack:
        if stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())
    
    return ' '.join(output)

def tokenize(expression):
    """
    Tokenize an infix expression.
    Handles spaces, multi-digit numbers, and operators.
    
    Args:
        expression: String of infix expression
    
    Returns:
        List of tokens
    """
    expression = expression.replace(' ', '')
    tokens = []
    i = 0
    
    while i < len(expression):
        if expression[i].isdigit() or expression[i] == '.':
            # Number (including decimals)
            num = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            tokens.append(num)
            continue
        elif expression[i].isalnum():
            # Variable (single letter or word)
            var = ''
            while i < len(expression) and expression[i].isalnum():
                var += expression[i]
                i += 1
            tokens.append(var)
            continue
        else:
            # Operator or parenthesis
            tokens.append(expression[i])
            i += 1
    
    return tokens

def get_conversion_steps(infix_expr):
    """
    Get step-by-step conversion process from infix to postfix.
    
    Args:
        infix_expr: String of infix expression
    
    Returns:
        List of step dictionaries with 'token', 'output', 'stack', 'action'
    """
    tokens = tokenize(infix_expr)
    steps = []
    output = []
    stack = []
    
    for i, token in enumerate(tokens):
        if token.isalnum() or token.replace('.', '').replace('-', '').isdigit():
            # Operand
            output.append(token)
            steps.append({
                'step': i + 1,
                'token': token,
                'output': ' '.join(output),
                'stack': ' '.join(stack) if stack else '(empty)',
                'action': f'Add {token} to output (operand)'
            })
        elif token == '(':
            stack.append(token)
            steps.append({
                'step': i + 1,
                'token': token,
                'output': ' '.join(output),
                'stack': ' '.join(stack),
                'action': 'Push ( to stack'
            })
        elif token == ')':
            popped = []
            while stack and stack[-1] != '(':
                popped.append(stack.pop())
                output.append(popped[-1])
            
            if stack:
                stack.pop()  # Remove '('
            
            steps.append({
                'step': i + 1,
                'token': token,
                'output': ' '.join(output),
                'stack': ' '.join(stack) if stack else '(empty)',
                'action': f'Pop {", ".join(popped)} from stack to output'
            })
        elif token in ['+', '-', '*', '/', '^']:
            popped_ops = []
            while (stack and 
                   stack[-1] != '(' and
                   (get_operator_precedence(stack[-1]) > get_operator_precedence(token) or
                    (get_operator_precedence(stack[-1]) == get_operator_precedence(token) and 
                     is_left_associative(token)))):
                op = stack.pop()
                popped_ops.append(op)
                output.append(op)
            
            if popped_ops:
                steps.append({
                    'step': i + 1,
                    'token': token,
                    'output': ' '.join(output),
                    'stack': ' '.join(stack) if stack else '(empty)',
                    'action': f'Pop {", ".join(popped_ops)} from stack (higher/equal precedence), then push {token}'
                })
            else:
                steps.append({
                    'step': i + 1,
                    'token': token,
                    'output': ' '.join(output),
                    'stack': ' '.join(stack) if stack else '(empty)',
                    'action': f'Push {token} to stack'
                })
            
            stack.append(token)
    
    # Final step: pop remaining operators
    if stack:
        final_popped = []
        while stack:
            if stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            op = stack.pop()
            final_popped.append(op)
            output.append(op)
        
        steps.append({
            'step': len(tokens) + 1,
            'token': '(end)',
            'output': ' '.join(output),
            'stack': '(empty)',
            'action': f'Pop remaining operators: {", ".join(final_popped)}'
        })
    
    return steps

