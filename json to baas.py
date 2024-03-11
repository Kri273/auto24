import sqlite3
import json

def json_to_sqlite(json_file, db_file, table_name):
    # Read JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create car table
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            url TEXT,
            brand TEXT,
            engine TEXT,
            mileage TEXT,
            fuel TEXT,
            model TEXT,
            model_short TEXT,
            transmission TEXT,
            year TEXT,
            bodytype TEXT,
            drive TEXT,
            price TEXT
        );
    """
    cursor.execute(create_table_query)

    # Insert car data into the table
    insert_data_query = f"""
        INSERT INTO {table_name} (
            url, brand, engine, mileage, fuel, model,
            model_short, transmission, year, bodytype, drive, price
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    for car in data:
        cursor.execute(insert_data_query, (
            car["url"], car["brand"], car["engine"], car["mileage"],
            car["fuel"], car["model"], car["model_short"], car["transmission"],
            car["year"], car["bodytype"], car["drive"], car["price"]
        ))

    # Commit changes and close connection
    conn.commit()
    conn.close()


# Example usage
json_file_path = 'autod.json'
db_file_path = 'output_autod.db'
table_name = 'autoddbfile'

json_to_sqlite(json_file_path, db_file_path, table_name)

    