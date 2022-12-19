def wordlegame(wordle, words, message):
	if message.author not in wordle:
		return ("Start Game")
	else:
		tries=wordle[message.author][0]
		
		word=wordle[message.author][1]
		lenght=len(word)
		what=message.content.split()[1].lower()
		
		if what=="stop":
			wordle.pop(message.author)
			return("Game Over")
		if what=="rules":
			return('''
·You have to guess a word of 4-7 letters
·after you make a guess you'll get hints about every letter
·a yellow letter means the word contains this letter
·a green letter means the word contains this letter and it is in the right place
·no color means the word doesn't contain this letter''')
		what = bytes(what, 'utf-8')
		if len(what)!=5:
			return(f"5 letters")
		if what not in words:
			return("It isn't a valid word")
		if tries==5:
			wordle.pop(message.author)
			if what==word:
				return("You Won")
			word=word.decode("utf-8")
			return (f"correct answer: {word}")
		mess=""
		if what==word:
			wordle.pop(message.author)
			return ("You Won")
						
		for i in range (lenght):
					
			if word[i]==what[i]:
				mess+=chr(what[i])
				mess+=" GREEN "
			elif what[i] in word:
				mess+=chr(what[i])
				mess+=" YELLOW "
			else:
				mess+=chr(what[i])
				mess+=" GREY "
		return (mess)
