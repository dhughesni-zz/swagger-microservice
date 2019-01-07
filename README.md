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
6. Add docker builds for application in production/testing/swaggerMock versions
7. Deploy application via kubernetes?
8. Show process of updating the API

-	show we can test against the mock server
