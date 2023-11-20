from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:times>/<word>')
def repeat_word(times, word):
    return f'{word} ' * times

if __name__ == '__main__':
    app.run(debug=True, port=5000)
