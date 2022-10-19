from lecture3Segment2 import *


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return (
            self.src.getName()
            + "->"
            + self.dest.getName()
            + " ("
            + self.getWeight()
            + ")"
        )
