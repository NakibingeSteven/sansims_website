from flask import Flask, render_template

app = Flask(__name__)

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
    app.run(debug=True, host='0.0.0.0', port=5000)
