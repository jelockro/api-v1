from flask import Flask
from routes.mongo_router import mongo
from routes.puppet_router import puppet

app = Flask(__name__)
app.register_blueprint(mongo)
app.register_blueprint(puppet)



# @app.route('/')
# def index():
#     return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)