from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask import json
from users_model import Users
from blue_print import user_blueprint


My_app = Flask(__name__, instance_relative_config=True)
My_app.register_blueprint(user_blueprint)
user_obj = Users()

#Geta all users
@My_app.route('/api/get-users', methods=['GET'])
def get_all_users():
    " A function to get all users"
    if user_obj.return_users():
        return jsonify(user_obj.return_users())
    else:
        return jsonify ({"Empty user list" : "Please add user"})


@My_app.route("/api/add-user", methods=['POST'])
def add_user():
    "A function to add a user"
    bol = True
    if request.data:
        user_details= request.json
        if user_obj.validate_user_obj(user_details):
            user_name = user_details['user_name']
            user_pasword = user_details['user_pasword']
            user_location = user_details['user_location']
            user_age = user_details['user_age']
            for user in user_obj.users_list:

                if user["user_name"] == user_name:
                    bol = False
                else :
                    bol = True

            if bol:
                user_obj.add_user(user_name, user_pasword, user_location, user_age)
                return jsonify(user_obj.users_list)
            else :
                message = {"ERROR": "user name already exists, please try another name"}
                return jsonify(message)

        else :
            return jsonify({"invalid user_object format": "Please Post a valid user object "})
    else :
        return jsonify({"Empty user object": "Please Post user details "})


@My_app.route("/api/delete/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    "A function to delete a user"
    message = {}
    del_user = {}
    for user in user_obj.users_list:
        if user["user_id"] == str(user_id):
           del_user = user

        else :
            message = {"Error": "User id dosent exist"}

    if del_user:
         user_obj.delete_user(del_user)
         return jsonify(user_obj.users_list)
    else:
         return jsonify(message)



if __name__ == '__main__':
    My_app.run(port=5000, debug=True)



