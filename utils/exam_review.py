"""
Exam review problem generators with code blocks for drag-and-drop and typing modes
Includes multiple problem variations for each topic
"""

import random
from enum import Enum

class ExamTopic(Enum):
    STACKS = "stacks"
    QUEUES = "queues"
    RECURSION = "recursion"
    LINKED_LIST = "linked_list"

class Mode(Enum):
    DRAG_DROP = "drag_drop"
    TYPING = "typing"

# Multiple stack problem variations
STACK_PROBLEMS = [
    {
        'name': 'Stack Problem 1: Basic Operations',
        'blocks': [
            {"id": "1", "code": "stackType<int> stack;", "type": "declaration", "order": 1},
            {"id": "2", "code": "int x, y;", "type": "declaration", "order": 2},
            {"id": "3", "code": "x = 5;", "type": "assignment", "order": 3},
            {"id": "4", "code": "y = 3;", "type": "assignment", "order": 4},
            {"id": "5", "code": "stack.push(4);", "type": "operation", "order": 5},
            {"id": "6", "code": "stack.push(x);", "type": "operation", "order": 6},
            {"id": "7", "code": "stack.push(x + 1);", "type": "operation", "order": 7},
            {"id": "8", "code": "y = stack.top();", "type": "operation", "order": 8},
            {"id": "9", "code": "stack.pop();", "type": "operation", "order": 9},
            {"id": "10", "code": "stack.push(x + y);", "type": "operation", "order": 10},
            {"id": "11", "code": "x = stack.top();", "type": "operation", "order": 11},
            {"id": "12", "code": "stack.pop();", "type": "operation", "order": 12},
            {"id": "13", "code": 'cout << "x = " << x << endl;', "type": "output", "order": 13},
            {"id": "14", "code": 'cout << "y = " << y << endl;', "type": "output", "order": 14},
        ],
        'hint': 'Remember: Declare stack and variables first, then perform operations, finally output results.'
    },
    {
        'name': 'Stack Problem 2: Reversing Values',
        'blocks': [
            {"id": "1", "code": "stackType<int> stack;", "type": "declaration", "order": 1},
            {"id": "2", "code": "int a, b, c;", "type": "declaration", "order": 2},
            {"id": "3", "code": "a = 10;", "type": "assignment", "order": 3},
            {"id": "4", "code": "b = 20;", "type": "assignment", "order": 4},
            {"id": "5", "code": "c = 30;", "type": "assignment", "order": 5},
            {"id": "6", "code": "stack.push(a);", "type": "operation", "order": 6},
            {"id": "7", "code": "stack.push(b);", "type": "operation", "order": 7},
            {"id": "8", "code": "stack.push(c);", "type": "operation", "order": 8},
            {"id": "9", "code": "a = stack.top();", "type": "operation", "order": 9},
            {"id": "10", "code": "stack.pop();", "type": "operation", "order": 10},
            {"id": "11", "code": "b = stack.top();", "type": "operation", "order": 11},
            {"id": "12", "code": "stack.pop();", "type": "operation", "order": 12},
            {"id": "13", "code": "c = stack.top();", "type": "operation", "order": 13},
            {"id": "14", "code": "stack.pop();", "type": "operation", "order": 14},
            {"id": "15", "code": 'cout << a << " " << b << " " << c << endl;', "type": "output", "order": 15},
        ],
        'hint': 'Stack reverses order: Last in, first out. Use this to reverse the values.'
    },
    {
        'name': 'Stack Problem 3: Arithmetic Expression',
        'blocks': [
            {"id": "1", "code": "stackType<int> stack;", "type": "declaration", "order": 1},
            {"id": "2", "code": "int result, temp;", "type": "declaration", "order": 2},
            {"id": "3", "code": "stack.push(7);", "type": "operation", "order": 3},
            {"id": "4", "code": "stack.push(3);", "type": "operation", "order": 4},
            {"id": "5", "code": "temp = stack.top();", "type": "operation", "order": 5},
            {"id": "6", "code": "stack.pop();", "type": "operation", "order": 6},
            {"id": "7", "code": "result = stack.top();", "type": "operation", "order": 7},
            {"id": "8", "code": "result = result * temp;", "type": "operation", "order": 8},
            {"id": "9", "code": "stack.pop();", "type": "operation", "order": 9},
            {"id": "10", "code": "stack.push(2);", "type": "operation", "order": 10},
            {"id": "11", "code": "temp = stack.top();", "type": "operation", "order": 11},
            {"id": "12", "code": "stack.pop();", "type": "operation", "order": 12},
            {"id": "13", "code": "result = result + temp;", "type": "operation", "order": 13},
            {"id": "14", "code": 'cout << "Result: " << result << endl;', "type": "output", "order": 14},
        ],
        'hint': 'Evaluate expression: 7 * 3 + 2. Stack helps with order of operations.'
    },
    {
        'name': 'Stack Problem 4: Multiple Pops',
        'blocks': [
            {"id": "1", "code": "stackType<int> stack;", "type": "declaration", "order": 1},
            {"id": "2", "code": "int val1, val2, val3;", "type": "declaration", "order": 2},
            {"id": "3", "code": "stack.push(15);", "type": "operation", "order": 3},
            {"id": "4", "code": "stack.push(25);", "type": "operation", "order": 4},
            {"id": "5", "code": "stack.push(35);", "type": "operation", "order": 5},
            {"id": "6", "code": "val1 = stack.top();", "type": "operation", "order": 6},
            {"id": "7", "code": "stack.pop();", "type": "operation", "order": 7},
            {"id": "8", "code": "val2 = stack.top();", "type": "operation", "order": 8},
            {"id": "9", "code": "stack.pop();", "type": "operation", "order": 9},
            {"id": "10", "code": "val3 = stack.top();", "type": "operation", "order": 10},
            {"id": "11", "code": "stack.pop();", "type": "operation", "order": 11},
            {"id": "12", "code": 'cout << val1 << " " << val2 << " " << val3 << endl;', "type": "output", "order": 12},
        ],
        'hint': 'Remember: top() reads without removing, pop() removes. Stack is LIFO (Last In First Out).'
    },
    {
        'name': 'Stack Problem 5: Complex Expression',
        'blocks': [
            {"id": "1", "code": "stackType<int> stack;", "type": "declaration", "order": 1},
            {"id": "2", "code": "int x = 4, y = 6;", "type": "declaration", "order": 2},
            {"id": "3", "code": "stack.push(x);", "type": "operation", "order": 3},
            {"id": "4", "code": "stack.push(y);", "type": "operation", "order": 4},
            {"id": "5", "code": "stack.push(x + y);", "type": "operation", "order": 5},
            {"id": "6", "code": "int sum = stack.top();", "type": "operation", "order": 6},
            {"id": "7", "code": "stack.pop();", "type": "operation", "order": 7},
            {"id": "8", "code": "stack.push(sum * 2);", "type": "operation", "order": 8},
            {"id": "9", "code": "y = stack.top();", "type": "operation", "order": 9},
            {"id": "10", "code": "stack.pop();", "type": "operation", "order": 10},
            {"id": "11", "code": 'cout << "x = " << x << ", y = " << y << endl;', "type": "output", "order": 11},
        ],
        'hint': 'Track the stack state: push adds to top, top reads top, pop removes top.'
    }
]

def generate_stack_blocks():
    """Generate code blocks for stack operations - randomly selects from multiple problems"""
    problem = random.choice(STACK_PROBLEMS)
    blocks = problem['blocks'].copy()
    
    # Shuffle blocks for drag-and-drop
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'stack_blocks',
        'problem_name': problem['name'],
        'correct_blocks': blocks,
        'shuffled_blocks': shuffled,
        'correct_code': '\n'.join([b['code'] for b in blocks]),
        'hint': problem['hint']
    }

# Multiple queue problem variations
QUEUE_PROBLEMS = [
    {
        'name': 'Queue Problem 1: Basic Operations',
        'blocks': [
            {"id": "1", "code": "queueType<int> queue;", "type": "declaration", "order": 1},
            {"id": "2", "code": "int x, y;", "type": "declaration", "order": 2},
            {"id": "3", "code": "x = 2;", "type": "assignment", "order": 3},
            {"id": "4", "code": "y = 3;", "type": "assignment", "order": 4},
            {"id": "5", "code": "queue.addQueue(x);", "type": "operation", "order": 5},
            {"id": "6", "code": "queue.addQueue(y);", "type": "operation", "order": 6},
            {"id": "7", "code": "x = queue.front();", "type": "operation", "order": 7},
            {"id": "8", "code": "queue.deleteQueue();", "type": "operation", "order": 8},
            {"id": "9", "code": "queue.addQueue(x + 2);", "type": "operation", "order": 9},
            {"id": "10", "code": "queue.addQueue(x);", "type": "operation", "order": 10},
            {"id": "11", "code": "queue.addQueue(y - 3);", "type": "operation", "order": 11},
            {"id": "12", "code": "y = queue.front();", "type": "operation", "order": 12},
            {"id": "13", "code": "queue.deleteQueue();", "type": "operation", "order": 13},
            {"id": "14", "code": 'cout << "x = " << x << endl;', "type": "output", "order": 14},
            {"id": "15", "code": 'cout << "y = " << y << endl;', "type": "output", "order": 15},
        ],
        'hint': 'Remember: Declare queue and variables first, then addQueue adds to rear, deleteQueue removes from front.'
    },
    {
        'name': 'Queue Problem 2: Processing Queue',
        'blocks': [
            {"id": "1", "code": "queueType<int> queue;", "type": "declaration", "order": 1},
            {"id": "2", "code": "int sum = 0;", "type": "declaration", "order": 2},
            {"id": "3", "code": "queue.addQueue(5);", "type": "operation", "order": 3},
            {"id": "4", "code": "queue.addQueue(10);", "type": "operation", "order": 4},
            {"id": "5", "code": "queue.addQueue(15);", "type": "operation", "order": 5},
            {"id": "6", "code": "sum = sum + queue.front();", "type": "operation", "order": 6},
            {"id": "7", "code": "queue.deleteQueue();", "type": "operation", "order": 7},
            {"id": "8", "code": "sum = sum + queue.front();", "type": "operation", "order": 8},
            {"id": "9", "code": "queue.deleteQueue();", "type": "operation", "order": 9},
            {"id": "10", "code": "sum = sum + queue.front();", "type": "operation", "order": 10},
            {"id": "11", "code": "queue.deleteQueue();", "type": "operation", "order": 11},
            {"id": "12", "code": 'cout << "Sum: " << sum << endl;', "type": "output", "order": 12},
        ],
        'hint': 'Queue maintains order: First in, first out (FIFO). Process elements in order they were added.'
    },
    {
        'name': 'Queue Problem 3: Multiple Operations',
        'blocks': [
            {"id": "1", "code": "queueType<int> queue;", "type": "declaration", "order": 1},
            {"id": "2", "code": "int a = 1, b = 2, c = 3;", "type": "declaration", "order": 2},
            {"id": "3", "code": "queue.addQueue(a);", "type": "operation", "order": 3},
            {"id": "4", "code": "queue.addQueue(b);", "type": "operation", "order": 4},
            {"id": "5", "code": "queue.addQueue(c);", "type": "operation", "order": 5},
            {"id": "6", "code": "a = queue.front();", "type": "operation", "order": 6},
            {"id": "7", "code": "queue.deleteQueue();", "type": "operation", "order": 7},
            {"id": "8", "code": "queue.addQueue(a + b);", "type": "operation", "order": 8},
            {"id": "9", "code": "b = queue.front();", "type": "operation", "order": 9},
            {"id": "10", "code": "queue.deleteQueue();", "type": "operation", "order": 10},
            {"id": "11", "code": 'cout << "a = " << a << ", b = " << b << endl;', "type": "output", "order": 11},
        ],
        'hint': 'Queue operations: addQueue adds to rear, front() reads front, deleteQueue removes from front.'
    },
    {
        'name': 'Queue Problem 4: Value Transformation',
        'blocks': [
            {"id": "1", "code": "queueType<int> queue;", "type": "declaration", "order": 1},
            {"id": "2", "code": "int val;", "type": "declaration", "order": 2},
            {"id": "3", "code": "queue.addQueue(8);", "type": "operation", "order": 3},
            {"id": "4", "code": "queue.addQueue(12);", "type": "operation", "order": 4},
            {"id": "5", "code": "val = queue.front();", "type": "operation", "order": 5},
            {"id": "6", "code": "queue.deleteQueue();", "type": "operation", "order": 6},
            {"id": "7", "code": "queue.addQueue(val * 2);", "type": "operation", "order": 7},
            {"id": "8", "code": "val = queue.front();", "type": "operation", "order": 8},
            {"id": "9", "code": "queue.deleteQueue();", "type": "operation", "order": 9},
            {"id": "10", "code": "queue.addQueue(val - 4);", "type": "operation", "order": 10},
            {"id": "11", "code": "val = queue.front();", "type": "operation", "order": 11},
            {"id": "12", "code": "queue.deleteQueue();", "type": "operation", "order": 12},
            {"id": "13", "code": 'cout << "Final value: " << val << endl;', "type": "output", "order": 13},
        ],
        'hint': 'Process queue elements one by one, transform them, and add back to queue.'
    }
]

def generate_queue_blocks():
    """Generate code blocks for queue operations - randomly selects from multiple problems"""
    problem = random.choice(QUEUE_PROBLEMS)
    blocks = problem['blocks'].copy()
    
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'queue_blocks',
        'problem_name': problem['name'],
        'correct_blocks': blocks,
        'shuffled_blocks': shuffled,
        'correct_code': '\n'.join([b['code'] for b in blocks]),
        'hint': problem['hint']
    }

# Multiple recursion problem variations
RECURSION_PROBLEMS = [
    {
        'name': 'Recursion Problem 1: Print Series (n-3)',
        'blocks': [
            {"id": "1", "code": "void printSeries(int n) {", "type": "function_declaration", "order": 1},
            {"id": "2", "code": "    if (n <= 0) {", "type": "condition", "order": 2},
            {"id": "3", "code": "        return;", "type": "base_case", "order": 3},
            {"id": "4", "code": "    }", "type": "closing", "order": 4},
            {"id": "5", "code": "    cout << n << \" \";", "type": "output", "order": 5},
            {"id": "6", "code": "    printSeries(n - 3);", "type": "recursive_call", "order": 6},
            {"id": "7", "code": "}", "type": "closing", "order": 7},
        ],
        'hint': 'Remember: Base case first (n <= 0), then output current value, then recursive call with n-3.'
    },
    {
        'name': 'Recursion Problem 2: Print Series (n-2)',
        'blocks': [
            {"id": "1", "code": "void printSeries(int n) {", "type": "function_declaration", "order": 1},
            {"id": "2", "code": "    if (n <= 0) {", "type": "condition", "order": 2},
            {"id": "3", "code": "        return;", "type": "base_case", "order": 3},
            {"id": "4", "code": "    }", "type": "closing", "order": 4},
            {"id": "5", "code": "    cout << n << \" \";", "type": "output", "order": 5},
            {"id": "6", "code": "    printSeries(n - 2);", "type": "recursive_call", "order": 6},
            {"id": "7", "code": "}", "type": "closing", "order": 7},
        ],
        'hint': 'Base case: n <= 0. Output n, then recursively call with n-2.'
    },
    {
        'name': 'Recursion Problem 3: Print Series (n/2)',
        'blocks': [
            {"id": "1", "code": "void printSeries(int n) {", "type": "function_declaration", "order": 1},
            {"id": "2", "code": "    if (n <= 0) {", "type": "condition", "order": 2},
            {"id": "3", "code": "        return;", "type": "base_case", "order": 3},
            {"id": "4", "code": "    }", "type": "closing", "order": 4},
            {"id": "5", "code": "    cout << n << \" \";", "type": "output", "order": 5},
            {"id": "6", "code": "    printSeries(n / 2);", "type": "recursive_call", "order": 6},
            {"id": "7", "code": "}", "type": "closing", "order": 7},
        ],
        'hint': 'Base case: n <= 0. Output n, then recursively call with n/2 (integer division).'
    },
    {
        'name': 'Recursion Problem 4: Count Down',
        'blocks': [
            {"id": "1", "code": "void countDown(int n) {", "type": "function_declaration", "order": 1},
            {"id": "2", "code": "    if (n < 1) {", "type": "condition", "order": 2},
            {"id": "3", "code": "        return;", "type": "base_case", "order": 3},
            {"id": "4", "code": "    }", "type": "closing", "order": 4},
            {"id": "5", "code": "    cout << n << \" \";", "type": "output", "order": 5},
            {"id": "6", "code": "    countDown(n - 1);", "type": "recursive_call", "order": 6},
            {"id": "7", "code": "}", "type": "closing", "order": 7},
        ],
        'hint': 'Base case: n < 1. Output n, then recursively call with n-1.'
    },
    {
        'name': 'Recursion Problem 5: Sum Series',
        'blocks': [
            {"id": "1", "code": "int sumSeries(int n) {", "type": "function_declaration", "order": 1},
            {"id": "2", "code": "    if (n <= 0) {", "type": "condition", "order": 2},
            {"id": "3", "code": "        return 0;", "type": "base_case", "order": 3},
            {"id": "4", "code": "    }", "type": "closing", "order": 4},
            {"id": "5", "code": "    return n + sumSeries(n - 1);", "type": "recursive_call", "order": 5},
            {"id": "6", "code": "}", "type": "closing", "order": 6},
        ],
        'hint': 'Base case: return 0 if n <= 0. Otherwise return n + sumSeries(n-1).'
    }
]

def generate_recursion_blocks():
    """Generate code blocks for recursive function - randomly selects from multiple problems"""
    problem = random.choice(RECURSION_PROBLEMS)
    blocks = problem['blocks'].copy()
    
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'recursion_blocks',
        'problem_name': problem['name'],
        'correct_blocks': blocks,
        'shuffled_blocks': shuffled,
        'correct_code': '\n'.join([b['code'] for b in blocks]),
        'hint': problem['hint']
    }

# Multiple linked list problem variations
LINKED_LIST_PROBLEMS = [
    {
        'name': 'Linked List Problem 1: Display Largest',
        'blocks': [
            {"id": "1", "code": "void displayLargest() {", "type": "function_declaration", "order": 1},
            {"id": "2", "code": "    if (stackTop == nullptr) {", "type": "condition", "order": 2},
            {"id": "3", "code": "        return;", "type": "base_case", "order": 3},
            {"id": "4", "code": "    }", "type": "closing", "order": 4},
            {"id": "5", "code": "    nodeType *current = stackTop;", "type": "declaration", "order": 5},
            {"id": "6", "code": "    float max = current->info;", "type": "initialization", "order": 6},
            {"id": "7", "code": "    while (current != nullptr) {", "type": "loop", "order": 7},
            {"id": "8", "code": "        if (current->info > max) {", "type": "condition", "order": 8},
            {"id": "9", "code": "            max = current->info;", "type": "assignment", "order": 9},
            {"id": "10", "code": "        }", "type": "closing", "order": 10},
            {"id": "11", "code": "        current = current->next;", "type": "traversal", "order": 11},
            {"id": "12", "code": "    }", "type": "closing", "order": 12},
            {"id": "13", "code": "    cout << \"Largest: \" << max << endl;", "type": "output", "order": 13},
            {"id": "14", "code": "}", "type": "closing", "order": 14},
        ],
        'hint': 'Remember: Check for empty list, initialize max with first element, traverse and compare, update max if larger.'
    },
    {
        'name': 'Linked List Problem 2: Display Smallest',
        'blocks': [
            {"id": "1", "code": "void displaySmallest() {", "type": "function_declaration", "order": 1},
            {"id": "2", "code": "    if (stackTop == nullptr) {", "type": "condition", "order": 2},
            {"id": "3", "code": "        return;", "type": "base_case", "order": 3},
            {"id": "4", "code": "    }", "type": "closing", "order": 4},
            {"id": "5", "code": "    nodeType *current = stackTop;", "type": "declaration", "order": 5},
            {"id": "6", "code": "    float min = current->info;", "type": "initialization", "order": 6},
            {"id": "7", "code": "    while (current != nullptr) {", "type": "loop", "order": 7},
            {"id": "8", "code": "        if (current->info < min) {", "type": "condition", "order": 8},
            {"id": "9", "code": "            min = current->info;", "type": "assignment", "order": 9},
            {"id": "10", "code": "        }", "type": "closing", "order": 10},
            {"id": "11", "code": "        current = current->next;", "type": "traversal", "order": 11},
            {"id": "12", "code": "    }", "type": "closing", "order": 12},
            {"id": "13", "code": "    cout << \"Smallest: \" << min << endl;", "type": "output", "order": 13},
            {"id": "14", "code": "}", "type": "closing", "order": 14},
        ],
        'hint': 'Check for empty list, initialize min with first element, traverse and compare, update min if smaller.'
    },
    {
        'name': 'Linked List Problem 3: Count Nodes',
        'blocks': [
            {"id": "1", "code": "int countNodes() {", "type": "function_declaration", "order": 1},
            {"id": "2", "code": "    int count = 0;", "type": "declaration", "order": 2},
            {"id": "3", "code": "    nodeType *current = stackTop;", "type": "declaration", "order": 3},
            {"id": "4", "code": "    while (current != nullptr) {", "type": "loop", "order": 4},
            {"id": "5", "code": "        count++;", "type": "operation", "order": 5},
            {"id": "6", "code": "        current = current->next;", "type": "traversal", "order": 6},
            {"id": "7", "code": "    }", "type": "closing", "order": 7},
            {"id": "8", "code": "    return count;", "type": "return", "order": 8},
            {"id": "9", "code": "}", "type": "closing", "order": 9},
        ],
        'hint': 'Initialize count to 0, traverse list, increment count for each node, return count.'
    },
    {
        'name': 'Linked List Problem 4: Display All',
        'blocks': [
            {"id": "1", "code": "void displayAll() {", "type": "function_declaration", "order": 1},
            {"id": "2", "code": "    nodeType *current = stackTop;", "type": "declaration", "order": 2},
            {"id": "3", "code": "    while (current != nullptr) {", "type": "loop", "order": 3},
            {"id": "4", "code": "        cout << current->info << \" \";", "type": "output", "order": 4},
            {"id": "5", "code": "        current = current->next;", "type": "traversal", "order": 5},
            {"id": "6", "code": "    }", "type": "closing", "order": 6},
            {"id": "7", "code": "    cout << endl;", "type": "output", "order": 7},
            {"id": "8", "code": "}", "type": "closing", "order": 8},
        ],
        'hint': 'Start from stackTop, traverse list, print each node\'s info, move to next until nullptr.'
    },
    {
        'name': 'Linked List Problem 5: Sum All Values',
        'blocks': [
            {"id": "1", "code": "float sumAll() {", "type": "function_declaration", "order": 1},
            {"id": "2", "code": "    float sum = 0;", "type": "declaration", "order": 2},
            {"id": "3", "code": "    nodeType *current = stackTop;", "type": "declaration", "order": 3},
            {"id": "4", "code": "    while (current != nullptr) {", "type": "loop", "order": 4},
            {"id": "5", "code": "        sum = sum + current->info;", "type": "operation", "order": 5},
            {"id": "6", "code": "        current = current->next;", "type": "traversal", "order": 6},
            {"id": "7", "code": "    }", "type": "closing", "order": 7},
            {"id": "8", "code": "    return sum;", "type": "return", "order": 8},
            {"id": "9", "code": "}", "type": "closing", "order": 9},
        ],
        'hint': 'Initialize sum to 0, traverse list, add each node\'s info to sum, return sum.'
    }
]

def generate_linked_list_blocks():
    """Generate code blocks for linked list operations - randomly selects from multiple problems"""
    problem = random.choice(LINKED_LIST_PROBLEMS)
    blocks = problem['blocks'].copy()
    
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'linked_list_blocks',
        'problem_name': problem['name'],
        'correct_blocks': blocks,
        'shuffled_blocks': shuffled,
        'correct_code': '\n'.join([b['code'] for b in blocks]),
        'hint': problem['hint']
    }

# Multiple typing exercise variations for each topic
TYPING_EXERCISES = {
    'stacks': [
        {
            'name': 'Stack Typing Exercise 1: Basic Operations',
            'template': """stackType<int> stack;
int x, y;
x = 5;
y = 3;
stack.push(4);
stack.push(x);
stack.push(x + 1);
y = stack.top();
stack.pop();
stack.push(x + y);
x = stack.top();
stack.pop();
cout << "x = " << x << endl;
cout << "y = " << y << endl;""",
            'partial': """stackType<int> stack;
int x, y;
x = 5;
y = 3;
// TODO: Add your code here
// Hint: Use stack.push(), stack.top(), stack.pop()
cout << "x = " << x << endl;
cout << "y = " << y << endl;""",
            'expected': """stack.push(4);
stack.push(x);
stack.push(x + 1);
y = stack.top();
stack.pop();
stack.push(x + y);
x = stack.top();
stack.pop();"""
        },
        {
            'name': 'Stack Typing Exercise 2: Reverse Values',
            'template': """stackType<int> stack;
int a = 10, b = 20, c = 30;
stack.push(a);
stack.push(b);
stack.push(c);
a = stack.top();
stack.pop();
b = stack.top();
stack.pop();
c = stack.top();
stack.pop();
cout << a << " " << b << " " << c << endl;""",
            'partial': """stackType<int> stack;
int a = 10, b = 20, c = 30;
// TODO: Add your code to reverse the values
// Hint: Push values, then pop and assign in reverse order
cout << a << " " << b << " " << c << endl;""",
            'expected': """stack.push(a);
stack.push(b);
stack.push(c);
a = stack.top();
stack.pop();
b = stack.top();
stack.pop();
c = stack.top();
stack.pop();"""
        },
        {
            'name': 'Stack Typing Exercise 3: Expression Evaluation',
            'template': """stackType<int> stack;
int result, temp;
stack.push(7);
stack.push(3);
temp = stack.top();
stack.pop();
result = stack.top();
result = result * temp;
stack.pop();
stack.push(2);
temp = stack.top();
stack.pop();
result = result + temp;
cout << "Result: " << result << endl;""",
            'partial': """stackType<int> stack;
int result, temp;
// TODO: Evaluate 7 * 3 + 2 using stack
// Hint: Use stack to store operands, perform operations
cout << "Result: " << result << endl;""",
            'expected': """stack.push(7);
stack.push(3);
temp = stack.top();
stack.pop();
result = stack.top();
result = result * temp;
stack.pop();
stack.push(2);
temp = stack.top();
stack.pop();
result = result + temp;"""
        }
    ],
    'queues': [
        {
            'name': 'Queue Typing Exercise 1: Basic Operations',
            'template': """queueType<int> queue;
int x, y;
x = 2;
y = 3;
queue.addQueue(x);
queue.addQueue(y);
x = queue.front();
queue.deleteQueue();
queue.addQueue(x + 2);
queue.addQueue(x);
queue.addQueue(y - 3);
y = queue.front();
queue.deleteQueue();
cout << "x = " << x << endl;
cout << "y = " << y << endl;""",
            'partial': """queueType<int> queue;
int x, y;
x = 2;
y = 3;
// TODO: Add your code here
// Hint: Use queue.addQueue(), queue.front(), queue.deleteQueue()
cout << "x = " << x << endl;
cout << "y = " << y << endl;""",
            'expected': """queue.addQueue(x);
queue.addQueue(y);
x = queue.front();
queue.deleteQueue();
queue.addQueue(x + 2);
queue.addQueue(x);
queue.addQueue(y - 3);
y = queue.front();
queue.deleteQueue();"""
        },
        {
            'name': 'Queue Typing Exercise 2: Sum Queue Values',
            'template': """queueType<int> queue;
int sum = 0;
queue.addQueue(5);
queue.addQueue(10);
queue.addQueue(15);
sum = sum + queue.front();
queue.deleteQueue();
sum = sum + queue.front();
queue.deleteQueue();
sum = sum + queue.front();
queue.deleteQueue();
cout << "Sum: " << sum << endl;""",
            'partial': """queueType<int> queue;
int sum = 0;
queue.addQueue(5);
queue.addQueue(10);
queue.addQueue(15);
// TODO: Calculate sum of all queue values
// Hint: Use front() to read, deleteQueue() to remove
cout << "Sum: " << sum << endl;""",
            'expected': """sum = sum + queue.front();
queue.deleteQueue();
sum = sum + queue.front();
queue.deleteQueue();
sum = sum + queue.front();
queue.deleteQueue();"""
        }
    ],
    'recursion': [
        {
            'name': 'Recursion Typing Exercise 1: Print Series (n-3)',
            'template': """void printSeries(int n) {
    if (n <= 0) {
        return;
    }
    cout << n << " ";
    printSeries(n - 3);
}""",
            'partial': """void printSeries(int n) {
    // TODO: Complete the recursive function
    // Hint: Base case when n <= 0, then output n, then recursive call
}""",
            'expected': """if (n <= 0) {
        return;
    }
    cout << n << " ";
    printSeries(n - 3);"""
        },
        {
            'name': 'Recursion Typing Exercise 2: Count Down',
            'template': """void countDown(int n) {
    if (n < 1) {
        return;
    }
    cout << n << " ";
    countDown(n - 1);
}""",
            'partial': """void countDown(int n) {
    // TODO: Complete the recursive countdown function
    // Hint: Base case when n < 1, output n, then recursive call
}""",
            'expected': """if (n < 1) {
        return;
    }
    cout << n << " ";
    countDown(n - 1);"""
        },
        {
            'name': 'Recursion Typing Exercise 3: Sum Series',
            'template': """int sumSeries(int n) {
    if (n <= 0) {
        return 0;
    }
    return n + sumSeries(n - 1);
}""",
            'partial': """int sumSeries(int n) {
    // TODO: Complete the recursive sum function
    // Hint: Base case returns 0, otherwise return n + recursive call
}""",
            'expected': """if (n <= 0) {
        return 0;
    }
    return n + sumSeries(n - 1);"""
        }
    ],
    'linked_list': [
        {
            'name': 'Linked List Typing Exercise 1: Display Largest',
            'template': """void displayLargest() {
    if (stackTop == nullptr) {
        return;
    }
    nodeType *current = stackTop;
    float max = current->info;
    while (current != nullptr) {
        if (current->info > max) {
            max = current->info;
        }
        current = current->next;
    }
    cout << "Largest: " << max << endl;
}""",
            'partial': """void displayLargest() {
    // TODO: Complete the function to find and display largest value
    // Hint: Check if stackTop is null, traverse list, compare values
}""",
            'expected': """if (stackTop == nullptr) {
        return;
    }
    nodeType *current = stackTop;
    float max = current->info;
    while (current != nullptr) {
        if (current->info > max) {
            max = current->info;
        }
        current = current->next;
    }
    cout << "Largest: " << max << endl;"""
        },
        {
            'name': 'Linked List Typing Exercise 2: Count Nodes',
            'template': """int countNodes() {
    int count = 0;
    nodeType *current = stackTop;
    while (current != nullptr) {
        count++;
        current = current->next;
    }
    return count;
}""",
            'partial': """int countNodes() {
    // TODO: Complete the function to count nodes
    // Hint: Initialize count to 0, traverse list, increment count
}""",
            'expected': """int count = 0;
    nodeType *current = stackTop;
    while (current != nullptr) {
        count++;
        current = current->next;
    }
    return count;"""
        },
        {
            'name': 'Linked List Typing Exercise 3: Sum All Values',
            'template': """float sumAll() {
    float sum = 0;
    nodeType *current = stackTop;
    while (current != nullptr) {
        sum = sum + current->info;
        current = current->next;
    }
    return sum;
}""",
            'partial': """float sumAll() {
    // TODO: Complete the function to sum all values
    // Hint: Initialize sum to 0, traverse list, add each value
}""",
            'expected': """float sum = 0;
    nodeType *current = stackTop;
    while (current != nullptr) {
        sum = sum + current->info;
        current = current->next;
    }
    return sum;"""
        }
    ]
}

def generate_typing_exercise(topic):
    """Generate typing mode exercise with partial code - randomly selects from multiple problems"""
    if topic not in TYPING_EXERCISES:
        topic = 'stacks'
    
    exercise = random.choice(TYPING_EXERCISES[topic])
    
    return {
        'type': 'typing_exercise',
        'topic': topic,
        'problem_name': exercise['name'],
        'template': exercise['template'],
        'partial_code': exercise['partial'],
        'expected_code': exercise['expected'],
        'hint': 'Type the missing code to complete the function. Pay attention to indentation and syntax.'
    }

def generate_exam_problem(topic, mode='drag_drop'):
    """
    Generate an exam review problem.
    
    Args:
        topic: 'stacks', 'queues', 'recursion', or 'linked_list'
        mode: 'drag_drop' or 'typing'
    
    Returns:
        Dictionary with problem data
    """
    if mode == 'typing':
        return generate_typing_exercise(topic)
    else:
        # Drag and drop mode
        if topic == 'stacks':
            return generate_stack_blocks()
        elif topic == 'queues':
            return generate_queue_blocks()
        elif topic == 'recursion':
            return generate_recursion_blocks()
        elif topic == 'linked_list':
            return generate_linked_list_blocks()
        else:
            return generate_stack_blocks()
