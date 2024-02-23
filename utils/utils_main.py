import base64
import json
import requests
import psycopg2


def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config


def get_jwt_token():
    host = load_config()["host_env"]
    url = f"http://{host}:8023/oauth2/token"

    # Encode Credentials to get token:
    client_id = load_config()["client_id"]
    client_secret = load_config()["client_secret"]
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    # Set up POST request:
    data = {
        "grant_type": "client_credentials",
        # "client_id": "internal-ms",
        # "client_secret": "Nr4lsn5o",
        "scope": "communicate.read communicate.write"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_credentials}"
    }

    response = requests.post(url, data=data, headers=headers)
    access_token = json.loads(response.text)["access_token"]
    return access_token


def count_items_in_db(schema_with_table):
    config = load_config()
    connection = psycopg2.connect(dbname=config["db_name"], user=config["db_user"], password=config["db_password"],
                                  host=config["db_host"], port=config["db_port"])
    cur = connection.cursor()
    cur.execute(f"SELECT COUNT (*) FROM {schema_with_table}")
    count = cur.fetchone()[0]
    cur.close()
    connection.close()
    return count


def remove_items_in_db(schema_with_table, item_id):
    config = load_config()
    connection = psycopg2.connect(dbname=config["db_name"], user=config["db_user"], password=config["db_password"],
                                  host=config["db_host"], port=config["db_port"])
    cur = connection.cursor()
    cur.execute(f"DELETE FROM {schema_with_table} WHERE id = %s", (item_id,))
    connection.commit()
    cur.close()
    connection.close()
    return print(f"User {item_id} cleanup done")
