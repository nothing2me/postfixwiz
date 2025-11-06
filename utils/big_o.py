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
            },
            {
                'code': '''i = 1
j = 1
while (i <= n):
    while (j <= n):
        k = k + 1
        j = j + 1
    i = i + 1''',
                'answer': 'O(n)',
                'explanation': '⚠️ Important: j is initialized ONCE before the outer loop. Inner loop runs n times only on first iteration (when i=1), then j stays > n for all subsequent iterations. Total: O(n)'
            },
            {
                'code': '''i = 1
while (i <= n):
    j = 1
    while (j <= n):
        k = k + 1
        j = j + 1
    i = i + 1''',
                'answer': 'O(n²)',
                'explanation': 'j is reset to 1 INSIDE the outer loop each time. Both loops run n times: O(n²)'
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
            {'expression': '5n + 2', 'answer': 'O(n)', 'hint': 'Drop constants and lower order terms', 
             'explanation': 'Drop constant 5 and lower order term 2. Dominant term is n: O(n)'},
            {'expression': 'n/2 - 3', 'answer': 'O(n)', 'hint': 'Drop constants and lower order terms',
             'explanation': 'Drop constant 1/2 and lower order term -3. Dominant term is n: O(n)'},
            {'expression': '3n + 5', 'answer': 'O(n)', 'hint': 'Drop constants and lower order terms',
             'explanation': 'Drop constant 3 and lower order term 5. Dominant term is n: O(n)'},
            {'expression': '10', 'answer': 'O(1)', 'hint': 'Constant time is O(1)',
             'explanation': 'Constant expression (no variable n): O(1)'},
            {'expression': 'T(n) = a + (n-1)(b+a)', 'answer': 'O(n)', 'hint': 'Simplify: a + (n-1)(b+a) = a + (n-1)c where c is constant',
             'explanation': 'T(n) = a + (n-1)(b+a) = a + (n-1)c = a + cn - c = cn + (a-c). Drop constants: O(n)'},
        ],
        'medium': [
            {'expression': 'n² - n', 'answer': 'O(n²)', 'hint': 'Keep the dominant term: n²',
             'explanation': 'n² dominates n. Keep the dominant term: O(n²)'},
            {'expression': 'n² + 3n + 5', 'answer': 'O(n²)', 'hint': 'Keep the dominant term: n²',
             'explanation': 'n² dominates 3n and 5. Drop lower order terms: O(n²)'},
            {'expression': 'n(n+1)/2', 'answer': 'O(n²)', 'hint': 'Simplify: n(n+1)/2 = (n²+n)/2 = O(n²)',
             'explanation': 'n(n+1)/2 = (n²+n)/2 = (1/2)n² + (1/2)n. Drop constants and lower order: O(n²)'},
            {'expression': '2n + log n', 'answer': 'O(n)', 'hint': 'n dominates log n, so O(n)',
             'explanation': 'n dominates log n. Keep the dominant term: O(n)'},
            {'expression': 'n log n + n', 'answer': 'O(n log n)', 'hint': 'n log n dominates n, so O(n log n)',
             'explanation': 'n log n dominates n. Keep the dominant term: O(n log n)'},
            {'expression': '1+2+3+...+n', 'answer': 'O(n²)', 'hint': 'Sum formula: n(n+1)/2 = O(n²)',
             'explanation': '1+2+3+...+n = n(n+1)/2 = (n²+n)/2 = O(n²)'},
        ],
        'hard': [
            {'expression': 'n³ + n² + n', 'answer': 'O(n³)', 'hint': 'Keep the dominant term: n³',
             'explanation': 'n³ dominates n² and n. Keep the dominant term: O(n³)'},
            {'expression': 'n² + n log n', 'answer': 'O(n²)', 'hint': 'n² dominates n log n, so O(n²)',
             'explanation': 'n² dominates n log n. Keep the dominant term: O(n²)'},
            {'expression': '2ⁿ + n³', 'answer': 'O(2ⁿ)', 'hint': 'Exponential dominates polynomial',
             'explanation': 'Exponential 2ⁿ dominates polynomial n³. Keep the dominant term: O(2ⁿ)'},
            {'expression': 'n(n+1)(2n+1)/6', 'answer': 'O(n³)', 'hint': 'Simplify: n(n+1)(2n+1)/6 = O(n³)',
             'explanation': 'n(n+1)(2n+1)/6 = (2n³+3n²+n)/6 = (1/3)n³ + (1/2)n² + (1/6)n. Drop constants and lower order: O(n³)'},
            {'expression': '1²+2²+3²+...+n²', 'answer': 'O(n³)', 'hint': 'Sum formula: n(n+1)(2n+1)/6 = O(n³)',
             'explanation': '1²+2²+3²+...+n² = n(n+1)(2n+1)/6 = O(n³)'},
            {'expression': 'log n + 5', 'answer': 'O(log n)', 'hint': 'Drop constants, keep log n',
             'explanation': 'Drop constant 5. Keep the dominant term: O(log n)'},
            {'expression': 'n² - n + log n', 'answer': 'O(n²)', 'hint': 'Keep the dominant term: n²',
             'explanation': 'n² dominates n and log n. Drop lower order terms: O(n²)'},
        ]
    }
    
    problem = random.choice(problems.get(difficulty, problems['easy']))
    
    return {
        'type': 'simplify',
        'question': f'Simplify the following complexity expression to Big-O notation:',
        'expression': problem['expression'],
        'correct_answer': problem['answer'],
        'hint': problem['hint'],
        'explanation': problem.get('explanation', f"Using the simplification method: drop constants and lower order terms. The dominant term in '{problem['expression']}' gives us {problem['answer']}.")
    }

def generate_match_problem(difficulty='easy'):
    """Generate a multiple choice problem matching code to complexity"""
    
    problems = {
        'easy': [
            {
                'code': 'return arr[0]',
                'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'],
                'answer': 'O(1)',
                'explanation': 'Constant time operation: O(1)'
            },
            {
                'code': '''for i in range(n):
    m = m + 1''',
                'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'],
                'answer': 'O(n)',
                'explanation': 'Single loop that runs n times: O(n)'
            },
            {
                'code': '''i = 1
while (i <= n):
    i = i * 2''',
                'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'],
                'answer': 'O(log n)',
                'explanation': 'Loop doubles i each iteration, so it runs log₂(n) times: O(log n)'
            },
            {
                'code': '''i = 1
while (i <= n):
    m = m + 2
    i = i + 1''',
                'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'],
                'answer': 'O(n)',
                'explanation': 'Loop increments i by 1 each time, runs n times: O(n)'
            }
        ],
        'medium': [
            {
                'code': '''for i in range(n):
    for j in range(n):
        k = k + 1''',
                'options': ['O(n)', 'O(n log n)', 'O(n²)', 'O(n³)'],
                'answer': 'O(n²)',
                'explanation': 'Nested loops, both running n times: n × n = O(n²)'
            },
            {
                'code': '''for i in range(n):
    j = i
    while (j > 0):
        j = j // 2''',
                'options': ['O(n)', 'O(n log n)', 'O(n²)', 'O(log n)'],
                'answer': 'O(n log n)',
                'explanation': 'Outer loop runs n times, inner loop runs log(i) times: O(n log n)'
            },
            {
                'code': '''i = 1
j = 1
while (i <= n):
    while (j <= n):
        k = k + 1
        j = j + 1
    i = i + 1''',
                'options': ['O(n)', 'O(n log n)', 'O(n²)', 'O(n³)'],
                'answer': 'O(n)',
                'explanation': '⚠️ Important: j is initialized ONCE before the outer loop. Inner loop runs n times only on first iteration, then j stays > n. Total: O(n)'
            },
            {
                'code': '''i = 1
while (i <= n):
    j = 1
    while (j <= n):
        k = k + 1
        j = j + 1
    i = i + 1''',
                'options': ['O(n)', 'O(n log n)', 'O(n²)', 'O(n³)'],
                'answer': 'O(n²)',
                'explanation': 'j is reset to 1 INSIDE the outer loop each time. Both loops run n times: O(n²)'
            }
        ],
        'hard': [
            {
                'code': '''for i in range(n):
    for j in range(n):
        for k in range(n):
            m = m + 1''',
                'options': ['O(n²)', 'O(n³)', 'O(2ⁿ)', 'O(n log n)'],
                'answer': 'O(n³)',
                'explanation': 'Three nested loops, each running n times: n × n × n = O(n³)'
            },
            {
                'code': '''def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)''',
                'options': ['O(n)', 'O(n²)', 'O(2ⁿ)', 'O(n log n)'],
                'answer': 'O(2ⁿ)',
                'explanation': 'Recursive function with two recursive calls, exponential growth: O(2ⁿ)'
            },
            {
                'code': '''for i in range(n):
    for j in range(i):
        k = k + 1''',
                'options': ['O(n)', 'O(n log n)', 'O(n²)', 'O(n³)'],
                'answer': 'O(n²)',
                'explanation': 'Inner loop runs i times where i goes from 0 to n-1: 0+1+2+...+(n-1) = n(n-1)/2 = O(n²)'
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
        'explanation': problem.get('explanation', ''),
        'hint': 'Count iterations and look at loop nesting patterns. Pay attention to where variables are initialized!'
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
    # Validate difficulty
    valid_difficulties = ['easy', 'medium', 'hard']
    if difficulty not in valid_difficulties:
        difficulty = 'easy'
    
    # Validate and determine problem type
    valid_types = ['code_analysis', 'simplify', 'match', 'both']
    if problem_type not in valid_types:
        problem_type = 'both'
    
    if problem_type == 'both':
        actual_type = random.choice(['code_analysis', 'simplify', 'match'])
    else:
        actual_type = problem_type
    
    try:
        if actual_type == 'code_analysis':
            result = generate_code_analysis_problem(difficulty)
        elif actual_type == 'simplify':
            result = generate_simplify_problem(difficulty)
        elif actual_type == 'match':
            result = generate_match_problem(difficulty)
        else:
            result = generate_code_analysis_problem(difficulty)
        
        # Ensure all required fields are present
        if 'type' not in result:
            result['type'] = actual_type
        if 'correct_answer' not in result or not result['correct_answer']:
            result['correct_answer'] = 'O(n)'  # Default fallback
        if 'hint' not in result:
            result['hint'] = 'Think about the number of iterations and loop nesting'
        if 'explanation' not in result:
            result['explanation'] = ''
        
        # Validate match problems have options
        if result['type'] == 'match':
            if 'options' not in result or not result['options']:
                # Generate default options
                result['options'] = ['O(1)', 'O(log n)', 'O(n)', 'O(n²)']
            # Ensure correct answer is in options
            if result['correct_answer'] not in result['options']:
                result['options'][0] = result['correct_answer']
        
        return result
    except Exception as e:
        # Fallback to a simple default problem
        return {
            'type': 'code_analysis',
            'question': 'What is the time complexity (Big-O) of the following code?',
            'code': 'return arr[0]',
            'correct_answer': 'O(1)',
            'explanation': 'Constant time operation: O(1)',
            'hint': 'This is a simple constant time operation'
        }

