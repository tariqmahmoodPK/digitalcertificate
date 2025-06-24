from flask import Flask, Response
import os

app = Flask(__name__)

@app.route('/')
def show_certificate():
    try:
        with open('digital-certificate.txt', 'r') as cert_file:
            content = cert_file.read()
        return Response(content, mimetype='text/plain')
    except FileNotFoundError:
        return "Certificate file not found.", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
