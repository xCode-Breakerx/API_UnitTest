# API Unit test

This is a simple API with unit tests. The API connects to a
**local sqlite3 in-memory database** when it is started.
The API has 6 main endpoints.

Tested with python 3.10.5
<pre>
>>> sys.version
'3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]'
</pre>

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
    - **/users/delete/&lt;name&gt;** : deletes a given user by its name
        - params:
            - **name** : the name of user

## Testing

Simply run the test file located in ``tests/unit/test_app.py``. Make sure
the API is running. The tests will fail if ran multiple times due to the default values
passed within the test cases (for example attempting to query a user that was deleted by
another test). Run the method ``test_w_last_all()`` to test everything at once which **should never fail**.