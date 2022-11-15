import random


def noReplacementSimulation(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    """

    same_color = 0
    for trial in range(numTrials):
        bucket = ["red", "red", "red", "green", "green", "green"]
        random.shuffle(bucket)
        drawn = []
        for draw in range(3):
            drawn.append(bucket.pop())
        if all(el == drawn[0] for el in drawn):
            same_color += 1

    return float(same_color) / float(numTrials)


print(noReplacementSimulation(5000))
