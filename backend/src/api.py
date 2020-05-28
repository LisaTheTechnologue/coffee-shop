import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
db_drop_and_create_all()

## ROUTES
'''
@TODO DONE implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route("/drinks")
def get_drinks():
    datas = Drink.query.all()
    drinks = [data.short() for data in datas]
    return jsonify({'success': True,
                    "drinks": drinks
                    }), 200

'''
@TODO DONE implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route("/drinks-detail", methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(token):
    datas = Drink.query.all()
    drinks = [Drink.long(data) for data in datas]
    return jsonify({'success': True,
                    "drinks": drinks
                    }), 200

'''
@TODO DONE implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route("/drinks", methods=['POST'])
@requires_auth('post:drinks')
def post_drinks(jwt):
    if request.data:
        body = request.get_json()
        new_title = body.get('title', None)
        new_recipes = body.get('recipe', None)
        drink = Drink(title=new_title,recipe=json.dumps(new_recipes))
        drink.insert()

        new_drink = Drink.query.filter_by(id=drink.id).first()
        return jsonify({'success': True,
                        "drinks": [new_drink.long()]
                        }), 200
    else:
        abort(422)
'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(jwt,id):
    try:
        drink = Drink.query.filter(Drink.id == id).one_or_none() 
        if not drink : raise
        body = request.get_json()
        drink.title = body.get('title', drink.title)
        recipe = json.dumps(body.get('recipe'))
        drink.recipe = recipe if recipe != 'null' else drink.recipe
        drink.update()
        return  jsonify({"success": True, "drinks": [drink.long()]}), 200
    except AuthError:
        abort()
    except:
        if not drink: abort(404)
        abort(422)

'''
@TODO DONE implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route("/drinks/<int:id>", methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(jwt,id):
    try:
        drink = Drink.query.filter(Drink.id == id)\
                                .one_or_none()

        if drink is None:
            abort(404)
        
        drink.delete()

        return jsonify({'success': True,
                        "delete": id
                        }), 200
    except Exception:
        abort(404)
## Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
        }), 404

@app.errorhandler(AuthError)
def not_found(error):
    return jsonify({
        "success": False,
        "error": AuthError,
        "message": "resource not found"
        }), AuthError