# General Notes

## CREATE
INIT input message
    The league of Superheroes would like to welcome you as an entry level sidekick.  First, you will need to add a record for yourself, what is your name?:

    Tell us about you: 
    What is your origin story?:
    What are your superpowers?:

## VIEW / CREATE #2 / UPDATE / DELETE
Would you like to view (1), add a new superhero (2), update hero records (3), or delete a superhero (4)?: 
    IF (1) INPUT 1
        Would you like to view all (1) or view a specific superhero (2)
            (1)
                SHOW heroes: id, name, about_me, bio
                    ability types: name
            (2) 
                SQL select one character
    ELIF (2) INPUT 2
        What is the name of the superhero?
        What can you tell us about them?
        What is their origin story?
        What cool abilities do they have?
    ELIF (3) INPUT 3
        IF you would like to update hero name enter (1)
        IF you would like to update hero about me enter (2)
        IF you would like to update hero bio enter (3)
    <!-- ELIF (3) INPUT 3
        What is the id of the first superhero?
        What is the id of the second superhero?
            Did you want to see the update?
                Y/N -->
    ELIF (4) INPUT 4
        Enter the id of the deceased or disbanded superhero: 
            Delete all details for this record
    ELSE Message "Please enter a valid response
