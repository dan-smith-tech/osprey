from flask import Flask, jsonify, request, send_from_directory
from list import add_items, delete_items, get_file, get_items, set_file

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
    items, tags = get_items()
    return jsonify({"items": items, "tags": tags})


@app.route("/api/list", methods=["POST"])
def add():
    items_to_add = request.json["itemsToAdd"]
    items_to_remove = request.json["itemsToRemove"]
    file_content = get_file()
    add_items(file_content, items_to_add)
    delete_items(file_content, items_to_remove)
    set_file(file_content)

    items = get_items()

    return jsonify({"items": items})


if __name__ == "__main__":
    app.run()
