from flask import Flask


app = Flask(__name__)
from views import *





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5153, debug=True)
    # app.run(debug=True)