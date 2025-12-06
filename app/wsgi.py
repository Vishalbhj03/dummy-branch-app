from app import create_app

app = create_app()

@app.route("/")
def root():
    return {"status": "ok", "service": "loan-api"}
