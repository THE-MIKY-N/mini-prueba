from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('click_button')
def handle_click(data):
    user = data.get('name', 'Anon')
    emit('server_msg', {'msg': f'👆 {user} hizo clic'}, broadcast=True)

if __name__ == '__main__':
    # Para ejecutar local:
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
