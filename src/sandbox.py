from database.connection import execute_query
from pprint import pprint as ppshasta

print('The league of Superheroes would like to welcome you as an entry level sidekick.  First, you will need to add a record for yourself')

# ***************CREATE A CHARACTER************
def create_new_hero():
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s);
    """
    query2 ="""
        INSERT INTO ability_types(name)
        VALUES (%s);
    """    
    name_input = input('Enter superhero name: ')
    about_me_input = input('Enter details about superhero: ')
    origin_input = input('Enter superhero origin: ')
    powers_input = input('Enter superhero powers: ')

    execute_query(query, (name_input, about_me_input, origin_input))
    execute_query(query2, (powers_input,))

# create_new_hero()

# ***************SHOW ALL CHARACTERS**************
def select_all():
    query = """
        SELECT h.id, h.name, h.about_me, h.biography, STRING_AGG(abtype.name,',') as abilities
                FROM heroes h
                JOIN abilities abs
                ON (h.id = abs.hero_id)
                JOIN ability_types abtype ON
                (abs.ability_type_id = abtype.id)
                GROUP BY h.id
    """
    list_of_all = execute_query(query).fetchall()
    ppshasta(list_of_all)
select_all()

# ***************SHOW ONE CHARACTERS**************
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

