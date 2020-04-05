import psycopg2

# Establish the connection
connection = psycopg2.connect(database="pc", user="user", password="pass", host="localhost", port="5432")

# Instance of the connection
cursor = connection.cursor()

# Insert query
query = """INSERT INTO computers(hard_drive, processor, amount_of_ram, maximum_ram, hard_drive_capacity, form_factor)
            VALUES
            ('Samsung','Celeron','4GB','8GB','420GB','Standard-ATX');

"""

cursor.execute(query)
connection.commit()