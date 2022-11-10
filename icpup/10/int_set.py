class Int_set:
    """An Int_set is a set of integers"""

    def __init__(self):
        """Create an empty set of integers"""
        self._vals = []

    def insert(self, v):
        """Assumes v is an integer and inserts e into self"""
        if v not in self._vals:
            self._vals.append(v)

    def member(self, v):
        """Assumes v is an integer
        Returns True if v is in self, False otherwise"""
        return v in self._vals

    def remove(self, v):
        """Assumes v is an integer and removes e from self"""
        try:
            self._vals.remove(v)
        except:
            raise ValueError(f"{v} not found")

    def get_members(self):
        """Returns a list containing the elements of self._vals
        Nothing can be assumed about the order of the elements"""
        return self._vals[:]

    def union(self, other):
        """other is an Inte_set
        mutates self so that it contains exactly the elements in self
        plus the elements in other."""

        for v in other.get_members():
            self.insert(v)

    def __add__(self, other):
        """Returns a new set which is a union between the two operands"""
        new_set = Int_set()
        new_set.union(self)
        new_set.union(other)
        return new_set

    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return "{}"
        self._vals.sort()
        result = ""
        for e in self._vals:
            result += str(e) + ", "
        return f"{{{result[:-2]}}}"


s = Int_set()
s.insert(3)
s.insert(4)
print(f"The value of s is {s}")

o = Int_set()
o.insert(3)
o.insert(5)

n = s + o
print(f"The value of n is {n}")
