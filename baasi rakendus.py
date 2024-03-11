import sqlite3

def search_cars(criteria):
    # Connect to SQLite database
    conn = sqlite3.connect('output_autod.db')
    cursor = conn.cursor()

    # Construct SQL query based on criteria
    query = f"SELECT * FROM autoddbfile WHERE {criteria};"
    cursor.execute(query)

    # Fetch results
    cars = cursor.fetchall()

    # Close connection
    conn.close()

    return cars

def main():
    print("Otsige autosid kriteeriumide alusel:")
    brand = input("Bränd: ")
    brand = brand.lower()
    model = input("Mudel: ")
    model = model.lower()
    fuel = input("Kütuse tüüp: ")
    fuel = fuel.lower()
    year = input("Aasta: ")
    price = input("Max hind: ")

    # Construct criteria for the SQL query
    criteria_list = []
    if brand:
        criteria_list.append(f"LOWER(brand) = '{brand}'")
    if model:
        criteria_list.append(f"LOWER(model) = '{model}'")
    if fuel:
        criteria_list.append(f"LOWER(fuel) = '{fuel}'")
    if year:
        criteria_list.append(f"year = '{year}'")
    if price:
        criteria_list.append(f"price <= {price}")

    # Join the criteria with 'AND' for the SQL query
    criteria = " AND ".join(criteria_list)

    # Perform the search
    result = search_cars(criteria)

    # Display results
    if result:
        print("\nMatching cars:")
        for car in result:
            print(car)
        print(f"\nTotal number of matching cars: {len(result)}")
    else:
        print("\nNo cars found matching the criteria.")

if __name__ == "__main__":
    main()
