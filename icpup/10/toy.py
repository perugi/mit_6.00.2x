class Toy:
    def __init__(self):
        self._elems = []

    def add(self, new_elems):
        """new_elems is a list"""
        self._elems += new_elems
