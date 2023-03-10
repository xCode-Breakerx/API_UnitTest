from flask import Flask, request

from Database import db_test

base = db_test.db_test()

app = Flask(__name__)


@app.route('/users', methods=["GET"])
def users() -> dict:
    try:
        return {"error": False, "users": base.fetchall()}
    except Exception as e:
        return {"error": True, "users": [], "msg": str(e)}


@app.route('/users/add', methods=["POST"])
def add_user() -> dict:
    try:
        base.insert(request.json.get("name"), request.json.get("age"))
        return {"error": False}
    except Exception as e:
        return {"error": True, "msg": str(e)}


@app.route('/users/delete/<name>', methods=["DELETE"])
def delete_user(name: int) -> dict:
    try:
        base.delete(name)
        return {"error": False}
    except Exception as e:
        return {"error": True, "msg": str(e)}


@app.route('/users/update', methods=["PUT"])
def update_user() -> dict:
    try:
        return {"error": False, "success": base.update(request.json.get("id"), request.json.get("name"), request.json.get("age"))}
    except Exception as e:
        return {"error": True, "success": False, "msg": str(e)}


@app.route('/users/user', methods=["GET"])
def fetch_user() -> dict:
    try:
        fetch: dict = base.fetch(request.args.get("name"))
        return {"error": False, "found": len(fetch) > 0, "user": fetch}
    except Exception as e:
        return {"error": True, "found": False, "user": {}, "msg": str(e)}


if __name__ == '__main__':
    app.run(debug=True)
