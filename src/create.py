from database.connection import execute_query
from pprint import pprint as pp

# ***************CREATE A CHARACTER************
def create_new_hero():
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s);
    """
    name_input = input('Enter superhero name: ')
    about_me_input = input('Enter details about superhero: ')
    origin_input = input('Enter superhero origin: ')

    execute_query(query, (name_input, about_me_input, origin_input))

# ***************CREATE ABILITY TYPE************

def create_new_hero_ability_type():
    query ="""
        INSERT INTO ability_types(name)
        VALUES (%s);
    """    
    powers_input = input('Enter superhero powers: ')

    execute_query(query, (powers_input,))

# ***************CREATE ABILITY LINK************

def create_new_hero_ability(): 
    query ="""
        INSERT INTO abilities(hero_id, ability_type_id)
        VALUES (hero_id_lookup, ability_types_id_lookup);
    """

    hero_id_lookup = execute_query("SELECT id FROM heroes WHERE name = name_input").fetchone()
    ability_types_id_lookup = execute_query("SELECT id FROM ability_types WHERE name = name_input").fetchone()

    execute_query(query, (hero_id_lookup[0], ability_types_id_lookup[0]))

# ***************ADD ABILITY************

def add_ability_to_hero():
    hero_name = input("What is the hero's name?: ")
    hero = execute_query("SELECT id FROM heroes where name = %s", (hero_name,)).fetchone()
    print('HERO ID IS: ', hero[0])

    ability_name = input("What is the ability's name?: ")
    ability = execute_query("SELECT id FROM ability_types where name = %s", (ability_name,)).fetchone()
    print('ABILITY ID IS: ', ability[0])

    execute_query("INSERT INTO abilities (hero_id, ability_type_id) VALUES (%s, %s)", (hero[0], ability[0]))    


# def test():
#         result = execute_query("SELECT id FROM ability_types WHERE name = 'Super Vision'").fetchone()
#         print(result[0])

# test()
