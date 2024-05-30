from flask import Flask, jsonify, render_template
from flask_frozen import Freezer
import subprocess

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        result = subprocess.run(['python', 'koko.py'], capture_output=True, text=True)
        return jsonify({'output': result.stdout, 'error': result.stderr})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    freezer.freeze()  # Generate static HTML files
