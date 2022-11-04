from database.connection import execute_query
from pprint import pprint as pp

def update_hero_name():
    hero_id = input("Enter the hero ID: ")
    hero_name = input("Enter the new hero name: ")
    query = """
        UPDATE heroes
        SET heroes.name = %s
        WHERE h.id = %s;
    """    

    execute_query(query, (hero_id, hero_name)).fetchone()