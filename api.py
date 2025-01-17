from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
from io import BytesIO
from model import generate_image

app = Flask(__name__)
CORS(app)  # This will allow all domains by default

@app.route('/generate-image', methods=['POST'])
def generate_image_route():
    try:
        data = request.get_json()
        prompt = data.get('prompt')
        negative_prompt = data.get('negative_prompt', None)

        if not prompt:
            return jsonify({'error': 'Prompt is required!'}), 400

        image = generate_image(prompt, negative_prompt)

        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return jsonify({'image': img_str})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
