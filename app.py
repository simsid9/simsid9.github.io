from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/letter')  # Define a new route for '/letter'
def letter():
    return render_template('letter.html')

if __name__ == '__main__':
    app.run(debug=True)
