# scritp to turn baseball into Yahtzee

import random 
def baseball():	

	die_1 = ""
	die_2 = ""
	score_1 = ""
	score_2 = ""
	fouls = ""
	base_1 = ""
	base_2 = ""
	base_3 = ""
	strikes = ""
	outs = ""
	innings = ""
	score1 = ""
	score2 = ""

dictionary = {

"1,1" : "double ",
"1,2" : "single ",
"1,3" : "single ",
"1,4" : "single ",
"1,5" : "base on error ",
"1,6" : "base on balls ",
"2,2" : "strike ",
"2,3" : "strike ",
"2,4" : "strike ",
"2,5" : "strike ",
"2,6" : "foul out", 
"3,3" : "out at 1st",
"3,4" : "out at 1st",
"3,5" : "out at 1st",
"3,6" : "out at 1st",
"4,4" : "fly out",
"4,5" : "fly out",
"4,6" : "fly out",
"5,5" : "double play",
"5,6" : "triple",
"6,6" : "home run",

}

numbers = ['1,1','1,2','1,3','1,4','1,5','1,6','2,2','2,3','2,4','2,5','2,6','3,3','3,4','3,5','3,6','4,4','4,5','4,6','5,5','5,6','6,6']
r = random.choice(numbers)
print(r)
step = dictionary[r]
print(step)

"""
#test to determine dice rolls using random 
die_1 = random.randint(1,6)
die_2 = random.randint(1,6)
print(die_1)
print(die_2)
"""

if __name__ == "__main__":
    baseball()


    





