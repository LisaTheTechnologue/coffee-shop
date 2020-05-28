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
        + barista : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im45b1UxYk5zQUViOXNUZF9XdnlzYiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3Atam9saXNhLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMTc2NDg2MDUzNDMzNjc5NDI0MiIsImF1ZCI6WyJjb2ZmZWVzaG9wIiwiaHR0cHM6Ly9jb2ZmZWVzaG9wLWpvbGlzYS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTkwNjQwNzEwLCJleHAiOjE1OTA2ODM5MTAsImF6cCI6IkZrR2txT1Y1VUxPZXMyYmtST1Z3MVY2dWhaZ0p3WWd4Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.1jAKWLJ4OZK-0ZKtlswNCErM5aXxVktbbvf35aBvYa2R0WnPRSp5jMgKH3tabrW5FJHlbgI0NDb4nxxoahs-Hmf8IqDz0ufE9Xg7t6yQhcj1iHG0UoLL4Fqk39h-YESXcg0JlE9jKXSL4s7jo26F6-A7sldjPGbnvAQZHXsJYen6tnmSGMvKyoZbyHOfs383mrN5IBx7bKrI1oZsCp-yhfxTyasu0WNG1Gjmp2rljg7_iCv4GCphrHPMBvNMD3u73WRrys8kmzogieP0PF_vVTN2oZTUpit-JNXaSbUVeM-Q9W-LNIZbBM5I-cGTRfLs-v4rT9-zyELcJ5W1PHJ2aA
        + manager : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im45b1UxYk5zQUViOXNUZF9XdnlzYiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3Atam9saXNhLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjA1NTEzMDYwNDYzODM0OTQwMSIsImF1ZCI6WyJjb2ZmZWVzaG9wIiwiaHR0cHM6Ly9jb2ZmZWVzaG9wLWpvbGlzYS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTkwNjg5OTEwLCJleHAiOjE1OTA3MzMxMTAsImF6cCI6IkZrR2txT1Y1VUxPZXMyYmtST1Z3MVY2dWhaZ0p3WWd4Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.T3UHdxsDXjKFVrS0T4pCcVkvef0dvY1gktIUsWhZ06wTQNu0CjJcggzSBvqX3w4Lyp0PH07NeLvrUrnDg4tvZmYdKgCgOoUqL2iADrncpqJrohg6LRK2KDNA8Dm8XjeO2IHjocfsXjJ4Mc99a9a8Kh958SVBV66sVG4ceCprsOLgXM4aNTD4Mxk2cRql6jlOfU9EkRtzywjdZ90u3G3WQj9eVb_8NtD5R7Mya9YZhHhFTXYanWUS6llUMcfAU1x94WnkeQjWn16nFx1vO8c2k2rgPyVSd-a2PGjPIeKOi3sdVVzOkuFPS_T_VIkSm_jXLY1tCBdoO0nhOWKb2Bayqw
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