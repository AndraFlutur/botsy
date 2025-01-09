import discord
from random import *
import random
import os
from urllib.request import urlopen
from wordlegame import *
from guessgame import *
from xogame import *




global words
global guess
global wordle
global rps
global xoreq
global xo

guess={}
wordle={}
rps={}
xoreq=set()
xo={}
		

with urlopen("") as response:
	body = response.read()
	words = body.splitlines()

words=set(words)

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	
	if message.author==client.user:
		return
	if message.content.lower()==('$list'):
		games="""
		!guess
		!wordle"""
		print(discord.Interaction.is_expired)
		await message.channel.send(games)
	if message.content.split()[0].lower()=="!guess":
		if message.content.lower()=="!guess":
			
			guess[message.author]=[0, randint(1,100)]
			await message.channel.send("guess it")
		elif message.content.lower()=="!guess rules":
				await message.channel.send ("""
					·I'll think about a number between 1-100
·You have 6 guesses
					""")
		else: 
			
			
			await message.channel.send (guessgame(message, guess))
			if guessgame(message, guess)=="Go Up" or guessgame(message, guess)=="Go Down":
				guess[message.author][0]+=1
		
	
	if message.content.split()[0].lower()=="!wordle":
		if message.content.lower()=="!wordle":
			while True:
				word=(random.choice(list(words)))
				if len(word)==5 and word!="rules" and word!="stop":
					await message.channel.send(f"Use !wordle '5 letters word' to make a guess")
					break
			wordle[message.author]=[0, word]
		elif message.content.lower()=="!wordle rules":
			await message.channel.send('''
·You have to guess a word of 4-7 letters
·after you make a guess you'll get hints about every letter
·yellow means the word contains this letter
·green means the word contains this letter and it is in the right place
·grey means the word doesn't contain this letter
·You have number of letters+1 guesses''')
		else:
			
			x=wordlegame(wordle, words, message)
			await message.channel.send(x)
			if len(x)>26 and len(x)<100:
				wordle[message.author][0]+=1
				
	if message.content.split()[0].lower()=="!rps":
		if message.content.lower()=="!rps rules":
			await message.channel.send("""
·You have 3 choices (rock, papper, scissors)
·You will play against the bot that have the same 3 options
·rock>scissors
·scissors>paper
·paper>rock""")
		elif message.content.lower()=="!rps":
			p = await message.channel.send("Play")
			rps[p]=[random.choice(["rock", "paper", "scissors"]), message.author]
			await p.add_reaction("🪨")
			await p.add_reaction("📝")
			await p.add_reaction("✂")
	if message.content.split()[0].lower()=="!xo":
		if message.content.lower()=="!xo rules":
			await message.channel.send('''
·to start a game use command !xo
·the first player to react 👍 is your opponent
·the player who reacts starts the game
·To place a x/o use command "!xo <number of the line> <number of the column>"
''')
		elif message.content.lower()=="!xo":
			if message.author not in xo:
				await message.add_reaction("👍")
				xoreq.add(message.author)
				print(xoreq)
			else:
				await message.channel.send("You are already in a game, if you want to stop it use command '!xo stop'")
		elif message.content.lower()=="!xo stop":
			if message.author in xo:
				await message.channel.send(f"We canceled the game between {message.author} and {xo[message.author][0]}")
				xo.pop(xo[message.author][0])
				xo.pop(message.author)
				print(xo)

			else:
				await message.channel.send("You did't start any game")
		else:
			if len(message.content.split())>2 and message.author in xo:
				if message.content.split()[1].isnumeric()==True and message.content.split()[2].isnumeric()==True:
					if int(message.content.split()[1])>0 and int(message.content.split()[1])<4 and  int(message.content.split()[2])>0 and int(message.content.split()[2])<4:
						await message.channel.send(xogame(message, xo))
				if message.author in xo:
					if xo[message.author][4]==9:
						await message.channel.send(f"Draw between {message.author} and {xo[message.author][0]}")
						xo.pop(xo[message.author][0])
						xo.pop(message.author)
						


@client.event
async def on_reaction_add(reaction, user):
	reacted = reaction.message
	
	if reacted in rps:
		if rps[reacted][1]==user:
			print(rps[reacted][0])
			if (reaction.emoji=="🪨" and rps[reacted][0]== "paper") or (reaction.emoji== "📝" and rps[reacted][0]=="scissors")  or (reaction.emoji== "✂" and rps[reacted][0]=="rock"):
				await reacted.channel.send(f"You lost {user.name}")
			elif (reaction.emoji=="🪨" and rps[reacted][0]== "scissors") or (reaction.emoji== "📝" and rps[reacted][0]=="rock")  or (reaction.emoji== "✂" and rps[reacted][0]=="paper"):
				await reacted.channel.send(f"You Won {user.name}")
			else:
				await reacted.channel.send(f"🤝 {user.name}")

			rps.pop(reacted)
	if reacted.author in xoreq and reacted.content.lower()=="!xo" and reaction.emoji=="👍" and reacted.author not in xo and user not in xo and user!=client.user and user!=reacted.author:
		table = [["#", "#", "#"],["#", "#", "#"],["#", "#", "#"]]
		xo[reacted.author]=[user, table, False, "O", 0]
		xo[user]=[reacted.author, table, True, "X", 0]
		xoreq.remove(reacted.author)
		if user in xoreq:
			xoreq.remove(user)
		await reacted.channel.send(f"""
·{user.name} you start
·{user.name} is X
·{reacted.author} is O
# # #
# # #
# # #""")
		print(xo)


			




		
		
	



client.run(TOKEN)





