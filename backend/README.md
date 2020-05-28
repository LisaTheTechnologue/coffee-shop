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
        + barista : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im45b1UxYk5zQUViOXNUZF9XdnlzYiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3Atam9saXNhLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMTc2NDg2MDUzNDMzNjc5NDI0MiIsImF1ZCI6WyJjb2ZmZWVzaG9wIiwiaHR0cHM6Ly9jb2ZmZWVzaG9wLWpvbGlzYS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTkwNjI5MzQ1LCJleHAiOjE1OTA2MzY1NDUsImF6cCI6IkZrR2txT1Y1VUxPZXMyYmtST1Z3MVY2dWhaZ0p3WWd4Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MtZGV0YWlsIl19.wqCZDYMFelxIGK-NxyLCkQJQaFgo4TIOi_y4dKJ27Au22K2Uj5akwYH0RgH3cj329fI59Lc2gGNy2jKc2Km0ceonDXRfgiSQ2KufPQZnLEMsX1CK1t5Tv3C8TAEeCTNwbkXMHUOXl7FSzwdMKTyWFcnVpuulxMPPfxgg93lB2lRetQi3VOvpQrZ7fDhCtOg1RdUkqwRIBjxhvYYbBAqEZdwcprxVahwxcWVye138CkF8ttnNOc_CE9qeS5s7CtZg6eeIym47v5gJ5_5EEC7R0kbMVvg3_VwIRuRYxk_FpyQLHs8dpxWhP_zs9J-BxeuBx7yhPlOYhXzBtaSTAtrBFQ
        + manager : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im45b1UxYk5zQUViOXNUZF9XdnlzYiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3Atam9saXNhLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjA1NTEzMDYwNDYzODM0OTQwMSIsImF1ZCI6WyJjb2ZmZWVzaG9wIiwiaHR0cHM6Ly9jb2ZmZWVzaG9wLWpvbGlzYS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTkwNjI5NDYyLCJleHAiOjE1OTA2MzY2NjIsImF6cCI6IkZrR2txT1Y1VUxPZXMyYmtST1Z3MVY2dWhaZ0p3WWd4Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.35d3eyH2TBf7u6vvnbX-YAKZd8Ygbd3KR36aTix9EfzDt8XirPVHDYATPIYtA7Axmk08T6WAseua7kObE7Opzbz15Xo_kZiO19ZFpACDRmyonLMhRX0WabE4HWtnCC2ushaoYroj7ZZ3_KtblEuyK-wGkfLvJKBRrcNaAYuefD-XNQx-WSR37wQU4q5fDD6YAGXGZNFlJz2IGxosfhZQmva5UDx0sF7Gy3lkuAymp9FPwVb_LDjRX3Mc9wlp-lFZ2ddSDnurVcdXtO2N4kkI3blFGl5GOq8EFDqPtEe9Dx6oGxIhEnG2vsFGbz3DyuHwvus-BkcH09CqNTsikiVerw
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`


### Errors
#### update_drink() got multiple values for argument 'id'
Should be 2 args : jwt,id
#### Object of type type is not JSON serializable
If there is another error src.auth.auth.AuthError: ({'code': 'token_expired', 'description': 'Token expired.'}, 401)
Then there must be something wrong with your tokens (Expired or no permission)