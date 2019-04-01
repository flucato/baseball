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

dictionary = {

"1, 1" : "double - 2",
"1, 2" : "single - 1",
"1, 3" : "single - 1",
"1, 4" : "single -1",
"1, 5" : "base on error - 1",
"1, 6" : "base on balls -1",
"2, 2" : "strike - 1",
"2, 3" : "strike - 1",
"2, 4" : "strike - 1",
"2, 5" : "strike - 1",
"2, 6" : "foul out", 
"3, 3" : "out at 1st",
"3, 4" : "out at 1st",
"3, 5" : "out at 1st",
"3, 6" : "out at 1st",
"4, 4" : "fly out",
"4, 5" : "fly out",
"4, 6" : "fly out",
"5, 5" : "double play",
"5, 6" : "triple",
"6, 6" : "home run",

}

numbers = [11,12,13,14,15,16,22,23,24,25,26,33,34,35,36,44,45,46,55,56,66]

r = random.choice(numbers)
print(r)

dic = 



"""
die_1 = random.randint(1,6)
die_2 = random.randint(1,6)
print(die_1)
print(die_2)
"""








if __name__ == "__main__":
    baseball()


    





