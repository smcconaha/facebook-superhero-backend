def add_ability_to_hero():
    hero_name = input("What is the hero's name?: ")
    #name_input
    hero = execute_query("SELECT id FROM heroes where name = %s", (hero_name,)).fetchone()
    print('HERO ID IS: ', hero[0])

    ability_name = input("What is the ability's name?: ")
    ability = execute_query("SELECT id FROM ability_types where name = %s", (ability_name,)).fetchone()
    print('ABILITY ID IS: ', ability[0])

    execute_query("INSERT INTO abilities (hero_id, ability_type_id) VALUES (%s, %s)", (hero[0], ability[0]))
