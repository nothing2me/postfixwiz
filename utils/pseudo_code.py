"""
Pseudo code generators for written code mode in exam review
Generates English pseudo code for each stage of code problems
"""

def generate_pseudo_code_for_stage(topic, stage_num, stage_data):
    """
    Generate English pseudo code for a specific stage.
    
    Args:
        topic: 'stack', 'queue', 'recursion', or 'binary_search'
        stage_num: Stage number (1, 2, 3, etc.)
        stage_data: Stage data dictionary with name, description, block_ids, etc.
    
    Returns:
        String with English pseudo code instructions
    """
    pseudo_code_map = {
        'stack': {
            1: """Stage 1: Class Definition
Create a template class named LinkedStack
Use the template keyword with Type parameter
Open the class with a curly brace {""",
            2: """Stage 2: Private Members
Declare a private section
Define a struct named nodeType with:
  - A data field (Type info)
  - A pointer to next node (nodeType *next)
Close the struct with };
Declare a pointer to nodeType named stackTop""",
            3: """Stage 3: Public Section & Constructor
Declare a public section
Create a constructor LinkedStack() that:
  - Initializes stackTop to nullptr""",
            4: """Stage 4: Public Methods
Implement push(newItem) function:
  - Create a new node
  - Set the new node's data to newItem
  - Link the new node to the top of stack
  - Update stackTop to point to the new node
  
Implement pop() function:
  - Check if stack is empty (stackTop == nullptr)
  - If empty, return early
  - Otherwise, save current top in a temporary pointer
  - Move stackTop to the next node
  - Delete the old top node
  
Implement top() function:
  - Check if stack is empty
  - If empty, throw an error
  - Otherwise, return the data at stackTop""",
            5: """Stage 5: Closing Brace
Close the class definition with };"""
        },
        'queue': {
            1: """Stage 1: Class Definition
Create a template class named LinkedQueue
Use the template keyword with Type parameter
Open the class with a curly brace {""",
            2: """Stage 2: Private Members
Declare a private section
Define a struct named nodeType with:
  - A data field (Type info)
  - A pointer to next node (nodeType *next)
Close the struct with };
Declare two pointers:
  - queueFront (points to front of queue)
  - queueRear (points to rear of queue)""",
            3: """Stage 3: Public Section & Constructor
Declare a public section
Create a constructor LinkedQueue() that:
  - Initializes queueFront to nullptr
  - Initializes queueRear to nullptr""",
            4: """Stage 4: Public Methods
Implement addQueue(newElement) function:
  - Create a new node
  - Set the new node's data to newElement
  - Set the new node's next to nullptr
  - If queue is empty (queueFront == nullptr):
    * Set both queueFront and queueRear to the new node
  - Otherwise:
    * Link the new node to the rear
    * Update queueRear to point to the new node
  
Implement deleteQueue() function:
  - Check if queue is empty (queueFront == nullptr)
  - If empty, return early
  - Otherwise, save current front in a temporary pointer
  - Move queueFront to the next node
  - Delete the old front node
  
Implement front() function:
  - Check if queue is empty
  - If empty, throw an error
  - Otherwise, return the data at queueFront""",
            5: """Stage 5: Closing Brace
Close the class definition with };"""
        },
        'recursion': {
            1: """Stage 1: Function Definition
Define a function named printSeries that:
  - Takes an integer parameter n
  - Returns void
  - Opens the function with a curly brace {""",
            2: """Stage 2: Base Case
Check if n is less than or equal to 0
If true, return immediately (stop recursion)""",
            3: """Stage 3: Recursive Case
Print the current value of n
Recursively call printSeries with n - 3
This will print: n, n-3, n-6, n-9... until n <= 0""",
            4: """Stage 4: Closing Brace
Close the function with }"""
        },
        'binary_search': {
            1: """Stage 1: Function Definition
Define a function named binarySearch that:
  - Takes parameters: array, left index, right index, target value
  - Returns an integer (index of target, or -1 if not found)
  - Opens the function with a curly brace {""",
            2: """Stage 2: Base Case
Check if left index is greater than right index
If true, return -1 (target not found)""",
            3: """Stage 3: Calculate Midpoint
Calculate the middle index: mid = (left + right) / 2""",
            4: """Stage 4: Check Midpoint
If the element at mid equals target:
  - Return mid (found the target)
  
If the element at mid is greater than target:
  - Search in the left half: binarySearch(arr, left, mid - 1, target)
  
Otherwise:
  - Search in the right half: binarySearch(arr, mid + 1, right, target)""",
            5: """Stage 5: Closing Brace
Close the function with }"""
        }
    }
    
    # Get pseudo code for the topic and stage
    if topic in pseudo_code_map and stage_num in pseudo_code_map[topic]:
        return pseudo_code_map[topic][stage_num]
    
    # Fallback to generic description
    return f"Stage {stage_num}: {stage_data.get('name', 'Complete this stage')}\n{stage_data.get('description', '')}"

def get_correct_code_for_stage(topic, stage_num, stage_data, all_blocks, correct_order):
    """
    Get the correct code for a specific stage.
    
    Args:
        topic: 'stack', 'queue', 'recursion', or 'binary_search'
        stage_num: Stage number
        stage_data: Stage data with block_ids
        all_blocks: List of all block dictionaries
        correct_order: List of block IDs in correct order
    
    Returns:
        String with correct code for this stage
    """
    # Get block IDs for this stage in correct order
    stage_block_ids = [bid for bid in correct_order if bid in stage_data.get('block_ids', [])]
    
    # Get the actual code text from blocks
    code_lines = []
    for block_id in stage_block_ids:
        block = next((b for b in all_blocks if b['id'] == block_id), None)
        if block:
            code_lines.append(block['text'])
    
    return '\n'.join(code_lines)

def generate_written_code_problem(topic):
    """
    Generate a written code problem for a topic using stages.
    
    Args:
        topic: 'stack', 'queue', 'recursion', or 'binary_search'
    
    Returns:
        Dictionary with problem data including stages and pseudo code
    """
    from utils.scratch_blocks import generate_stack_class_problem, generate_queue_class_problem, generate_recursion_function_problem, generate_binary_search_problem
    
    # Get the scratch problem which has stages based on topic
    if topic == 'stack':
        problem = generate_stack_class_problem()
    elif topic == 'queue':
        problem = generate_queue_class_problem()
    elif topic == 'recursion':
        problem = generate_recursion_function_problem()
    elif topic == 'binary_search':
        problem = generate_binary_search_problem()
    else:
        problem = generate_stack_class_problem()
    
    # Add pseudo code for each stage
    if 'stages' in problem:
        for stage_num, stage_data in problem['stages'].items():
            pseudo_code = generate_pseudo_code_for_stage(topic, stage_num, stage_data)
            stage_data['pseudo_code'] = pseudo_code
            
            # Also get the correct code for this stage
            correct_code = get_correct_code_for_stage(
                topic, 
                stage_num, 
                stage_data, 
                problem['blocks'], 
                problem['correct_order']
            )
            stage_data['correct_code'] = correct_code
    
    return problem

