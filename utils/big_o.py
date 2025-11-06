"""
Big-O Notation practice problem generation
"""

import random
from enum import Enum

class BigOProblemType(Enum):
    CODE_ANALYSIS = "code_analysis"  # Analyze code snippet
    SIMPLIFY = "simplify"  # Simplify complexity expression
    MATCH = "match"  # Match code to complexity

# Common Big-O complexities
BIG_O_OPTIONS = [
    "O(1)", "O(log n)", "O(n)", "O(n log n)", 
    "O(n²)", "O(n³)", "O(2ⁿ)", "O(n!)"
]

def generate_code_analysis_problem(difficulty='easy'):
    """Generate a problem where user analyzes code to find Big-O"""
    
    problems = {
        'easy': [
            {
                'code': '''i = 1
while (i <= n):
    m = m + 2
    i = i + 1''',
                'answer': 'O(n)',
                'explanation': 'Single loop that runs n times: O(n)'
            },
            {
                'code': '''return arr[0]''',
                'answer': 'O(1)',
                'explanation': 'Constant time operation: O(1)'
            },
            {
                'code': '''i = 1
while (i <= n):
    i = i * 2
    m = m + 1''',
                'answer': 'O(log n)',
                'explanation': 'Loop increments by multiplication, doubles each time: O(log n)'
            },
            {
                'code': '''for i in range(n):
    for j in range(n):
        k = k + 1''',
                'answer': 'O(n²)',
                'explanation': 'Nested loops, each running n times: O(n²)'
            }
        ],
        'medium': [
            {
                'code': '''i = 1
while (i <= n):
    j = 1
    while (j <= n):
        k = k + 1
        j = j + 1
    i = i + 1''',
                'answer': 'O(n²)',
                'explanation': 'Nested loops, both running n times: O(n²)'
            },
            {
                'code': '''for i in range(n):
    for j in range(i):
        k = k + 1''',
                'answer': 'O(n²)',
                'explanation': 'Nested loops, inner loop runs i times where i goes from 0 to n-1: 0+1+2+...+(n-1) = n(n-1)/2 = O(n²)'
            },
            {
                'code': '''i = n
while (i > 1):
    i = i // 2
    m = m + 1''',
                'answer': 'O(log n)',
                'explanation': 'Loop divides i by 2 each iteration: O(log n)'
            },
            {
                'code': '''for i in range(n):
    j = i
    while (j > 0):
        j = j // 2
        k = k + 1''',
                'answer': 'O(n log n)',
                'explanation': 'Outer loop runs n times, inner loop runs log(i) times: O(n log n)'
            }
        ],
        'hard': [
            {
                'code': '''for i in range(n):
    for j in range(n):
        for k in range(n):
            m = m + 1''',
                'answer': 'O(n³)',
                'explanation': 'Three nested loops, each running n times: O(n³)'
            },
            {
                'code': '''def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)''',
                'answer': 'O(2ⁿ)',
                'explanation': 'Recursive function with two recursive calls, exponential growth: O(2ⁿ)'
            },
            {
                'code': '''for i in range(n):
    for j in range(i, n):
        k = k + 1''',
                'answer': 'O(n²)',
                'explanation': 'Nested loops, inner loop runs from i to n: when i=0 runs n times, i=1 runs n-1 times, etc. Total: n + (n-1) + ... + 1 = n(n+1)/2 = O(n²)'
            },
            {
                'code': '''i = 1
while (i <= n):
    j = 1
    while (j <= i):
        k = k + 1
        j = j * 2
    i = i + 1''',
                'answer': 'O(n log n)',
                'explanation': 'Outer loop runs n times, inner loop runs log(i) times: O(n log n)'
            }
        ]
    }
    
    problem = random.choice(problems.get(difficulty, problems['easy']))
    
    return {
        'type': 'code_analysis',
        'question': 'What is the time complexity (Big-O) of the following code?',
        'code': problem['code'],
        'correct_answer': problem['answer'],
        'explanation': problem['explanation'],
        'hint': 'Count the number of iterations. Look for loops and their nesting. Remember: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ)'
    }

def generate_simplify_problem(difficulty='easy'):
    """Generate a problem where user simplifies a complexity expression"""
    
    problems = {
        'easy': [
            {'expression': '5n + 2', 'answer': 'O(n)', 'hint': 'Drop constants and lower order terms'},
            {'expression': 'n/2 - 3', 'answer': 'O(n)', 'hint': 'Drop constants and lower order terms'},
            {'expression': '3n + 5', 'answer': 'O(n)', 'hint': 'Drop constants and lower order terms'},
            {'expression': '10', 'answer': 'O(1)', 'hint': 'Constant time is O(1)'},
        ],
        'medium': [
            {'expression': 'n² - n', 'answer': 'O(n²)', 'hint': 'Keep the dominant term: n²'},
            {'expression': 'n² + 3n + 5', 'answer': 'O(n²)', 'hint': 'Keep the dominant term: n²'},
            {'expression': 'n(n+1)/2', 'answer': 'O(n²)', 'hint': 'Simplify: n(n+1)/2 = (n²+n)/2 = O(n²)'},
            {'expression': '2n + log n', 'answer': 'O(n)', 'hint': 'n dominates log n, so O(n)'},
            {'expression': 'n log n + n', 'answer': 'O(n log n)', 'hint': 'n log n dominates n, so O(n log n)'},
        ],
        'hard': [
            {'expression': 'n³ + n² + n', 'answer': 'O(n³)', 'hint': 'Keep the dominant term: n³'},
            {'expression': 'n² + n log n', 'answer': 'O(n²)', 'hint': 'n² dominates n log n, so O(n²)'},
            {'expression': '2ⁿ + n³', 'answer': 'O(2ⁿ)', 'hint': 'Exponential dominates polynomial'},
            {'expression': 'n(n+1)(2n+1)/6', 'answer': 'O(n³)', 'hint': 'Simplify: n(n+1)(2n+1)/6 = O(n³)'},
            {'expression': 'log n + 5', 'answer': 'O(log n)', 'hint': 'Drop constants, keep log n'},
        ]
    }
    
    problem = random.choice(problems.get(difficulty, problems['easy']))
    
    return {
        'type': 'simplify',
        'question': f'Simplify the following complexity expression to Big-O notation:',
        'expression': problem['expression'],
        'correct_answer': problem['answer'],
        'hint': problem['hint'],
        'explanation': f"Using the simplification method: drop constants and lower order terms. The dominant term in '{problem['expression']}' gives us {problem['answer']}."
    }

def generate_match_problem(difficulty='easy'):
    """Generate a multiple choice problem matching code to complexity"""
    
    problems = {
        'easy': [
            {
                'code': 'return arr[0]',
                'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'],
                'answer': 'O(1)'
            },
            {
                'code': '''for i in range(n):
    m = m + 1''',
                'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'],
                'answer': 'O(n)'
            },
            {
                'code': '''i = 1
while (i <= n):
    i = i * 2''',
                'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'],
                'answer': 'O(log n)'
            }
        ],
        'medium': [
            {
                'code': '''for i in range(n):
    for j in range(n):
        k = k + 1''',
                'options': ['O(n)', 'O(n log n)', 'O(n²)', 'O(n³)'],
                'answer': 'O(n²)'
            },
            {
                'code': '''for i in range(n):
    j = i
    while (j > 0):
        j = j // 2''',
                'options': ['O(n)', 'O(n log n)', 'O(n²)', 'O(log n)'],
                'answer': 'O(n log n)'
            }
        ],
        'hard': [
            {
                'code': '''for i in range(n):
    for j in range(n):
        for k in range(n):
            m = m + 1''',
                'options': ['O(n²)', 'O(n³)', 'O(2ⁿ)', 'O(n log n)'],
                'answer': 'O(n³)'
            },
            {
                'code': '''def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)''',
                'options': ['O(n)', 'O(n²)', 'O(2ⁿ)', 'O(n log n)'],
                'answer': 'O(2ⁿ)'
            }
        ]
    }
    
    problem = random.choice(problems.get(difficulty, problems['easy']))
    
    return {
        'type': 'match',
        'question': 'What is the time complexity (Big-O) of the following code?',
        'code': problem['code'],
        'options': problem['options'],
        'correct_answer': problem['answer'],
        'hint': 'Count iterations and look at loop nesting patterns'
    }

def generate_big_o_problem(difficulty='easy', problem_type='both'):
    """
    Generate a Big-O practice problem.
    
    Args:
        difficulty: 'easy', 'medium', or 'hard'
        problem_type: 'code_analysis', 'simplify', 'match', or 'both'
    
    Returns:
        Dictionary with problem data
    """
    if problem_type == 'both':
        actual_type = random.choice(['code_analysis', 'simplify', 'match'])
    else:
        actual_type = problem_type
    
    if actual_type == 'code_analysis':
        return generate_code_analysis_problem(difficulty)
    elif actual_type == 'simplify':
        return generate_simplify_problem(difficulty)
    elif actual_type == 'match':
        return generate_match_problem(difficulty)
    else:
        return generate_code_analysis_problem(difficulty)

