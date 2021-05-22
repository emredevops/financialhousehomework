from flask import Flask

app = Flask(__name__)

@app.route('/home')
def index():
   return "Hello. This page created by Emre Oztoprak"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)