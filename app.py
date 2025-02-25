from flask import Flask
from routes.robot_routes import robot_bp


app = Flask(__name__)
app.register_blueprint(robot_bp)

@app.route('/')
def home():
    return "Hello World!"

# @app.route('/login', methods=['POST'])
# def login():
#     user_id = 1  
#     token = generate_token(user_id)
#     return jsonify({"token": token})

# @app.route('/protected', methods=['GET'])
# @token_required
# def protected():
#     user_id = request.user_id  
#     return jsonify({"message": f"Hello, User {user_id}! This is a protected route."})

if __name__ == '__main__':
    app.run(port=5000, debug=True)