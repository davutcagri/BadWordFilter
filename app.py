from flask import Flask, request, jsonify

import assistant

app = Flask(__name__)

@app.route('/check',methods=['POST'])
def process_messages():
    try:
        data = request.json
        messages = data.get('messages', [])

        if not messages:
            return jsonify({'error': 'no messages'}, 400)

        responses = []
        for message in messages:
            response = assistant.checkMessage(message)
            responses.append({'message': message, 'isInsult': response})

        return jsonify({'response': responses})

    except Exception as ex:
        return jsonify({'error': str(ex)}, 500)