def guessgame(message, guess):
	if message.author not in guess:
		return ( "You didn't start guess")
	else:
		correct=guess[message.author][1]
		result = message.content.split()
		if result[1].isnumeric()==True:
			x=int(result[1])
			if x>0 and x<101:
				if guess[message.author][0]==5:
					guess.pop(message.author)
					if x==correct:
						return("You Won")
					else:
						return  (f"The correct answer was {correct}")
				else:
					if x>correct:
						return ("Go Down")
					if x<correct:
						return ("Go Up")
					if x==correct:
						guess.pop(message.author)
						return( "You Won")
			else:
				return ("NOT VALID")
		else:
			if result[1].lower()=="stop":
				guess.pop(message.author)
				return("Game Over")
			if result[1].lower()=="rules":
					return ("""
					·I'll think about a number between 1-100
·You have 5 guesses
					""")
			return("NOT VALID")


