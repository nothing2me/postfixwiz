"""
Postfix (Reverse Polish Notation) evaluation utilities
"""

def evaluate_postfix(expression):
    """
    Evaluate a postfix expression.
    
    Args:
        expression: String of postfix expression (e.g., "3 4 + 5 *")
    
    Returns:
        Result of the expression evaluation
    """
    if not expression:
        raise ValueError("Empty expression")
    
    # Split by spaces and filter empty strings
    tokens = [token.strip() for token in expression.split() if token.strip()]
    
    if not tokens:
        raise ValueError("No valid tokens in expression")
    
    stack = []
    
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            # Number
            stack.append(float(token))
        elif token in ['+', '-', '*', '/', '^']:
            # Operator
            if len(stack) < 2:
                raise ValueError(f"Not enough operands for operator {token}")
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            elif token == '^':
                result = a ** b
            
            stack.append(result)
        else:
            raise ValueError(f"Invalid token: {token}")
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack[0]

def is_valid_postfix(expression):
    """
    Check if a postfix expression is valid.
    
    Args:
        expression: String of postfix expression
    
    Returns:
        Tuple (is_valid, error_message)
    """
    try:
        evaluate_postfix(expression)
        return True, None
    except Exception as e:
        return False, str(e)

def format_postfix(expression):
    """
    Format postfix expression for display.
    
    Args:
        expression: String of postfix expression
    
    Returns:
        Formatted string with proper spacing
    """
    tokens = [token.strip() for token in expression.split() if token.strip()]
    return ' '.join(tokens)

