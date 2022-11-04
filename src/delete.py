from database.connection import execute_query

# ***************DELETE ONE CHARACTER**************
def another_one_bites_the_dust():
    query = """
    DELETE FROM heroes h
    WHERE h.id = %s
    """

    id = input('Enter the superhero id that you would like to delete: ')
    execute_query(query,(id,))
    pp('Superhero deletion action completed')
