# swagger-microservice
Example python-flask API using swagger as the driver

- Using Swagger Version 2.0
-	Using the PetStore example

# Tasks to accomplish to prove out this workflow:

1. Show definition of API is configuration YMAL file in swagger v2
  - https://editor.swagger.io/
  - Reference in the repo: swagger-petstore.ymal
2. Demonstrate code generation for a specific server
  a. Go to Swagger editor: https://editor.swagger.io/
  b. "Generate Server" > “python-flask”
  c. Extract folder from .zip and move to "../swagger-microservice/" project repo
    ```
    dhughes@Daryls-MacBook-Pro:~$ cd Downloads/ && ls
    python-flask-server/               python-flask-server-generated.zip
    dhughes@Daryls-MacBook-Pro:~/Downloads$ cd python-flask-server/
    dhughes@Daryls-MacBook-Pro:~/Downloads/python-flask-server$ ls
    Dockerfile*            README.md*             git_push.sh*           requirements.txt*      setup.py*              swagger_server/        test-requirements.txt* tox.ini*
    dhughes@Daryls-MacBook-Pro:~/Downloads/python-flask-server$ mv * ~/Developer/swagger-microservice/
    ```
3. Add example functionality into generated code (in services folder)
4. Show API documentation
5. Show simple mock server
  ```
  (venv) dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice$ connexion run swagger_server/swagger/swagger.yaml --mock=all -v
  WARNING:connexion.operation:... OAuth2 token info URL missing. **IGNORING SECURITY REQUIREMENTS**
  WARNING:connexion.operation:... OAuth2 token info URL missing. **IGNORING SECURITY REQUIREMENTS**
  WARNING:connexion.operation:... OAuth2 token info URL missing. **IGNORING SECURITY REQUIREMENTS**
  WARNING:connexion.operation:... OAuth2 token info URL missing. **IGNORING SECURITY REQUIREMENTS**
  WARNING:connexion.operation:... OAuth2 token info URL missing. **IGNORING SECURITY REQUIREMENTS**
  WARNING:connexion.operation:... OAuth2 token info URL missing. **IGNORING SECURITY REQUIREMENTS**
  WARNING:connexion.operation:... OAuth2 token info URL missing. **IGNORING SECURITY REQUIREMENTS**
   * Serving Flask app "connexion.cli" (lazy loading)
   * Environment: production
     WARNING: Do not use the development server in a production environment.
     Use a production WSGI server instead.
   * Debug mode: off
  INFO:werkzeug: * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)


  ... In new terminal window
  dhughes@Daryls-MacBook-Pro:~/Downloads/python-flask-server$ curl http://petstore.swagger.io/v2/store/inventory
{"dd":4,"TestStatus":2,"placed":2,"unavailable":5,"available":3839,"pramod":1,"ut lab":1,"UNAVAILABLE":13,"Available":12,"eeeee":1,"Not available":3,"sold_by_pflb":1,"12":1,"test":1,"Invalid_status_XXX":4,"Nonavailable":1,"fff":2,"PramodYadav":1,"3.14":4,"active":10,"available and very cheap":1,"as":2,"reserved":4,"Valid":1,"{{status}}":1,"status":12,"string":148585,"pending":326,"available;pending;sold":1,"asdasd":1,"ava":1,"unknown":2,"Sold":15,"availablee":1,"not available":2,"free":1,"sold":109,"availabe":2,"available may be":1,"装逼中":1,"panding":2,"deserunt fugiat cons":1,"Taken":4,"irure aliquip veli":1,"AVAILABLE":34,"dolore":1,"availae":1,"s":1,"noavailable":2,"amet":1,"sold12":1,"availble":2,"Pending":9,"consectetur":1}
  ```
6. Add docker builds for application in production/testing/swaggerMock versions
7. Deploy application via kubernetes?
8. Show process of updating the API

# TESTING
- Pytest example:
```
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice$ pytest
=========================================================================================================================== test session starts ============================================================================================================================
platform darwin -- Python 3.7.2, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: /Users/dhughes/Developer/swagger-microservice, inifile:
collected 20 items

swagger_server/test/test_pet_controller.py ........                                                                                                                                                                                                                  [ 40%]
swagger_server/test/test_store_controller.py ....                                                                                                                                                                                                                    [ 60%]
swagger_server/test/test_user_controller.py ........                                                                                                                                                                                                                 [100%]

============================================================================================================================= warnings summary =============================================================================================================================
...
-- Docs: https://docs.pytest.org/en/latest/warnings.html
================================================================================================================== 20 passed, 7 warnings in 7.12 seconds ===================================================================================================================
(venv) dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice$
```
-	show we can test against the mock server



# Swagger Generated README:

# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/v2/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/v2/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```
