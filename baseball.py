"""
title: baseball.py.

description:
author:
date:
url:
notes:

"""
# scritp to turn baseball into Yahtzee

from random import choice


def baseball():
    """Baseball.

    description: yahtzee into baseball via python.
    arguments:
    returns:

    """
    """
    die_1 = ""
    DIE_2 = ""
    SCORE_1 = ""
    SCORE_2 = ""
    FOULS = ""
    BASE_1 = ""
    BASE_2 = ""
    BASE_3 = ""
    STRIKES = ""
    OUTS = ""
    INNINGS = ""
    SCORE1 = ""
    SCORE2 = ""

    """

    DICTIONARY = {
        "1,1": "double ",
        "1,2": "single ",
        "1,3": "single ",
        "1,4": "single ",
        "1,5": "base on error ",
        "1,6": "base on balls ",
        "2,2": "strike ",
        "2,3": "strike ",
        "2,4": "strike ",
        "2,5": "strike ",
        "2,6": "foul out",
        "3,3": "out at 1st",
        "3,4": "out at 1st",
        "3,5": "out at 1st",
        "3,6": "out at 1st",
        "4,4": "fly out",
        "4,5": "fly out",
        "4,6": "fly out",
        "5,5": "double play",
        "5,6": "triple",
        "6,6": "home run"
    }

    NUMBERS = [
        '1,1',
        '1,2',
        '1,3',
        '1,4',
        '1,5',
        '1,6',
        '2,2',
        '2,3',
        '2,4',
        '2,5',
        '2,6',
        '3,3',
        '3,4',
        '3,5',
        '3,6',
        '4,4',
        '4,5',
        '4,6',
        '5,5',
        '5,6',
        '6,6']

    RAN = choice(NUMBERS)
    print(RAN)
    STEP = DICTIONARY[RAN]
    print(STEP)


if __name__ == "__main__":
    baseball()
