from flask import Flask, jsonify

app = Flask(__name__)



@app.route('/')
def saludo():
    return 'Hola qué tal!'

if __name__ == "__main__":
    app.run(debug=True, port=4000)

