from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/landing01')
def landing01():
    return render_template('landing01.html')

if __name__ == '__main__':
    app.run(debug=True)