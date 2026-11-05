# Worksheet 1.5: Person class

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)


from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self,name,birth):

        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if name == "":
            raise ValueError("Name cannot be an empty string")
        
        if not isinstance(birth, date):
            raise TypeError("Birth must be a date object")
            
        self.name = name
        self.birth = birth

    def initials(self):
        parts = self.name.split()
        return "".join([part[0].upper() for part in parts])

    def is_birthday(self):
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day
