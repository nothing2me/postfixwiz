"""
Exam review problem generators with code blocks for drag-and-drop and typing modes
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

def generate_stack_blocks():
    """Generate code blocks for stack operations"""
    blocks = [
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
    ]
    
    # Shuffle blocks for drag-and-drop
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'stack_blocks',
        'correct_blocks': blocks,
        'shuffled_blocks': shuffled,
        'correct_code': '\n'.join([b['code'] for b in blocks]),
        'hint': 'Remember: Declare stack and variables first, then perform operations, finally output results.'
    }

def generate_queue_blocks():
    """Generate code blocks for queue operations"""
    blocks = [
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
    ]
    
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'queue_blocks',
        'correct_blocks': blocks,
        'shuffled_blocks': shuffled,
        'correct_code': '\n'.join([b['code'] for b in blocks]),
        'hint': 'Remember: Declare queue and variables first, then addQueue adds to rear, deleteQueue removes from front.'
    }

def generate_recursion_blocks():
    """Generate code blocks for recursive function"""
    blocks = [
        {"id": "1", "code": "void printSeries(int n) {", "type": "function_declaration", "order": 1},
        {"id": "2", "code": "    if (n <= 0) {", "type": "condition", "order": 2},
        {"id": "3", "code": "        return;", "type": "base_case", "order": 3},
        {"id": "4", "code": "    }", "type": "closing", "order": 4},
        {"id": "5", "code": "    cout << n << \" \";", "type": "output", "order": 5},
        {"id": "6", "code": "    printSeries(n - 3);", "type": "recursive_call", "order": 6},
        {"id": "7", "code": "}", "type": "closing", "order": 7},
    ]
    
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'recursion_blocks',
        'correct_blocks': blocks,
        'shuffled_blocks': shuffled,
        'correct_code': '\n'.join([b['code'] for b in blocks]),
        'hint': 'Remember: Base case first (n <= 0), then output current value, then recursive call with n-3.'
    }

def generate_linked_list_blocks():
    """Generate code blocks for linked list display largest function"""
    blocks = [
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
    ]
    
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'linked_list_blocks',
        'correct_blocks': blocks,
        'shuffled_blocks': shuffled,
        'correct_code': '\n'.join([b['code'] for b in blocks]),
        'hint': 'Remember: Check for empty list, initialize max with first element, traverse and compare, update max if larger.'
    }

def generate_typing_exercise(topic):
    """Generate typing mode exercise with partial code"""
    exercises = {
        'stacks': {
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
        'queues': {
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
        'recursion': {
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
        'linked_list': {
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
        }
    }
    
    if topic not in exercises:
        topic = 'stacks'
    
    return {
        'type': 'typing_exercise',
        'topic': topic,
        'template': exercises[topic]['template'],
        'partial_code': exercises[topic]['partial'],
        'expected_code': exercises[topic]['expected'],
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
