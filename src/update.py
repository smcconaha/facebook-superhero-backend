from database.connection import execute_query
from pprint import pprint as pp

def update_hero_name():
    hero_id = input("Enter the hero ID: ")
    hero_name = input("Enter the new hero name: ")
    query = """
        UPDATE heroes
        SET name = %s
        WHERE id = %s
    """    

    execute_query(query, (hero_name, hero_id))

def update_hero_about():
    hero_id = input("Enter the hero ID: ")
    hero_about = input("Enter the new hero 'about me': ")
    query = """
        UPDATE heroes
        SET about_me = %s
        WHERE id = %s
    """    

    execute_query(query, (hero_about, hero_id))

def update_hero_bio():
    hero_id = input("Enter the hero ID: ")
    hero_about = input("Enter the new hero bio: ")
    query = """
        UPDATE heroes
        SET biography = %s
        WHERE id = %s
    """    

    execute_query(query, (biography, hero_id))