from flask import Flask
from routes.robot_routes import robot_bp

app = Flask(__name__)
app.register_blueprint(robot_bp)

@app.route('/')
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)