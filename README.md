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
  - services folder should contain files following the same convention as controllers: "<NAME> _ service.py"
  ```
  dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice$ mkdir swagger_server/services
  dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice$ touch swagger_server/services/__init__.py
  dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice$ touch swagger_server/services/pet_service.py
  dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice$ touch swagger_server/services/store_service.py
  dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice$ touch swagger_server/services/user_service.py
  ```
  - add example service function
  ```
  /swagger_server/controllers/pet_controller.py
  +from swagger_server.services.pet_service import *

  @@ -46,7 +48,7 @@ def find_pets_by_status(status):
  +    return service_find_pets_by_status(status)
  ```
  - add example unit test to pet_service
  ```
  dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice$ touch swagger_server/test/test_pet_service.py
  dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice/swagger_server/test$ pytest test_pet_service.py
  =========================================================================================================================== test session starts ============================================================================================================================
  platform darwin -- Python 3.7.2, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
  rootdir: /Users/dhughes/Developer/swagger-microservice, inifile:
  collected 3 items

  test_pet_service.py ...                                                                                                                                                                                                                                              [100%]

  ============================================================================================================================= warnings summary =============================================================================================================================
  ...
  =================================================================================================================== 3 passed, 6 warnings in 0.20 seconds ===================================================================================================================
  ```

4. Show API documentation
5. Show simple mock server
  ```
  (venv) dhughes@Daryls-MacBook-Pro:~/Developer/swagger-microservice$ connexion run swagger_server/swagger/swagger.yaml --mock=all --strict-validation --validate-responses -w flask -v
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

  -	show we can test against the mock server
  ... In new terminal window
  dhughes@Daryls-MacBook-Pro:~/Downloads/python-flask-server$ curl http://petstore.swagger.io/v2/store/inventory
{"dd":4,"TestStatus":2,"placed":2,"unavailable":5,"available":3839,"pramod":1,"ut lab":1,"UNAVAILABLE":13,"Available":12,"eeeee":1,"Not available":3,"sold_by_pflb":1,"12":1,"test":1,"Invalid_status_XXX":4,"Nonavailable":1,"fff":2,"PramodYadav":1,"3.14":4,"active":10,"available and very cheap":1,"as":2,"reserved":4,"Valid":1,"{{status}}":1,"status":12,"string":148585,"pending":326,"available;pending;sold":1,"asdasd":1,"ava":1,"unknown":2,"Sold":15,"availablee":1,"not available":2,"free":1,"sold":109,"availabe":2,"available may be":1,"装逼中":1,"panding":2,"deserunt fugiat cons":1,"Taken":4,"irure aliquip veli":1,"AVAILABLE":34,"dolore":1,"availae":1,"s":1,"noavailable":2,"amet":1,"sold12":1,"availble":2,"Pending":9,"consectetur":1}
  ```
6. Add docker builds for application in production/testing/swaggerMock versions
7. Deploy application via kubernetes?
8. Show process of updating the API

# TESTING

- UNIT:
    - YES: services(business logic functional testing)
    - MAYBE: controller-ping-checks(contract testing) ?
- API:
    - YES: Testing both service and controller together as they are implemented against mocked services config
- Integration: Running API Tests, implemented against externally mocked APIs with integration config
- Integrated: Running API Tests, implemented against live running APIs that are running against externally mocked APIs with integrated config
- e2e: Running the application against running system with mocked data

- Testing of 400,404? should we get them for free or have to write the tests - IN SWAGGER WE TRUST
---

# Take Aways:
- Project structure is a good thing to standardise
- Swagger is a nice tool for API development, handling all API structure ect. documentation
- The swagger codegen offered the ability to easily decouple the business logic from the API - it does result in "TURST IN SWAGGER"
- Testing was clean at a unit test level and API testing
- One dislike was that I was tied into using the swagger testing boilerplate which did not give me the ability to reuse the API tests for integration - we would be smarter her and write mocks, so that helper functions could be used to enable them to work for local API testing and then also against external mocks, for integration tests.

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
