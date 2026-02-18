from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps CI/CD Pipeline Running Successfully!"

if __name__ == "__main__":
    app.run(port=5000)
