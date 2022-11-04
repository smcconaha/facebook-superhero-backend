from database.connection import execute_query
from pprint import pprint as pp

def update_hero_name():
    hero_id = input("Enter the hero ID: ")
    hero_name = input("Enter the new hero name: ")
    query = """
        UPDATE heroes h
        SET name = hero_name
        WHERE h.id = %s;
    """    

    hero = execute_query("SELECT id FROM heroes where id = %s", (hero_id,)).fetchone()
    pp(hero[0])

update_hero_name()