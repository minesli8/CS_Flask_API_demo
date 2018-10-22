from flask import Flask, render_template
from flask_restful import abort, Api
from models.sentiment import sentiment_analyzer


app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def info():
    return render_template('info.html')

api.add_resource(sentiment_analyzer, '/sentiment')

if __name__ == '__main__':
    app.run(debug=False)
