from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='1835')