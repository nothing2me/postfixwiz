"""
Vercel serverless function entry point for Flask app
"""
from flask import Flask, render_template, request, jsonify, session
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.postfix import evaluate_postfix, is_valid_postfix
from utils.infix_to_postfix import infix_to_postfix, get_conversion_steps
from utils.problems import generate_problem, ProblemType
from utils.scratch_blocks import generate_scratch_problem
from utils.pseudo_code import generate_written_code_problem
from utils.big_o import generate_big_o_problem

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
            static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'))
app.secret_key = os.environ.get('SECRET_KEY', 'postfix_trainer_secret_key_2024_vercel')

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

@app.route('/big-o')
def big_o():
    """Big-O notation practice mode"""
    return render_template('big_o.html')

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
        # Calculate correct answer first, even if user answer is invalid
        correct_result = None
        try:
            correct_result = evaluate_postfix(original_expression)
        except Exception as e:
            # If evaluation fails, try to use the correct_answer from the problem
            if correct_answer is not None:
                try:
                    correct_result = float(correct_answer)
                except:
                    correct_result = correct_answer if correct_answer is not None else "N/A"
            else:
                correct_result = "N/A"
        
        try:
            user_result = float(user_answer)
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
        except Exception as e:
            # User answer is invalid, but still return the correct answer
            if 'stats' not in session:
                session['stats'] = {'correct': 0, 'total': 0, 'streak': 0, 'max_streak': 0}
            
            session['stats']['total'] += 1
            session['stats']['streak'] = 0
            session.modified = True
            
            return jsonify({
                'correct': False,
                'correct_answer': correct_result,
                'error': 'Invalid answer format',
                'stats': session['stats']
            })
    
    elif problem_type == 'convert':
        try:
            # Clean and normalize answers
            user_postfix = user_answer.replace(' ', '').upper()
            correct_postfix = correct_answer.replace(' ', '').upper() if correct_answer else ''
            
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
                'correct_answer': correct_answer if correct_answer else 'N/A',
                'stats': session['stats']
            })
        except Exception as e:
            # Ensure we always return correct_answer
            if 'stats' not in session:
                session['stats'] = {'correct': 0, 'total': 0, 'streak': 0, 'max_streak': 0}
            
            session['stats']['total'] += 1
            session['stats']['streak'] = 0
            session.modified = True
            
            return jsonify({
                'correct': False,
                'correct_answer': correct_answer if correct_answer else 'N/A',
                'error': 'Invalid answer format',
                'stats': session['stats']
            })
    
    return jsonify({
        'correct': False,
        'correct_answer': correct_answer if correct_answer else 'N/A',
        'error': 'Unknown problem type'
    })

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
    """Normalize code for comparison by removing leading/trailing whitespace from lines,
    removing empty lines, and normalizing case, while preserving structural characters."""
    # Split into lines, strip each line, and filter out empty lines
    lines = [line.strip() for line in code.split('\n') if line.strip()]
    # Join lines back with a single newline
    code = '\n'.join(lines)
    # Normalize case (preserves all structural characters like ; {} () etc.)
    code = code.lower()
    return code

@app.route('/api/generate-big-o-problem', methods=['POST'])
def api_generate_big_o_problem():
    """Generate a Big-O practice problem"""
    data = request.json
    difficulty = data.get('difficulty', 'easy')
    problem_type = data.get('type', 'both')
    
    problem = generate_big_o_problem(difficulty, problem_type)
    return jsonify(problem)

def normalize_big_o_answer(answer):
    """Normalize Big-O notation answer for comparison"""
    if not answer:
        return ''
    
    # Convert to lowercase and remove all whitespace
    normalized = answer.lower().replace(' ', '').replace('\t', '').replace('\n', '')
    
    # Remove O() wrapper if present but keep content
    if normalized.startswith('o(') and normalized.endswith(')'):
        normalized = normalized[2:-1]
    elif normalized.startswith('o'):
        normalized = normalized[1:]
        if normalized.startswith('(') and normalized.endswith(')'):
            normalized = normalized[1:-1]
    
    # Handle common variations
    # n^2, n2, n*n, n squared -> n²
    normalized = normalized.replace('n^2', 'n²').replace('n2', 'n²')
    normalized = normalized.replace('n*n', 'n²').replace('nsquared', 'n²')
    normalized = normalized.replace('n²²', 'n²')  # Fix double superscript
    
    # n^3, n3, n*n*n, n cubed -> n³
    normalized = normalized.replace('n^3', 'n³').replace('n3', 'n³')
    normalized = normalized.replace('n*n*n', 'n³').replace('ncubed', 'n³')
    normalized = normalized.replace('n³³', 'n³')  # Fix double superscript
    
    # Handle log variations
    normalized = normalized.replace('log(n)', 'logn').replace('log2(n)', 'logn')
    normalized = normalized.replace('log2n', 'logn').replace('log_2(n)', 'logn')
    
    # Handle special characters
    normalized = normalized.replace('²', '²').replace('³', '³')
    
    return normalized

@app.route('/api/get-written-code-problem', methods=['POST'])
def api_get_written_code_problem():
    """Get written code problem with stages and pseudo code"""
    data = request.json
    topic = data.get('topic', 'stack')
    
    problem = generate_written_code_problem(topic)
    return jsonify(problem)

@app.route('/api/check-written-code-stage', methods=['POST'])
def api_check_written_code_stage():
    """Check written code for a specific stage"""
    data = request.json
    user_code = data.get('user_code', '').strip()
    correct_code = data.get('correct_code', '').strip()
    stage_num = data.get('stage_num', 1)
    
    # Normalize code for comparison
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
        'message': f'Stage {stage_num} code is correct!' if is_correct else f'Stage {stage_num} code needs revision. Check syntax and logic.',
        'correct_code': correct_code,
        'stats': session['stats']
    })

@app.route('/api/check-big-o-answer', methods=['POST'])
def api_check_big_o_answer():
    """Check if user's Big-O answer is correct"""
    try:
        data = request.json
        if not data:
            return jsonify({'correct': False, 'error': 'No data provided', 'correct_answer': 'N/A'})
        
        problem_type = data.get('problem_type')
        user_answer = data.get('answer', '').strip() if data.get('answer') else ''
        correct_answer = data.get('correct_answer', '').strip() if data.get('correct_answer') else ''
        
        # Validate inputs
        if not user_answer:
            return jsonify({
                'correct': False,
                'error': 'Please provide an answer',
                'correct_answer': correct_answer if correct_answer else 'N/A'
            })
        
        if not correct_answer:
            return jsonify({
                'correct': False,
                'error': 'Problem data incomplete',
                'correct_answer': 'N/A'
            })
        
        # Normalize answers for comparison
        user_normalized = normalize_big_o_answer(user_answer)
        correct_normalized = normalize_big_o_answer(correct_answer)
        
        # Compare normalized answers
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
            'correct_answer': correct_answer,
            'stats': session['stats']
        })
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            'correct': False,
            'error': f'Error checking answer: {str(e)}',
            'correct_answer': data.get('correct_answer', 'N/A') if 'data' in locals() else 'N/A'
        })

# Export the app for Vercel
# Vercel's Python runtime will automatically detect the 'app' variable
__all__ = ['app']

