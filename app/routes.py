from flask import Blueprint, request, jsonify, current_app

main = Blueprint('main', __name__)

@main.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask!"})


@main.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not all([name, email, message]):
        return jsonify({"success": False, "error": "Missing fields"}), 400

    try:
        conn = current_app.get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )
        conn.commit()
        cur.close()
        return jsonify({"success": True, "message": "Message stored successfully"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
