from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph1')
def graph1():
    # Lógica para Graph1
    return 'Esta es la ruta para Graph1'

@app.route('/graph2')
def graph2():
    # Lógica para Graph2
    return 'Esta es la ruta para Graph2'

@app.route('/graph3')
def graph3():
    # Lógica para Graph3
    return 'Esta es la ruta para Graph3'

@app.route('/graph4')
def graph3():
    # Lógica para Graph4
    return 'Esta es la ruta para Graph4'

if __name__ == '__main__':
    app.run(debug=True)
