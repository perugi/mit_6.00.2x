class Person():
    
    def __init__(self, name):
        """Assumes name is a string. Create a person."""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            