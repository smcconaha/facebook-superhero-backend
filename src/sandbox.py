from database.connection import execute_query

def create_new():
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (name_input, about_me_input, origin_input);
        INSERT INTO ability_types(name)
        VALUES (powers_input);
    """

    name_input = input('The league of Superheroes would like to welcome you as an entry level sidekick.  First, you will need to add a record for yourself, what is your name?: ')
    about_me_input = input('Tell us about you: ')
    origin_input = input('What is your origin story?: ')
    powers_input = input('What are your superpowers?: ')

    create_you = execute_query(query, (name_input, about_me_input, origin_input, powers_input)).commit()

create_new()

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

