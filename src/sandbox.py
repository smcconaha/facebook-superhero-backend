from database.connection import execute_query

def select_all():
    query = """
        SELECT *
        FROM heroes
        WHERE id = %s
    """
    id = input('What is the id?: ')
    list_of_heroes = execute_query(query, (id,)).fetchall()
    print(list_of_heroes[0])
    for record in list_of_heroes:
        print(record[1])
select_all()

