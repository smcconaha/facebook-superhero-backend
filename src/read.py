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
                ORDER BY h.id;
    """
    list_of_all = execute_query(query).fetchall()
    pp(list_of_all)

# select_all()

# ***************SHOW ONE CHARACTERS**************
def select_one():
    query = """
        SELECT h.id, h.name, h.about_me, h.biography, STRING_AGG(abtype.name,',') as abilities
            FROM heroes h
            JOIN abilities abs
            ON (h.id = abs.hero_id)
            JOIN ability_types abtype ON
            (abs.ability_type_id = abtype.id)
            WHERE h.id = %s
            GROUP BY h.id;
    """
    id = input('Enter the superhero ID that you would like to search: ')
    list_of_heroes = execute_query(query, (id,)).fetchall()
    print(list_of_heroes[0])
    for record in list_of_heroes:
        print(record[1])

# select_one()
