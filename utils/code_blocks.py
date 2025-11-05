"""
Code block templates for drag-and-drop learning
"""

import random
from enum import Enum

class CodeBlockType(Enum):
    STACK = "stack"
    QUEUE = "queue"
    RECURSION = "recursion"
    BINARY_SEARCH = "binary_search"
    LINKED_LIST = "linked_list"

def generate_stack_code_blocks():
    """Generate code blocks for stack operations"""
    blocks = [
        {'id': 1, 'text': 'stackType<int> stack;', 'type': 'declaration', 'required': True},
        {'id': 2, 'text': 'int x, y;', 'type': 'declaration', 'required': True},
        {'id': 3, 'text': 'x = 5;', 'type': 'assignment', 'required': True},
        {'id': 4, 'text': 'y = 3;', 'type': 'assignment', 'required': True},
        {'id': 5, 'text': 'stack.push(4);', 'type': 'operation', 'required': True},
        {'id': 6, 'text': 'stack.push(x);', 'type': 'operation', 'required': True},
        {'id': 7, 'text': 'stack.push(x + 1);', 'type': 'operation', 'required': True},
        {'id': 8, 'text': 'y = stack.top();', 'type': 'operation', 'required': True},
        {'id': 9, 'text': 'stack.pop();', 'type': 'operation', 'required': True},
        {'id': 10, 'text': 'stack.push(x + y);', 'type': 'operation', 'required': True},
        {'id': 11, 'text': 'x = stack.top();', 'type': 'operation', 'required': True},
        {'id': 12, 'text': 'stack.pop();', 'type': 'operation', 'required': True},
        {'id': 13, 'text': 'cout << "x = " << x << endl;', 'type': 'output', 'required': True},
        {'id': 14, 'text': 'cout << "y = " << y << endl;', 'type': 'output', 'required': True},
    ]
    
    # Shuffle non-required blocks
    required_blocks = [b for b in blocks if b['required']]
    optional_blocks = [b for b in blocks if not b['required']]
    random.shuffle(optional_blocks)
    
    return {
        'blocks': blocks,
        'correct_order': [b['id'] for b in blocks],
        'hint': 'Stack operations: push adds to top, pop removes from top, top returns the top element',
        'type': 'stack'
    }

def generate_queue_code_blocks():
    """Generate code blocks for queue operations"""
    blocks = [
        {'id': 1, 'text': 'queueType<int> queue;', 'type': 'declaration', 'required': True},
        {'id': 2, 'text': 'int x, y;', 'type': 'declaration', 'required': True},
        {'id': 3, 'text': 'x = 2;', 'type': 'assignment', 'required': True},
        {'id': 4, 'text': 'y = 3;', 'type': 'assignment', 'required': True},
        {'id': 5, 'text': 'queue.addQueue(x);', 'type': 'operation', 'required': True},
        {'id': 6, 'text': 'queue.addQueue(y);', 'type': 'operation', 'required': True},
        {'id': 7, 'text': 'x = queue.front();', 'type': 'operation', 'required': True},
        {'id': 8, 'text': 'queue.deleteQueue();', 'type': 'operation', 'required': True},
        {'id': 9, 'text': 'queue.addQueue(x + 2);', 'type': 'operation', 'required': True},
        {'id': 10, 'text': 'queue.addQueue(x);', 'type': 'operation', 'required': True},
        {'id': 11, 'text': 'queue.addQueue(y - 3);', 'type': 'operation', 'required': True},
        {'id': 12, 'text': 'y = queue.front();', 'type': 'operation', 'required': True},
        {'id': 13, 'text': 'queue.deleteQueue();', 'type': 'operation', 'required': True},
        {'id': 14, 'text': 'cout << "x = " << x << endl;', 'type': 'output', 'required': True},
        {'id': 15, 'text': 'cout << "y = " << y << endl;', 'type': 'output', 'required': True},
    ]
    
    return {
        'blocks': blocks,
        'correct_order': [b['id'] for b in blocks],
        'hint': 'Queue operations: addQueue adds to rear, deleteQueue removes from front, front returns the front element',
        'type': 'queue'
    }

def generate_recursion_code_blocks():
    """Generate code blocks for recursive function"""
    blocks = [
        {'id': 1, 'text': 'void printSeries(int n) {', 'type': 'function_declaration', 'required': True},
        {'id': 2, 'text': '    if (n <= 0)', 'type': 'base_case', 'required': True},
        {'id': 3, 'text': '        return;', 'type': 'return', 'required': True},
        {'id': 4, 'text': '    cout << n << " ";', 'type': 'output', 'required': True},
        {'id': 5, 'text': '    printSeries(n - 3);', 'type': 'recursive_call', 'required': True},
        {'id': 6, 'text': '}', 'type': 'closing', 'required': True},
    ]
    
    return {
        'blocks': blocks,
        'correct_order': [b['id'] for b in blocks],
        'hint': 'Recursive function: base case stops recursion, recursive call calls itself with smaller value',
        'type': 'recursion'
    }

def generate_binary_search_code_blocks():
    """Generate code blocks for binary search"""
    blocks = [
        {'id': 1, 'text': 'int binarySearch(int arr[], int left, int right, int target) {', 'type': 'function_declaration', 'required': True},
        {'id': 2, 'text': '    if (left > right)', 'type': 'base_case', 'required': True},
        {'id': 3, 'text': '        return -1;', 'type': 'return', 'required': True},
        {'id': 4, 'text': '    int mid = (left + right) / 2;', 'type': 'calculation', 'required': True},
        {'id': 5, 'text': '    if (arr[mid] == target)', 'type': 'condition', 'required': True},
        {'id': 6, 'text': '        return mid;', 'type': 'return', 'required': True},
        {'id': 7, 'text': '    if (arr[mid] > target)', 'type': 'condition', 'required': True},
        {'id': 8, 'text': '        return binarySearch(arr, left, mid - 1, target);', 'type': 'recursive_call', 'required': True},
        {'id': 9, 'text': '    return binarySearch(arr, mid + 1, right, target);', 'type': 'recursive_call', 'required': True},
        {'id': 10, 'text': '}', 'type': 'closing', 'required': True},
    ]
    
    return {
        'blocks': blocks,
        'correct_order': [b['id'] for b in blocks],
        'hint': 'Binary search: compare target with middle element, then search left or right half recursively',
        'type': 'binary_search'
    }

def generate_linked_list_code_blocks():
    """Generate code blocks for linked list operations"""
    blocks = [
        {'id': 1, 'text': 'struct nodeType {', 'type': 'struct_declaration', 'required': True},
        {'id': 2, 'text': '    Type info;', 'type': 'member', 'required': True},
        {'id': 3, 'text': '    nodeType *next;', 'type': 'member', 'required': True},
        {'id': 4, 'text': '};', 'type': 'closing', 'required': True},
        {'id': 5, 'text': 'nodeType *current = head;', 'type': 'declaration', 'required': True},
        {'id': 6, 'text': 'while (current != nullptr) {', 'type': 'loop', 'required': True},
        {'id': 7, 'text': '    cout << current->info << " ";', 'type': 'operation', 'required': True},
        {'id': 8, 'text': '    current = current->next;', 'type': 'operation', 'required': True},
        {'id': 9, 'text': '}', 'type': 'closing', 'required': True},
    ]
    
    return {
        'blocks': blocks,
        'correct_order': [b['id'] for b in blocks],
        'hint': 'Linked list: traverse using current pointer, move to next node until nullptr',
        'type': 'linked_list'
    }

def generate_code_blocks(topic):
    """
    Generate code blocks for a specific topic.
    
    Args:
        topic: 'stack', 'queue', 'recursion', 'binary_search', or 'linked_list'
    
    Returns:
        Dictionary with blocks, correct order, and hint
    """
    if topic == 'stack':
        return generate_stack_code_blocks()
    elif topic == 'queue':
        return generate_queue_code_blocks()
    elif topic == 'recursion':
        return generate_recursion_code_blocks()
    elif topic == 'binary_search':
        return generate_binary_search_code_blocks()
    elif topic == 'linked_list':
        return generate_linked_list_code_blocks()
    else:
        return generate_stack_code_blocks()

def generate_typing_problem(topic):
    """
    Generate a typing problem for a specific topic.
    
    Args:
        topic: 'stack', 'queue', 'recursion', 'binary_search', or 'linked_list'
    
    Returns:
        Dictionary with problem data
    """
    if topic == 'stack':
        return {
            'type': 'stack',
            'question': 'Write code to trace stack operations. Initialize x=5, y=3, push 4, push x, push x+1, set y=top(), pop, push x+y, set x=top(), pop. Output x and y.',
            'template': 'stackType<int> stack;\nint x, y;\nx = 5;\ny = 3;\n// Your code here\ncout << "x = " << x << endl;\ncout << "y = " << y << endl;',
            'correct_answer': 'stackType<int> stack;\nint x, y;\nx = 5;\ny = 3;\nstack.push(4);\nstack.push(x);\nstack.push(x + 1);\ny = stack.top();\nstack.pop();\nstack.push(x + y);\nx = stack.top();\nstack.pop();\ncout << "x = " << x << endl;\ncout << "y = " << y << endl;',
            'hint': 'Remember: push adds to top, pop removes from top, top returns top element'
        }
    elif topic == 'queue':
        return {
            'type': 'queue',
            'question': 'Write code to trace queue operations. Initialize x=2, y=3, addQueue x, addQueue y, set x=front(), deleteQueue, addQueue x+2, addQueue x, addQueue y-3, set y=front(), deleteQueue. Output x and y.',
            'template': 'queueType<int> queue;\nint x, y;\nx = 2;\ny = 3;\n// Your code here\ncout << "x = " << x << endl;\ncout << "y = " << y << endl;',
            'correct_answer': 'queueType<int> queue;\nint x, y;\nx = 2;\ny = 3;\nqueue.addQueue(x);\nqueue.addQueue(y);\nx = queue.front();\nqueue.deleteQueue();\nqueue.addQueue(x + 2);\nqueue.addQueue(x);\nqueue.addQueue(y - 3);\ny = queue.front();\nqueue.deleteQueue();\ncout << "x = " << x << endl;\ncout << "y = " << y << endl;',
            'hint': 'Remember: addQueue adds to rear, deleteQueue removes from front, front returns front element'
        }
    elif topic == 'recursion':
        return {
            'type': 'recursion',
            'question': 'Write a recursive function that prints: n, n-3, n-6, n-9... until n <= 0',
            'template': 'void printSeries(int n) {\n    // Your code here\n}',
            'correct_answer': 'void printSeries(int n) {\n    if (n <= 0)\n        return;\n    cout << n << " ";\n    printSeries(n - 3);\n}',
            'hint': 'Base case: if n <= 0, return. Otherwise print n and recursively call with n-3'
        }
    elif topic == 'binary_search':
        return {
            'type': 'binary_search',
            'question': 'Write a recursive binary search function that finds target in sorted array',
            'template': 'int binarySearch(int arr[], int left, int right, int target) {\n    // Your code here\n}',
            'correct_answer': 'int binarySearch(int arr[], int left, int right, int target) {\n    if (left > right)\n        return -1;\n    int mid = (left + right) / 2;\n    if (arr[mid] == target)\n        return mid;\n    if (arr[mid] > target)\n        return binarySearch(arr, left, mid - 1, target);\n    return binarySearch(arr, mid + 1, right, target);\n}',
            'hint': 'Base case: if left > right, return -1. Compare target with middle, search left or right half'
        }
    else:
        return generate_typing_problem('stack')

