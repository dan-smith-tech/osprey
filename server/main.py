from flask import Flask, jsonify, request, send_from_directory
from list import add_item, delete_item, get_file, get_items, set_file

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
    new_item = request.json
    file_content = get_file()
    file_content = add_item(file_content, new_item)
    set_file(file_content)

    items = get_items()

    return jsonify({"items": items})


@app.route("/api/list", methods=["DELETE"])
def delete():
    print(request.json)
    item = request.json
    file_content = get_file()
    file_content = delete_item(file_content, item)
    set_file(file_content)

    items = get_items()

    return jsonify({"items": items})


if __name__ == "__main__":
    app.run()
