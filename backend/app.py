"""
Flask API server for Wilderness Destinations Chatbot
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import WildernessChatbot
import uuid

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Initialize chatbot
chatbot = WildernessChatbot()

# Store sessions
sessions = {}


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.json
        user_message = data.get('message', '')
        session_id = data.get('session_id')
        
        # Create session if doesn't exist
        if not session_id:
            session_id = str(uuid.uuid4())
        
        if session_id not in sessions:
            sessions[session_id] = {
                'history': [],
                'user_id': session_id
            }
        
        # Process message
        response = chatbot.process_message(session_id, user_message)
        
        # Store in history
        sessions[session_id]['history'].append({
            'user': user_message,
            'bot': response
        })
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'response': response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/enquiry', methods=['POST'])
def submit_enquiry():
    """Handle enquiry form submissions"""
    try:
        data = request.json
        result = chatbot.submit_enquiry(data)
        
        return jsonify({
            'success': True,
            'result': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/camps', methods=['GET'])
def get_camps():
    """Get all camps or search camps"""
    try:
        query = request.args.get('q', '')
        country = request.args.get('country', '')
        
        if query:
            camps = chatbot.knowledge_base.search_camps(query)
        elif country:
            camps = chatbot.knowledge_base.get_camps_by_country(country)
        else:
            camps = chatbot.knowledge_base.camps
        
        from dataclasses import asdict
        camps_data = [asdict(camp) for camp in camps]
        
        return jsonify({
            'success': True,
            'camps': camps_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Wilderness Destinations Chatbot',
        'version': '1.1.0'
    })


if __name__ == '__main__':
    print("🌍 Wilderness Destinations Chatbot API Starting...")
    print("📍 Server running on http://localhost:5000")
    print("🦁 Ready to help travelers discover Africa's wilderness!")
    app.run(debug=True, host='0.0.0.0', port=5000)
