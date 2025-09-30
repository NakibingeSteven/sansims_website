from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'change-this-secret-key')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/solution')
def solution():
    return render_template('solution.html')

@app.route('/technology')
def technology():
    return render_template('technology.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use env PORT or default 5000
    app.run(host='0.0.0.0', port=port)