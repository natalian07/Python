import mysql.connector

# Function to configure MySQL connection
def configure_connection():
    config = {
        "user": "your_username",
        "password": "your_password",
        "host": "your_host",         # Usually 'localhost' for local installations
        "database": "your_database"
    }
    return mysql.connector.connect(**config)

# Function to create the table (if it doesn't exist)
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS people (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT)")
        connection.commit()
    except mysql.connector.Error as error:
        print("Error creating table:", error)

# Function to insert data into the table
def insert_data(connection, name, age):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO people (name, age) VALUES (%s, %s)"
        values = (name, age)
        cursor.execute(sql, values)
        connection.commit()
        print("Data inserted successfully.")
    except mysql.connector.Error as error:
        print("Error inserting data:", error)

# Function to fetch and display data from the table
def fetch_and_display_data(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM people")
        data = cursor.fetchall()
        for row in data:
            print("ID:", row[0], "| Name:", row[1], "| Age:", row[2])
    except mysql.connector.Error as error:
        print("Error fetching data:", error)

# Main function to execute the program
def main():
    try:
        # Connect to the MySQL server
        connection = configure_connection()

        # Create a table (if it doesn't exist)
        create_table(connection)

        # Insert data into the table
        insert_data(connection, "John", 30)
        insert_data(connection, "Alice", 25)
        insert_data(connection, "Bob", 28)

        # Fetch and display data from the table
        fetch_and_display_data(connection)

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        # Close the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()