import os
import secrets
import psycopg2
import urllib.parse as urlparse


def generate_env():
    # Generate a unique secret key for each user
    secret_key = secrets.token_hex(16)

    # Generate a unique database name for each user
    database_name = f"user_{secrets.token_hex(8)}"

    # Return the generated values
    return {"SECRET_KEY": secret_key, "DATABASE_NAME": database_name}


def save_to_db(env_vars):
    database_uri = os.getenv('DATABASE_URI')

    # Parse the database URI
    result = urlparse(database_uri)
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname

    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname=database,
        user=username,
        password=password,
        host=hostname
    )
    # Create a cursor object
    cur = conn.cursor()

    # Check if the table exists, and if not, create it
    cur.execute("""
        CREATE TABLE IF NOT EXISTS env_vars (
            key VARCHAR(255),
            value VARCHAR(255)
        )
    """)

    # Insert the environment variables into the database
    for key, value in env_vars.items():
        cur.execute("INSERT INTO env_vars (key, value) VALUES (%s, %s)", (key, value))

    # Commit the changes and close the connection
    conn.commit()
    cur.close()
    conn.close()

# Generate environment variables and save them to the database
env_vars = generate_env()
save_to_db(env_vars)