from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        return {"status": "ok", "service": "loan-api"}

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app
