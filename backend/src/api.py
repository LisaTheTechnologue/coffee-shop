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

db_drop_and_create_all()


# ROUTES
@app.route("/drinks")
def get_drinks():
    datas = Drink.query.all()
    drinks = [data.short() for data in datas]
    return jsonify({'success': True,
                    "drinks": drinks
                    }), 200


@app.route("/drinks-detail", methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(token):
    datas = Drink.query.all()
    drinks = [Drink.long(data) for data in datas]
    return jsonify({'success': True,
                    "drinks": drinks
                    }), 200


@app.route("/drinks", methods=['POST'])
@requires_auth('post:drinks')
def post_drinks(jwt):
    if request.data:
        body = request.get_json()
        new_title = body.get('title', None)
        new_recipes = body.get('recipe', None)
        drink = Drink(title=new_title, recipe=json.dumps(new_recipes))
        drink.insert()

        new_drink = Drink.query.filter_by(id=drink.id).first()
        return jsonify({'success': True,
                        "drinks": [new_drink.long()]
                        }), 200
    else:
        abort(422)


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(jwt, id):
    try:
        drink = Drink.query.filter(Drink.id == id).one_or_none()
        if not drink:
            abort(404)
        body = request.get_json()
        drink.title = body.get('title', drink.title)
        recipe = json.dumps(body.get('recipe'))
        drink.recipe = recipe if recipe != 'null' else drink.recipe
        drink.update()
        return jsonify({"success": True, "drinks": [drink.long()]}), 200
    except Exception:
        abort(404)


@app.route("/drinks/<int:id>", methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(jwt, id):
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


# Error Handling
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
def handle_auth_error(ex):
    """
    Receive the raised authorization error and propagates it as response
    """
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response