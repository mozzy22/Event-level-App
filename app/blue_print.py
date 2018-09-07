from flask import  Blueprint
from flask import jsonify

user_blueprint = Blueprint('user_blue', __name__ )

@user_blueprint.route('/blue', methods = ["GET"])
def index():
    "An example of a blue print"
    return jsonify({"message": "This is a blue print"})