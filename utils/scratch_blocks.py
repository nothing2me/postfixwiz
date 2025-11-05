"""
Scratch-like code block definitions for exam review
Blocks are organized into logical groups that connect together
"""

from enum import Enum
import random

class BlockType(Enum):
    CLASS_DEF = "class_def"
    STRUCT_DEF = "struct_def"
    FUNCTION_DEF = "function_def"
    MEMBER_VAR = "member_var"
    CONSTRUCTOR = "constructor"
    DESTRUCTOR = "destructor"
    RETURN = "return"
    CONDITION = "condition"
    LOOP = "loop"
    STATEMENT = "statement"
    EXPRESSION = "expression"

def generate_stack_class_problem():
    """Generate blocks for building a Stack linked list class with logical grouping"""
    # Organized into logical groups that connect together
    blocks = [
        # Group 1: Class definition start
        {
            'id': 'b1',
            'type': 'class_def',
            'text': 'template <class Type>\nclass LinkedStack {',
            'shape': 'hat',
            'indent': 0,
            'group': 1,
            'order_in_group': 1
        },
        # Group 2: Private section
        {
            'id': 'b2',
            'type': 'member_var',
            'text': 'private:',
            'shape': 'stack',
            'indent': 0,
            'group': 2,
            'order_in_group': 1
        },
        {
            'id': 'b3',
            'type': 'struct_def',
            'text': 'struct nodeType {',
            'shape': 'stack',
            'indent': 1,
            'group': 2,
            'order_in_group': 2
        },
        {
            'id': 'b3a',
            'type': 'member_var',
            'text': '    Type info;',
            'shape': 'stack',
            'indent': 2,
            'group': 2,
            'order_in_group': 3
        },
        {
            'id': 'b3b',
            'type': 'member_var',
            'text': '    nodeType *next;',
            'shape': 'stack',
            'indent': 2,
            'group': 2,
            'order_in_group': 4
        },
        {
            'id': 'b3c',
            'type': 'statement',
            'text': '};',
            'shape': 'stack',
            'indent': 1,
            'group': 2,
            'order_in_group': 5
        },
        {
            'id': 'b4',
            'type': 'member_var',
            'text': 'nodeType *stackTop;',
            'shape': 'stack',
            'indent': 1,
            'group': 2,
            'order_in_group': 6
        },
        # Group 3: Public section
        {
            'id': 'b5',
            'type': 'member_var',
            'text': 'public:',
            'shape': 'stack',
            'indent': 0,
            'group': 3,
            'order_in_group': 1
        },
        # Group 4: Constructor
        {
            'id': 'b6',
            'type': 'constructor',
            'text': 'LinkedStack() {',
            'shape': 'stack',
            'indent': 1,
            'group': 4,
            'order_in_group': 1
        },
        {
            'id': 'b6a',
            'type': 'statement',
            'text': '    stackTop = nullptr;',
            'shape': 'stack',
            'indent': 2,
            'group': 4,
            'order_in_group': 2
        },
        {
            'id': 'b6b',
            'type': 'statement',
            'text': '}',
            'shape': 'stack',
            'indent': 1,
            'group': 4,
            'order_in_group': 3
        },
        # Group 5: Push function
        {
            'id': 'b7',
            'type': 'function_def',
            'text': 'void push(const Type& newItem) {',
            'shape': 'stack',
            'indent': 1,
            'group': 5,
            'order_in_group': 1
        },
        {
            'id': 'b8',
            'type': 'statement',
            'text': '    nodeType *newNode;',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 2
        },
        {
            'id': 'b9',
            'type': 'statement',
            'text': '    newNode = new nodeType;',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 3
        },
        {
            'id': 'b10',
            'type': 'statement',
            'text': '    newNode->info = newItem;',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 4
        },
        {
            'id': 'b11',
            'type': 'statement',
            'text': '    newNode->next = stackTop;',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 5
        },
        {
            'id': 'b12',
            'type': 'statement',
            'text': '    stackTop = newNode;',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 6
        },
        {
            'id': 'b7a',
            'type': 'statement',
            'text': '}',
            'shape': 'stack',
            'indent': 1,
            'group': 5,
            'order_in_group': 7
        },
        # Group 6: Pop function
        {
            'id': 'b13',
            'type': 'function_def',
            'text': 'void pop() {',
            'shape': 'stack',
            'indent': 1,
            'group': 6,
            'order_in_group': 1
        },
        {
            'id': 'b14',
            'type': 'condition',
            'text': '    if (stackTop == nullptr) {',
            'shape': 'stack',
            'indent': 2,
            'group': 6,
            'order_in_group': 2
        },
        {
            'id': 'b15',
            'type': 'return',
            'text': '        return;',
            'shape': 'stack',
            'indent': 3,
            'group': 6,
            'order_in_group': 3
        },
        {
            'id': 'b14a',
            'type': 'statement',
            'text': '    }',
            'shape': 'stack',
            'indent': 2,
            'group': 6,
            'order_in_group': 4
        },
        {
            'id': 'b16',
            'type': 'statement',
            'text': '    nodeType *temp = stackTop;',
            'shape': 'stack',
            'indent': 2,
            'group': 6,
            'order_in_group': 5
        },
        {
            'id': 'b17',
            'type': 'statement',
            'text': '    stackTop = stackTop->next;',
            'shape': 'stack',
            'indent': 2,
            'group': 6,
            'order_in_group': 6
        },
        {
            'id': 'b18',
            'type': 'statement',
            'text': '    delete temp;',
            'shape': 'stack',
            'indent': 2,
            'group': 6,
            'order_in_group': 7
        },
        {
            'id': 'b13a',
            'type': 'statement',
            'text': '}',
            'shape': 'stack',
            'indent': 1,
            'group': 6,
            'order_in_group': 8
        },
        # Group 7: Top function
        {
            'id': 'b19',
            'type': 'function_def',
            'text': 'Type top() const {',
            'shape': 'stack',
            'indent': 1,
            'group': 7,
            'order_in_group': 1
        },
        {
            'id': 'b20',
            'type': 'condition',
            'text': '    if (stackTop == nullptr) {',
            'shape': 'stack',
            'indent': 2,
            'group': 7,
            'order_in_group': 2
        },
        {
            'id': 'b21',
            'type': 'statement',
            'text': '        throw "Stack is empty";',
            'shape': 'stack',
            'indent': 3,
            'group': 7,
            'order_in_group': 3
        },
        {
            'id': 'b20a',
            'type': 'statement',
            'text': '    }',
            'shape': 'stack',
            'indent': 2,
            'group': 7,
            'order_in_group': 4
        },
        {
            'id': 'b22',
            'type': 'return',
            'text': '    return stackTop->info;',
            'shape': 'stack',
            'indent': 2,
            'group': 7,
            'order_in_group': 5
        },
        {
            'id': 'b19a',
            'type': 'statement',
            'text': '}',
            'shape': 'stack',
            'indent': 1,
            'group': 7,
            'order_in_group': 6
        },
        # Group 8: Class closing
        {
            'id': 'b23',
            'type': 'statement',
            'text': '};',
            'shape': 'cap',
            'indent': 0,
            'group': 8,
            'order_in_group': 1
        }
    ]
    
    # Build correct order from groups
    correct_order = []
    groups = {}
    for block in blocks:
        group_id = block['group']
        if group_id not in groups:
            groups[group_id] = []
        groups[group_id].append(block)
    
    # Sort each group by order_in_group
    for group_id in sorted(groups.keys()):
        groups[group_id].sort(key=lambda x: x['order_in_group'])
        correct_order.extend([b['id'] for b in groups[group_id]])
    
    # Shuffle blocks for drag-and-drop, but keep groups together
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'stack_class',
        'question': 'Build a Stack linked list class with the following methods: push, pop, and top. Use the provided code blocks to assemble the complete class definition.',
        'blocks': shuffled,
        'correct_order': correct_order,
        'groups': groups,
        'hint': 'Start with class definition, then private members (struct and pointer), then public methods (constructor, push, pop, top), and end with closing brace. Function bodies should be grouped with their function definitions.'
    }

def generate_queue_class_problem():
    """Generate blocks for building a Queue linked list class with logical grouping"""
    blocks = [
        # Group 1: Class definition
        {
            'id': 'q1',
            'type': 'class_def',
            'text': 'template <class Type>\nclass LinkedQueue {',
            'shape': 'hat',
            'indent': 0,
            'group': 1,
            'order_in_group': 1
        },
        # Group 2: Private section
        {
            'id': 'q2',
            'type': 'member_var',
            'text': 'private:',
            'shape': 'stack',
            'indent': 0,
            'group': 2,
            'order_in_group': 1
        },
        {
            'id': 'q3',
            'type': 'struct_def',
            'text': 'struct nodeType {',
            'shape': 'stack',
            'indent': 1,
            'group': 2,
            'order_in_group': 2
        },
        {
            'id': 'q3a',
            'type': 'member_var',
            'text': '    Type info;',
            'shape': 'stack',
            'indent': 2,
            'group': 2,
            'order_in_group': 3
        },
        {
            'id': 'q3b',
            'type': 'member_var',
            'text': '    nodeType *next;',
            'shape': 'stack',
            'indent': 2,
            'group': 2,
            'order_in_group': 4
        },
        {
            'id': 'q3c',
            'type': 'statement',
            'text': '};',
            'shape': 'stack',
            'indent': 1,
            'group': 2,
            'order_in_group': 5
        },
        {
            'id': 'q4',
            'type': 'member_var',
            'text': 'nodeType *queueFront;',
            'shape': 'stack',
            'indent': 1,
            'group': 2,
            'order_in_group': 6
        },
        {
            'id': 'q5',
            'type': 'member_var',
            'text': 'nodeType *queueRear;',
            'shape': 'stack',
            'indent': 1,
            'group': 2,
            'order_in_group': 7
        },
        # Group 3: Public section
        {
            'id': 'q6',
            'type': 'member_var',
            'text': 'public:',
            'shape': 'stack',
            'indent': 0,
            'group': 3,
            'order_in_group': 1
        },
        # Group 4: Constructor
        {
            'id': 'q7',
            'type': 'constructor',
            'text': 'LinkedQueue() {',
            'shape': 'stack',
            'indent': 1,
            'group': 4,
            'order_in_group': 1
        },
        {
            'id': 'q7a',
            'type': 'statement',
            'text': '    queueFront = nullptr;',
            'shape': 'stack',
            'indent': 2,
            'group': 4,
            'order_in_group': 2
        },
        {
            'id': 'q7b',
            'type': 'statement',
            'text': '    queueRear = nullptr;',
            'shape': 'stack',
            'indent': 2,
            'group': 4,
            'order_in_group': 3
        },
        {
            'id': 'q7c',
            'type': 'statement',
            'text': '}',
            'shape': 'stack',
            'indent': 1,
            'group': 4,
            'order_in_group': 4
        },
        # Group 5: addQueue function
        {
            'id': 'q8',
            'type': 'function_def',
            'text': 'void addQueue(const Type& newElement) {',
            'shape': 'stack',
            'indent': 1,
            'group': 5,
            'order_in_group': 1
        },
        {
            'id': 'q9',
            'type': 'statement',
            'text': '    nodeType *newNode = new nodeType;',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 2
        },
        {
            'id': 'q10',
            'type': 'statement',
            'text': '    newNode->info = newElement;',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 3
        },
        {
            'id': 'q11',
            'type': 'statement',
            'text': '    newNode->next = nullptr;',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 4
        },
        {
            'id': 'q12',
            'type': 'condition',
            'text': '    if (queueFront == nullptr) {',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 5
        },
        {
            'id': 'q13',
            'type': 'statement',
            'text': '        queueFront = newNode;',
            'shape': 'stack',
            'indent': 3,
            'group': 5,
            'order_in_group': 6
        },
        {
            'id': 'q14',
            'type': 'statement',
            'text': '        queueRear = newNode;',
            'shape': 'stack',
            'indent': 3,
            'group': 5,
            'order_in_group': 7
        },
        {
            'id': 'q12a',
            'type': 'statement',
            'text': '    }',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 8
        },
        {
            'id': 'q15',
            'type': 'statement',
            'text': '    else {',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 9
        },
        {
            'id': 'q16',
            'type': 'statement',
            'text': '        queueRear->next = newNode;',
            'shape': 'stack',
            'indent': 3,
            'group': 5,
            'order_in_group': 10
        },
        {
            'id': 'q17',
            'type': 'statement',
            'text': '        queueRear = newNode;',
            'shape': 'stack',
            'indent': 3,
            'group': 5,
            'order_in_group': 11
        },
        {
            'id': 'q15a',
            'type': 'statement',
            'text': '    }',
            'shape': 'stack',
            'indent': 2,
            'group': 5,
            'order_in_group': 12
        },
        {
            'id': 'q8a',
            'type': 'statement',
            'text': '}',
            'shape': 'stack',
            'indent': 1,
            'group': 5,
            'order_in_group': 13
        },
        # Group 6: deleteQueue function
        {
            'id': 'q18',
            'type': 'function_def',
            'text': 'void deleteQueue() {',
            'shape': 'stack',
            'indent': 1,
            'group': 6,
            'order_in_group': 1
        },
        {
            'id': 'q19',
            'type': 'condition',
            'text': '    if (queueFront == nullptr) {',
            'shape': 'stack',
            'indent': 2,
            'group': 6,
            'order_in_group': 2
        },
        {
            'id': 'q20',
            'type': 'return',
            'text': '        return;',
            'shape': 'stack',
            'indent': 3,
            'group': 6,
            'order_in_group': 3
        },
        {
            'id': 'q19a',
            'type': 'statement',
            'text': '    }',
            'shape': 'stack',
            'indent': 2,
            'group': 6,
            'order_in_group': 4
        },
        {
            'id': 'q21',
            'type': 'statement',
            'text': '    nodeType *temp = queueFront;',
            'shape': 'stack',
            'indent': 2,
            'group': 6,
            'order_in_group': 5
        },
        {
            'id': 'q22',
            'type': 'statement',
            'text': '    queueFront = queueFront->next;',
            'shape': 'stack',
            'indent': 2,
            'group': 6,
            'order_in_group': 6
        },
        {
            'id': 'q23',
            'type': 'statement',
            'text': '    delete temp;',
            'shape': 'stack',
            'indent': 2,
            'group': 6,
            'order_in_group': 7
        },
        {
            'id': 'q18a',
            'type': 'statement',
            'text': '}',
            'shape': 'stack',
            'indent': 1,
            'group': 6,
            'order_in_group': 8
        },
        # Group 7: front function
        {
            'id': 'q24',
            'type': 'function_def',
            'text': 'Type front() const {',
            'shape': 'stack',
            'indent': 1,
            'group': 7,
            'order_in_group': 1
        },
        {
            'id': 'q25',
            'type': 'condition',
            'text': '    if (queueFront == nullptr) {',
            'shape': 'stack',
            'indent': 2,
            'group': 7,
            'order_in_group': 2
        },
        {
            'id': 'q26',
            'type': 'statement',
            'text': '        throw "Queue is empty";',
            'shape': 'stack',
            'indent': 3,
            'group': 7,
            'order_in_group': 3
        },
        {
            'id': 'q25a',
            'type': 'statement',
            'text': '    }',
            'shape': 'stack',
            'indent': 2,
            'group': 7,
            'order_in_group': 4
        },
        {
            'id': 'q27',
            'type': 'return',
            'text': '    return queueFront->info;',
            'shape': 'stack',
            'indent': 2,
            'group': 7,
            'order_in_group': 5
        },
        {
            'id': 'q24a',
            'type': 'statement',
            'text': '}',
            'shape': 'stack',
            'indent': 1,
            'group': 7,
            'order_in_group': 6
        },
        # Group 8: Class closing
        {
            'id': 'q28',
            'type': 'statement',
            'text': '};',
            'shape': 'cap',
            'indent': 0,
            'group': 8,
            'order_in_group': 1
        }
    ]
    
    # Build correct order from groups
    correct_order = []
    groups = {}
    for block in blocks:
        group_id = block['group']
        if group_id not in groups:
            groups[group_id] = []
        groups[group_id].append(block)
    
    # Sort each group by order_in_group
    for group_id in sorted(groups.keys()):
        groups[group_id].sort(key=lambda x: x['order_in_group'])
        correct_order.extend([b['id'] for b in groups[group_id]])
    
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'queue_class',
        'question': 'Build a Queue linked list class with the following methods: addQueue, deleteQueue, and front. Use the provided code blocks to assemble the complete class definition.',
        'blocks': shuffled,
        'correct_order': correct_order,
        'groups': groups,
        'hint': 'Start with class definition, then private members (struct and pointers), then public methods (constructor, addQueue, deleteQueue, front), and end with closing brace.'
    }

def generate_recursion_function_problem():
    """Generate blocks for building a recursive function with logical grouping"""
    blocks = [
        {
            'id': 'r1',
            'type': 'function_def',
            'text': 'void printSeries(int n) {',
            'shape': 'hat',
            'indent': 0,
            'group': 1,
            'order_in_group': 1
        },
        {
            'id': 'r2',
            'type': 'condition',
            'text': '    if (n <= 0) {',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 2
        },
        {
            'id': 'r3',
            'type': 'return',
            'text': '        return;',
            'shape': 'stack',
            'indent': 2,
            'group': 1,
            'order_in_group': 3
        },
        {
            'id': 'r2a',
            'type': 'statement',
            'text': '    }',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 4
        },
        {
            'id': 'r4',
            'type': 'statement',
            'text': '    cout << n << " ";',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 5
        },
        {
            'id': 'r5',
            'type': 'statement',
            'text': '    printSeries(n - 3);',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 6
        },
        {
            'id': 'r1a',
            'type': 'statement',
            'text': '}',
            'shape': 'cap',
            'indent': 0,
            'group': 1,
            'order_in_group': 7
        }
    ]
    
    correct_order = [b['id'] for b in blocks]
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'recursion',
        'question': 'Build a recursive function that prints: n, n-3, n-6, n-9... until n <= 0. Use the provided code blocks to assemble the function.',
        'blocks': shuffled,
        'correct_order': correct_order,
        'groups': {1: blocks},
        'hint': 'Start with function definition, then base case (if n <= 0 return), then print n, then recursive call with n-3, and close with brace.'
    }

def generate_binary_search_problem():
    """Generate blocks for building a binary search function with logical grouping"""
    blocks = [
        {
            'id': 'bs1',
            'type': 'function_def',
            'text': 'int binarySearch(int arr[], int left, int right, int target) {',
            'shape': 'hat',
            'indent': 0,
            'group': 1,
            'order_in_group': 1
        },
        {
            'id': 'bs2',
            'type': 'condition',
            'text': '    if (left > right) {',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 2
        },
        {
            'id': 'bs3',
            'type': 'return',
            'text': '        return -1;',
            'shape': 'stack',
            'indent': 2,
            'group': 1,
            'order_in_group': 3
        },
        {
            'id': 'bs2a',
            'type': 'statement',
            'text': '    }',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 4
        },
        {
            'id': 'bs4',
            'type': 'statement',
            'text': '    int mid = (left + right) / 2;',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 5
        },
        {
            'id': 'bs5',
            'type': 'condition',
            'text': '    if (arr[mid] == target) {',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 6
        },
        {
            'id': 'bs6',
            'type': 'return',
            'text': '        return mid;',
            'shape': 'stack',
            'indent': 2,
            'group': 1,
            'order_in_group': 7
        },
        {
            'id': 'bs5a',
            'type': 'statement',
            'text': '    }',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 8
        },
        {
            'id': 'bs7',
            'type': 'condition',
            'text': '    if (arr[mid] > target) {',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 9
        },
        {
            'id': 'bs8',
            'type': 'return',
            'text': '        return binarySearch(arr, left, mid - 1, target);',
            'shape': 'stack',
            'indent': 2,
            'group': 1,
            'order_in_group': 10
        },
        {
            'id': 'bs7a',
            'type': 'statement',
            'text': '    }',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 11
        },
        {
            'id': 'bs9',
            'type': 'return',
            'text': '    return binarySearch(arr, mid + 1, right, target);',
            'shape': 'stack',
            'indent': 1,
            'group': 1,
            'order_in_group': 12
        },
        {
            'id': 'bs1a',
            'type': 'statement',
            'text': '}',
            'shape': 'cap',
            'indent': 0,
            'group': 1,
            'order_in_group': 13
        }
    ]
    
    correct_order = [b['id'] for b in blocks]
    shuffled = blocks.copy()
    random.shuffle(shuffled)
    
    return {
        'type': 'binary_search',
        'question': 'Build a recursive binary search function that finds target in sorted array. Use the provided code blocks to assemble the function.',
        'blocks': shuffled,
        'correct_order': correct_order,
        'groups': {1: blocks},
        'hint': 'Start with function definition, then base case (if left > right return -1), calculate mid, check if found, then recursively search left or right half.'
    }

def generate_scratch_problem(topic):
    """
    Generate a Scratch-like problem for a specific topic.
    
    Args:
        topic: 'stack', 'queue', 'recursion', or 'binary_search'
    
    Returns:
        Dictionary with problem data including blocks
    """
    if topic == 'stack':
        return generate_stack_class_problem()
    elif topic == 'queue':
        return generate_queue_class_problem()
    elif topic == 'recursion':
        return generate_recursion_function_problem()
    elif topic == 'binary_search':
        return generate_binary_search_problem()
    else:
        return generate_stack_class_problem()
