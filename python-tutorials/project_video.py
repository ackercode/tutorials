from flask import Flask, request
from microservices import service_flask

app = Flask(__name__)

@app.route("/<path:path>", methods=['GET', 'POST'])

def service(path):
    return service(request)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
