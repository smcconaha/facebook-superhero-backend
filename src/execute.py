from database.connection import execute_query
from pprint import pprint as pp

from create import create_new_hero, create_new_hero_ability, create_new_hero_ability_type, add_ability_to_hero
from read import select_all, select_one
from update import update_hero_name, update_hero_about, update_hero_bio
from delete import another_one_bites_the_dust

print('\n The league of Superheroes would like to welcome you as an entry level sidekick.  First, you will need to add a record for yourself.\n  NOTICE: Responses are continuously monitored and subject to auditing')

create_new_hero()
create_new_hero_ability_type()

# Directory Function
print("Great job sidekick, keep up the good work and you may just become a real superhero!")

def directory_mess():
    print('----Actions----\n Enter the number of your selection \n(1) View the superhero roster\n(2) Add a new superhero\n(3) Update superhero records\n(4) Delete a superhero')

def init():
    directory_mess()
    directory = input('Enter Number Selection From Directory: ')
    if directory == '1':
        view_type = input('Enter (1) to view all or enter (2) to view a specific superhero record: ')
        if view_type == '1':
            select_all()
        elif view_type == '2':
            select_one()
        else:
             print('Please make a valid selection: ')
    elif directory == '2':
        create_new_hero()
        create_new_hero_ability_type()
    elif directory == '3':
        update_type = input('----Update Actions----\n Enter the number of your selection \n(1) Update superhero name \n(2) Update superhero "about me" \n(3) Update superhero bio\nEnter Selection: ')
        if update_type == '1':
            update_hero_name()      
        elif update_type == '2':
            update_hero_about()
        elif update_type == '3':
            update_hero_bio()
        else:
             print('Please make a valid selection: ')                   
    elif directory == '4':
        another_one_bites_the_dust()
    else:
        print('Please make a valid selection')
    init()

init()