import psycopg2

conn = psycopg2.connect(
    database="taskdb",
    user="docker",
    password="docker",
    host="database"
)
cursor = conn.cursor()


def input_function():
    """
    With this function, you can insert data to taskdb.
    Structure of taskdb DataBase you can find in Read.md documentation.
    """
    data_to_insert = None
    print("Example 'INSERT INTO example_table ( session_id, timestamp, talked_duration) "
          "VALUES ( %s, %s, %s);'")
    insert_query = input('Write query to like in example to insert data to table')

    done = False
    print("Example: 'session456', 8/12/2024, 120")

    while not done:
        data_to_insert = tuple(input('Provide data like in example please: '))
        done_check = input('Are you done with this function?(yes or no): ').lower()

        if done_check == 'yes':
            done = True
        elif done_check == 'no':
            pass
        else:
            raise ValueError(f'String {done} is neither "yes" nor "no"')

    cursor.execute(insert_query, data_to_insert)
    cursor.close()
    conn.close()

    return 'Data stored successfully'


def query_function():
    """
    With this function, you can have access, clear or remove data stored in taskdb with simple queries on SQL language
    Structure of taskdb DataBase you can find in Read.md documentation.
    :return: Selected data from DB
    """

    print("Example: 'SELECT * FROM example_table'")
    search_query = input("Hear you can write query specified for thi DB: ")

    cursor.execute(search_query)
    rows = cursor.fetchall()

    for row in rows:
        return row

    cursor.close()
    conn.close()


cursor.close()
conn.close()
