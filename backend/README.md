# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
set FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account : github  
2. Select a unique tenant domain : coffeeshop-jolisa.auth0.com
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
        + barista : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im45b1UxYk5zQUViOXNUZF9XdnlzYiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3Atam9saXNhLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWNlOTAyNDBmZDcyMjBjNjVkZTZjYjQiLCJhdWQiOiJjb2ZmZWVzaG9wIiwiaWF0IjoxNTkwNjA3NDU4LCJleHAiOjE1OTA2MTQ2NTgsImF6cCI6IkZrR2txT1Y1VUxPZXMyYmtST1Z3MVY2dWhaZ0p3WWd4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQiXX0.3rsLkU1kwa5PS9owJtQdweeHRrh2A_I4jXz3_56sM0U7UHA7gJAZzohiXgyPPuvlXPIeWPNQ9MQ2XrfBK7c0bWhS7BC1Joatfn5BK_QvJjHZr9aN5DLsLVlIdYc3IO1bMffyerCxc8V-EwM_ghXUQ-FWcBJY1D31dgZamuuFtf8ivOTpuRRPEkDYi1Lkrqy152zUj0lQnKBHcZvHT4-fvMHs7pdsY_oa4LTzPS3g1I5LSxwEBTihEN3c8z9-Q70Mj_0iyMPo1VfqF9X0kCHEQc8paW1RUxzQXkBhR7rShSqzwOkLdE1LJjuPZIsSyso7uLjqzYQUAvyvZYRN_zut6g
        + manager : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im45b1UxYk5zQUViOXNUZF9XdnlzYiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3Atam9saXNhLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWNlOTA5MDBmZDcyMjBjNjVkZTZlNzciLCJhdWQiOiJjb2ZmZWVzaG9wIiwiaWF0IjoxNTkwNjA3NjQ2LCJleHAiOjE1OTA2MTQ4NDYsImF6cCI6IkZrR2txT1Y1VUxPZXMyYmtST1Z3MVY2dWhaZ0p3WWd4Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGUiLCJnZXQiLCJwYXRjaCIsInBvc3QiXX0.De1mr0VO-MvkxVr4ECycKUaNxhaqNP2h85mV76ldOssVpI7dlzK6JXcVwF8XgMFR165NhNHESUFiImPcKqgINXWIcfvfZo_KSrABtnmFhegbHLy3bi8xoFLqfDJJTo_nbt-Trpb6L9EHAYi-0B9ny1q3q8sLoeE0x-8TlhbHwmfdhGNmzI27gtay4eK98pmcWxwgOJOpk-kLtxE7BwLCqfhlLtNJrqKA73WqCRcotcSQFA0YR7HgH-T5IGwuG6XHzY13-0RZ__b4L5Ed0wNfEqzpAfi0rxeRDSmEwvVTf_R9CTJS1ROPFY4yh2EDhjR4JrhIcO9V3l1kX9pjz4UOFA
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`
