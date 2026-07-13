import json
import os
import time
import chromadb

SESSION_FILE = "database/sessions.json"
MAX_AGE = 60 * 60 * 24   # 24 hours

client = chromadb.PersistentClient(path="database")


def load_sessions():
    # Create database folder if it doesn't exist
    os.makedirs("database", exist_ok=True)

    # Create sessions.json if it doesn't exist
    if not os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "w") as f:
            json.dump({}, f)

    # Read the file
    with open(SESSION_FILE, "r") as f:
        return json.load(f)
    
def save_sessions(data):

    with open(SESSION_FILE, "w") as f:
        json.dump(data, f)


def register_session(collection_name):

    sessions = load_sessions()

    sessions[collection_name] = time.time()

    save_sessions(sessions)


def cleanup_old_sessions():

    sessions = load_sessions()

    current = time.time()

    updated = {}

    for collection_name, created in sessions.items():

        if current - created > MAX_AGE:

            try:
                client.delete_collection(collection_name)
                print(f"Deleted {collection_name}")

            except Exception:
                pass

        else:
            updated[collection_name] = created

    save_sessions(updated)