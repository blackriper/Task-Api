from  flask import Flask
from routes.routes import taskes
from flask_cors import CORS

app= Flask(__name__)
cors=CORS(app)
app.config.from_pyfile('./config/config.py')
app.register_blueprint(taskes,url_prefix='/api')


if __name__ == '__main__':
    app.run()