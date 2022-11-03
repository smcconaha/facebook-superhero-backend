from database.connection import execute_query
from pprint import pprint as pp

from create import create_new_hero
from create import create_new_hero_ability
from create import create_new_hero_ability_type
from read import select_all
from read import select_one
from delete import another_one_bites_the_dust
from update import add_ability_to_hero

print('The league of Superheroes would like to welcome you as an entry level sidekick.  First, you will need to add a record for yourself')

# another_one_bites_the_dust()