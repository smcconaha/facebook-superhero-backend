from database.connection import execute_query
from pprint import pprint as pp

from create import create_new_hero
from create import create_new_hero_ability
from create import create_new_hero_ability_type
from read import select_all
from read import select_one
from delete import another_one_bites_the_dust
from update import add_ability_to_hero

print('The league of Superheroes would like to welcome you as an entry level sidekick.  First, you will need to add a record for yourself.\n  NOTICE: Responses are continuously monitored and subject to auditing')

# create_new_hero()
# create_new_hero_ability_type()

# Directory Function
print("Great job sidekick, keep up the good work and you may just become a real superhero!")

def directory():
    print('----Actions----\n Enter the number of your selection \n(1) View the superhero roster\n(2) Add a new superhero\n(3) Update friends and enemies\n(4) Delete a superhero')

directory()

def init():
    directory = input('Enter Number Selection From Directory: ')
    if directory == '1':
        print('You clicked one')
    elif directory == '2':
        print('You clicked two')
    elif directory == '3':
        print('You clicked three')        
    elif directory == '4':
        print('You clicked four')
    else:
        print('Please make a valid selection')

init()
# another_one_bites_the_dust()