from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user_input = request.form['user_input']
        print(f"User submitted: {user_input}")  # Console output
        return f"You submitted: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)