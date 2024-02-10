from flask import Flask, jsonify, request
import time  # Import the time module

app = Flask(__name__)

# Placeholder data structure for storing passwords
passwords = []

@app.route('/manifest', methods=['GET'])
def get_manifest():
    manifest = {
        "app_name": "Training App",
        "description": "Test App",
        "vendor": "BigID",
        "category": "utility",
        "license_type": "FREE",
        "actions": [
            {
                "description": "test",
                "params": [],
                "is_sync": True,
                "action_id": "Sync"
            },
            {
                "description": "Password Manager",
                "params": [],
                "is_sync": True,
                "action_id": "vault"
            },
            {
                "description": "Retrieve Passwords",
                "params": ["category"],
                "is_sync": True,
                "action_id": "retrieve_passwords"
            }
        ],
        "global_params": []
    }
    return jsonify(manifest)

@app.route('/vault', methods=['POST'])
def password_manager():
    data = request.get_json()

    # Assuming the data contains website, username, password, and category
    website = data.get("website")
    username = data.get("username")
    password = data.get("password")
    category = data.get("category")

     # Placeholder logic: simulate a longer process by sleeping for 5 seconds
    time.sleep(5)

    # Placeholder logic: store the password in the passwords list
    passwords.append({"website": website, "username": username, "password": password, "category": category})

    response = {
        "status": "In Progress",  # Change status to "In Progress"
        "message": "Password storage is in progress."
    }
    return jsonify(response)

@app.route('/retrieve_passwords', methods=['POST'])
def retrieve_passwords():
    data = request.get_json()

    # Assuming the data contains the category for retrieval
    category_to_retrieve = data.get("category")

    # Placeholder logic: retrieve passwords based on the specified category
    retrieved_passwords = [p for p in passwords if p["category"] == category_to_retrieve]

    response = {
        "status": "Success",
        "passwords": retrieved_passwords
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=3000)
