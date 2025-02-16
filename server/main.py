from flask import Flask, jsonify, request, send_from_directory
from list import add_item, delete_item, get_items

app = Flask(__name__)


# Serve static files automatically via Flask's default /static/<path>
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/list", methods=["GET"])
def get():
    items = get_items()
    return jsonify({"items": items})


@app.route("/api/list/add", methods=["POST"])
def add():
    new_item = request.json["item"]
    items = add_item(new_item)
    return jsonify({"items": items})


@app.route("/api/list/delete", methods=["POST"])
def delete():
    item_id = request.json["id"]
    items = delete_item(item_id)
    return jsonify({"items": items})


if __name__ == "__main__":
    app.run()
