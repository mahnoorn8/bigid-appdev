from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Placeholder data structure for storing passwords
passwords = []

# Placeholder for storing the BigID Token (for demonstration purposes)
bigid_token = "YOUR_BIGID_TOKEN_HERE"

# Function to validate the BigID Token
def validate_bigid_token(token):
    return token == bigid_token

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
            },
            {
                "description": "Synchronize",
                "params": [],
                "is_sync": True,
                "action_id": "synchronize"
            }
        ],
        "global_params": []
    }
    return jsonify(manifest)

@app.route('/execute', methods=['POST'])
def execute_action():
    token = request.headers.get("BigID-Token")
    if not validate_bigid_token(token):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    action_id = data.get("action_id")
    execution_id = data.get("execution_id")

    if action_id == "Sync":
        # Handle synchronization action
        response = {
            "status": "SUCCESS",
            "execution_id": execution_id,
            "progress": 1,
            "message": "Synchronization is complete."
        }
    elif action_id == "vault":
        # Handle vault action
        response = vault_action(data)
    elif action_id == "retrieve_passwords":
        response = retrieve_passwords(data)
    elif action_id == "synchronize":
        response = synchronize_action(data)
    else:
        response = {
            "status": "ERROR",
            "execution_id": execution_id,
            "progress": 0,
            "message": "Invalid action_id"
        }

    return jsonify(response)

def vault_action(data):
    # Placeholder logic for vault action
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
    return response

def retrieve_passwords(data):
    # Placeholder logic for retrieving passwords
    category_to_retrieve = data.get("category")
    retrieved_passwords = [p for p in passwords if p["category"] == category_to_retrieve]

    response = {
        "status": "Success",
        "passwords": retrieved_passwords
    }
    return response

def synchronize_action(data):
    # Placeholder logic for synchronization
    execution_id = data.get("execution_id")
    response = {
        "status": "In Progress",
        "execution_id": execution_id,
        "message": "Synchronization is in progress."
    }
    return response

if __name__ == '__main__':
    app.run(port=3000)
