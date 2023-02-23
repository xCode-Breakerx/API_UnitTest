# API Unit test

This is a simple API with unit tests. The API connects to a
**local in-memory database** when it is started.
The API has 6 main endpoints.

Method

- GET
    - **/users** : returns all the users in the database
    - **/users/user** : query a specific user by name
        - params (query):
            - **name** : the name of user
- POST
    - **/users/add** : adds a new user
        - params (body):
            - **name** : the name of user
            - **age** : the age of the user
- PUT
    - **/users/update** : updates a given user by its id
        - params (body):
            - **id** : the id of the user to edit
            - **name** : the new name of user
            - **age** : the new age of the user
- DELETE
    - **/users/delete/<name>** : deletes a given user by its name
        - params:
            - **name** : the name of user

## Testing

Simply run the test file located in ``tests/unit/test_app.py``. Make sure
the API is running. The tests will fail if ran multiple times due to the default values
passed within the test cases (for example attempting to query a user that was deleted by
another test). Run the method ``test_w_last_all()`` to test everything at once which **should never fail**.