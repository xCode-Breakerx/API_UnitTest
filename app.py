from flask import Flask, request

from Database import db_test

base = db_test.db_test()

app = Flask(__name__)


@app.route('/users', methods=["GET"])
def users():
    try:
        return {"error": False, "users": base.fetchall()}
    except Exception as e:
        return {"error": True, "users": [], "msg": str(e)}


@app.route('/users/add', methods=["POST"])
def add_user():
    try:
        base.insert(request.json.get("name"), request.json.get("age"))
        return {"error": False}
    except Exception as e:
        return {"error": True, "msg": str(e)}


@app.route('/users/delete/<id>', methods=["DELETE"])
def delete_user(id):
    try:
        base.delete(id)
        return {"error": False}
    except Exception as e:
        return {"error": True, "msg": str(e)}


@app.route('/users/update', methods=["PUT"])
def update_user():
    try:
        return {"error": False, "success": base.update(request.json.get("id"), request.json.get("name"), request.json.get("age"))}
    except Exception as e:
        return {"error": True, "success": False, "msg": str(e)}


@app.route('/users/user', methods=["GET"])
def fetch_user():
    try:
        fetch = base.fetch(request.args.get("name"))
        return {"error": False, "found": len(fetch) > 0, "user": fetch}
    except Exception as e:
        return {"error": True, "found": False, "user": {}, "msg": str(e)}


if __name__ == '__main__':
    app.run(debug=True)
