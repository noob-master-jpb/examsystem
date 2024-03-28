from flask import *

from models import *

from function_set import json_convertion

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db.init_app(app)

@app.route('/')
def login():
    with app.app_context():
        data = Login.query.all()
        for i in data:
            print(i.username)
    return jsonify([i.username for i in data])



if __name__ == '__main__':
    app.run(debug=True,port=80)