from flask import Flask, render_template, request, jsonify, session
import random
import json
from utils.postfix import evaluate_postfix, is_valid_postfix
from utils.infix_to_postfix import infix_to_postfix, get_conversion_steps
from utils.problems import generate_problem, ProblemType
from utils.scratch_blocks import generate_scratch_problem

app = Flask(__name__)
app.secret_key = 'postfix_trainer_secret_key_2024'

@app.route('/')
def index():
    """Home page with introduction"""
    return render_template('index.html')

@app.route('/learn')
def learn():
    """Learn mode - step-by-step tutorial"""
    return render_template('learn.html')

@app.route('/practice')
def practice():
    """Practice mode - interactive problems"""
    return render_template('practice.html')

@app.route('/results')
def results():
    """Results page showing progress"""
    return render_template('results.html')

@app.route('/exam-review')
def exam_review():
    """Exam review mode - topic-specific study games"""
    return render_template('exam_review.html')

# API Routes
@app.route('/api/generate-problem', methods=['POST'])
def api_generate_problem():
    """Generate a random problem"""
    data = request.json
    difficulty = data.get('difficulty', 'easy')
    problem_type = data.get('type', 'both')
    use_variables = data.get('use_variables', False)
    
    problem = generate_problem(difficulty, problem_type, use_variables)
    return jsonify(problem)

@app.route('/api/check-answer', methods=['POST'])
def api_check_answer():
    """Check if user's answer is correct"""
    data = request.json
    problem_type = data.get('problem_type')
    user_answer = data.get('answer')
    correct_answer = data.get('correct_answer')
    original_expression = data.get('original_expression')
    
    if problem_type == 'evaluate':
        try:
            user_result = float(user_answer)
            correct_result = evaluate_postfix(original_expression)
            is_correct = abs(user_result - correct_result) < 0.0001
            
            # Update session stats
            if 'stats' not in session:
                session['stats'] = {'correct': 0, 'total': 0, 'streak': 0, 'max_streak': 0}
            
            session['stats']['total'] += 1
            if is_correct:
                session['stats']['correct'] += 1
                session['stats']['streak'] += 1
                if session['stats']['streak'] > session['stats']['max_streak']:
                    session['stats']['max_streak'] = session['stats']['streak']
            else:
                session['stats']['streak'] = 0
            
            session.modified = True
            
            return jsonify({
                'correct': is_correct,
                'correct_answer': correct_result,
                'stats': session['stats']
            })
        except:
            return jsonify({'correct': False, 'error': 'Invalid answer format'})
    
    elif problem_type == 'convert':
        try:
            # Clean and normalize answers
            user_postfix = user_answer.replace(' ', '').upper()
            correct_postfix = correct_answer.replace(' ', '').upper()
            
            is_correct = user_postfix == correct_postfix
            
            # Update session stats
            if 'stats' not in session:
                session['stats'] = {'correct': 0, 'total': 0, 'streak': 0, 'max_streak': 0}
            
            session['stats']['total'] += 1
            if is_correct:
                session['stats']['correct'] += 1
                session['stats']['streak'] += 1
                if session['stats']['streak'] > session['stats']['max_streak']:
                    session['stats']['max_streak'] = session['stats']['streak']
            else:
                session['stats']['streak'] = 0
            
            session.modified = True
            
            return jsonify({
                'correct': is_correct,
                'correct_answer': correct_answer,
                'stats': session['stats']
            })
        except:
            return jsonify({'correct': False, 'error': 'Invalid answer format'})
    
    return jsonify({'correct': False, 'error': 'Unknown problem type'})

@app.route('/api/get-stats', methods=['GET'])
def api_get_stats():
    """Get user statistics"""
    if 'stats' not in session:
        session['stats'] = {'correct': 0, 'total': 0, 'streak': 0, 'max_streak': 0}
    
    stats = session['stats']
    accuracy = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
    
    return jsonify({
        'stats': stats,
        'accuracy': round(accuracy, 1)
    })

@app.route('/api/get-conversion-steps', methods=['POST'])
def api_get_conversion_steps():
    """Get step-by-step conversion from infix to postfix"""
    data = request.json
    infix_expr = data.get('expression')
    
    if not infix_expr:
        return jsonify({'error': 'No expression provided'})
    
    steps = get_conversion_steps(infix_expr)
    postfix_result = infix_to_postfix(infix_expr)
    
    return jsonify({
        'steps': steps,
        'result': postfix_result
    })

@app.route('/api/reset-stats', methods=['POST'])
def api_reset_stats():
    """Reset user statistics"""
    session['stats'] = {'correct': 0, 'total': 0, 'streak': 0, 'max_streak': 0}
    session.modified = True
    return jsonify({'success': True})

@app.route('/api/generate-exam-problem', methods=['POST'])
def api_generate_exam_problem():
    """Generate an exam review problem"""
    data = request.json
    topic = data.get('topic', 'stacks')
    mode = data.get('mode', 'drag_drop')
    
    problem = generate_exam_problem(topic, mode)
    return jsonify(problem)

@app.route('/api/get-scratch-problem', methods=['POST'])
def api_get_scratch_problem():
    """Get Scratch-like problem with code blocks"""
    data = request.json
    topic = data.get('topic', 'stack')
    
    result = generate_scratch_problem(topic)
    return jsonify(result)

@app.route('/api/get-typing-problem', methods=['POST'])
def api_get_typing_problem():
    """Get typing problem"""
    data = request.json
    topic = data.get('topic', 'stack')
    
    problem = generate_typing_problem(topic)
    return jsonify(problem)

@app.route('/api/check-typing-code', methods=['POST'])
def api_check_typing_code():
    """Check typed code for accuracy"""
    data = request.json
    user_code = data.get('user_code', '').strip()
    correct_code = data.get('correct_code', '').strip()
    topic = data.get('topic', 'stack')
    
    # Normalize code for comparison (remove whitespace differences)
    user_normalized = normalize_code(user_code)
    correct_normalized = normalize_code(correct_code)
    
    # Check if code matches
    is_correct = user_normalized == correct_normalized
    
    # Update session stats
    if 'stats' not in session:
        session['stats'] = {'correct': 0, 'total': 0, 'streak': 0, 'max_streak': 0}
    
    session['stats']['total'] += 1
    if is_correct:
        session['stats']['correct'] += 1
        session['stats']['streak'] += 1
        if session['stats']['streak'] > session['stats']['max_streak']:
            session['stats']['max_streak'] = session['stats']['streak']
    else:
        session['stats']['streak'] = 0
    
    session.modified = True
    
    return jsonify({
        'correct': is_correct,
        'message': 'Code matches!' if is_correct else 'Code does not match. Check syntax and logic.',
        'stats': session['stats']
    })

def normalize_code(code):
    """Normalize code for comparison by removing extra whitespace and normalizing"""
    # Remove all whitespace
    code = ''.join(code.split())
    # Normalize case
    code = code.lower()
    # Remove common formatting differences
    code = code.replace(';', '')
    code = code.replace('{', '')
    code = code.replace('}', '')
    code = code.replace('(', '')
    code = code.replace(')', '')
    return code

if __name__ == '__main__':
    app.run(debug=True, port=5000)

