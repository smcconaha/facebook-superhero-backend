from database.connection import execute_query



def select_all():
    query = """
        SELECT h.name, h.about_me, h.biography, at.name
        FROM heroes h
        JOIN ability_types at
        ON (h.id = at.id)
        JOIN abilities a ON
        (at.id = a.id)
    """
    list_of_all = execute_query(query).fetchall()
    print(list_of_all)
    for record in list_of_all():
        print(record[1])
select_all()

def select_one():
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

