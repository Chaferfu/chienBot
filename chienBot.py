from functions import *
from user import *
import sys
from random import randint, uniform
import random 
from time import sleep
import os
import pickle
import user
# import ipdb

def stockDataInUser(user):
	with open('Users/' + user.infos[0], "wb") as u:
		pickle.dump(user, u, protocol = pickle.HIGHEST_PROTOCOL)


def readDataFromUser(user):
	with open('Users/' + user.infos[0], "rb") as u:
		unserialiazed_data = pickle.load(u)
		return unserialiazed_data

def calou():
	motsCles = ["gamelle",'promener','promenade','chat','miaou']
	repliques = read_word_list_file("mode0")
	repliquesRares = read_word_list_file("mode1")
	derniere = ""
	triggered = False

	text = ""
	while continuer(text):

		text = input("Moi   : ")
		jeDis = text.split(" ")

		isNomPrononce = False

		for mot in jeDis:
			if mot == "Calou" or mot == "calou":
				isNomPrononce = True

		for mot in jeDis:
			if mot in motsCles:
				triggered = True


		sleep(uniform(0.5,1.5))

		if isNomPrononce:
			print("Calou : " + "Oui, c'est moi.")
		else:
			reponse = reponseNulle(repliques, repliquesRares)
			while reponse == derniere:
				reponse = reponseNulle(repliques, repliquesRares)

			if triggered:
				reponse = reponse.upper()

		print("Calou : " + reponse)
		derniere = reponse
	return

def check_Connexion(name, filename):
	with open(filename, "r") as filepointer:
		for line in filepointer.readlines():
			if name == line.strip():
				return True

	with open(filename, 'a') as filepointer:
		filepointer.write(name + "\n")
	return False

def read_word_list_file(filename):
    wordlist = []
    with open(filename, "r") as filepointer:
        for line in filepointer.readlines():
            word = line.strip()
            if word=="": continue
            wordlist.append(word)
    return wordlist

#renvoie les mots & réponses contenues dans le fichier
def stock_Words_And_Questions(filename):

	dictThemes = {}
	key = ""
	theme = ""
	with open(filename, "r") as filepointer:
		for line in filepointer:
			if line[0] != '#':
				line = line.strip()
				if line[0] in ['£','@']:
					key = line[0]
					if key == '£':
						theme = line[1:]
						dictThemes[theme] = ([], [])				
				elif(key == '£'):
					#line = line.replace(' ', '')
					dictThemes[theme][0].append(line.lower().split('|'))
				elif(key == '@'):
					dictThemes[theme][1].append(line)
	return dictThemes

def mode1():
	calou()
	return

def mode2():

	smalltalk = read_word_list_file("mode2_hmmm")
	dico = stock_Words_And_Questions("mode2")
	derniere = ""

	text = ""
	while continuer(text):

		text = input("Moi                 : ")

		themeDetecte, motDetecte = analyzeSentence(text, dico)

		sleep(uniform(0.5,1.5))

		if themeDetecte == "no":
			jeSuisDetecte, reponse = jeSuis(text)			
			if jeSuisDetecte == "no":
				reponse = random.choice(smalltalk)
				while reponse == derniere:
					reponse = random.choice(smalltalk)

		else:
			reponse = reaction(dico, themeDetecte, motDetecte)
			while reponse == derniere:
				print("DEBUG : meme message, je reconstruis une nouvelle reaction")
				reponse = reaction(dico, themeDetecte, motDetecte)


		print("Nathanaelle Poilane : " + reponse)
		derniere = reponse


def mode3():
	name = input("name pls :\n")
	u = User(name)
	if check_Connexion(name, "utilisateurs"):
		print("Oh content de te revoir ", name)
		u = readDataFromUser(u)
	else:
		print("Enchanté ", name)
	text = ""
	while continuer(text):
		temps = time()
		text = input("Moi                 : ")
		reponse = ""
		getInformationFromAnswer(text, u)
		print("Nathanaelle Poilane : " + reponse)
	stockDataInUser(u)
	tmp = readDataFromUser(u)
	tmp.printInformationUser()
	return

# Permet de quitter le mode actuel si l'utilisateur dit "Au revoir !"
def continuer(text):
	if(text == "Au revoir !"):
		return False
	return True

#Renvoie une reponse plutot nulle et non constructive
def reponseNulle(tabMots, tabMotsrares):
	rng = randint(1,3)
	text = ""
	for i in range(rng):
		
		if uniform(0,1) < 0.9:
			text += tabMots[randint(0,len(tabMots) - 1)]
			text += " "

		else:
			text += tabMotsrares[randint(0,len(tabMotsrares) - 1)]
			text += " "

	return text

# Cherche si un mot rentre par l'utilisateur figure dans le dictionnaire et 
# retourne le thème associé, ou "mot absent" si le mot n'est pas dans le 
# dictionnaire
def findThemes(line, dico):

	nbOcc = {}
	wordsInTheme = {}

	for key in dico.keys():
		wordsInTheme[key] = []
		nbOcc[key] = 0
		# print(key)

	#print("line is : " + line)

	for theme, valeur in dico.items():
		for w in valeur[0]:
			for variante in w:
				#print(" is " + variante + " in line ? : ")
				#if variante != '' and variante.strip() in line.lower(): #cette ligne marchait avant ais nathan est iperialiste il veut quo tilise sa fonction partout
				# if variante.strip() == "chien":
				# 	print("is chien in " + line + "? : " + str(findStringInString(variante.strip(),line)))
				if findStringInString(variante, line):
					#print("yes")
					# print("Le mot " + variante +" de la famille " + str(w) +" appartient au thème " + theme)
					
					hypothese = variante.strip().split(' ')
					tokens = line.lower().strip().split(' ')

					for tok in tokens:
						#print ("tok : " + tok + " \t hypo : " + hypothese[0])
						if tok == hypothese[0]:
							nbOcc[theme] += 1
							wordsInTheme[theme].append(w)
						
					
	return nbOcc, wordsInTheme


def analyzeSentence(line, dico):
	
	theme = ""
	nothingfound = True

	
	line = removePunctuation(line)
	#words = line.split(' ')
	# print(words)
	
		# print(word)
		#print("HEEEY")
		#print(findTheme(word, dico))
	nbOcc, wordsInTheme = findThemes(line, dico)

	bestOcc = max([ nbOcc[k] for k in nbOcc])
	for k, v in nbOcc.items():
		# print("#################")
		# print(bestOcc)
		# print(k, v)
		if 0<v :
			nothingfound = False

	if nothingfound:
		return "no", []

	for k in nbOcc.keys():
		if nbOcc[k] == bestOcc:
			return k, random.choice(wordsInTheme[k])


	#should be dead code from here
	print("ca bug :(")

def removePunctuation(line):
	line = line.replace(',', '')
	line = line.replace('.', '')
	line = line.replace('!', '')
	line = line.replace('?', '')
	line = line.replace(';', '')
	line = line.replace(':', '')

	return line

# Li
# def analyzeSentence(line, dico):
# 	nbOcc = {}
# 	wordsInTheme = {}
# 	theme = ""
# 	genre = ""
# 	for key in dico.keys():
# 		wordsInTheme[key] = []
# 		nbOcc[key] = 0
# 		print(key)
# 	line = removePunctuation(line)
# 	words = line.split(' ')
# 	print(words)
# 	for word in words:
# 		print(word)
# 		#print("HEEEY")
# 		#print(findTheme(word, dico))
# 		theme, wordArray = findTheme(word, dico)
# 		if(theme != "mot absent"):
# 			print("Theme trouv : " + theme)
# 			nbOcc[theme] += 1
# 			wordsInTheme[theme].append(wordArray)


# 	bestOcc = max([ nbOcc[k] for k in nbOcc])
# 	for k, v in nbOcc.items():
# 		print("#################")
# 		print(k, v)

# 	for k in nbOcc.keys():
# 		if nbOcc[k] == bestOcc:
# 			return k, random.choice(wordsInTheme[k]),genre

def remplacer(message, remplacement, mot):
	# ipdb.set_trace()

	if ',' in remplacement:
			determinant = remplacement.split(' ')[0].strip()
			# print("DEBUG   determinant : " + str(determinant))
			determinant = determinant.split(',')


			print("DEBUG    determinant : " + str(determinant))
			# print(str(remplacement))

			fill = remplacement.split(' ')[1].strip()

			print("DEBUG    fill : " + fill)

			if "ms" in fill:
				if '¤' not in mot[0]:
					message = message.replace("*", determinant[0] + " " + mot[0].strip(), 1)
				else:
					message = message.replace("*", determinant[1] + " " + mot[1].strip(), 1)
			elif "fs" in fill:
				if '¤' not in mot[1]:
					message = message.replace("*", determinant[1] + " " + mot[1].strip(), 1)
				else:
					message = message.replace("*", determinant[0] + " " + mot[0].strip(), 1)
			elif "mp" in fill:
				if '¤' not in mot[2]:
					message = message.replace("*", determinant[0] + " " + mot[2].strip(), 1)
				else:
					message = message.replace("*", determinant[1] + " " + mot[3].strip(), 1)
			elif "fp" in fill:
				if '¤' not in mot[3]:
					message = message.replace("*", determinant[1] + " " + mot[3].strip(), 1)
				else:
					message = message.replace("*", determinant[0] + " " + mot[2].strip(), 1)
			else:
				print("#######ERREUR certainement dans le fichier mode2 ici")


	else:
			if "ms" in remplacement:
				if '¤' not in mot[0]:
					message = message.replace("*", mot[0].strip(), 1)
				else:
					message = message.replace("*", mot[1].strip(), 1)
			elif "fs" in remplacement:
				if '¤' not in mot[1]:
					message = message.replace("*", mot[1].strip(), 1)
				else:
					message = message.replace("*", mot[0].strip(), 1)
			elif "mp" in remplacement:
				if '¤' not in mot[2]:
					message = message.replace("*", mot[2].strip(), 1)
				else:
					message = message.replace("*", mot[3].strip(), 1)
			elif "fp" in remplacement:
				if '¤' not in mot[3]:
					message = message.replace("*", mot[3].strip(), 1)
				else:
					message = message.replace("*", mot[2].strip(), 1)
			else:
				print("#######ERREUR certainement dans le fichier mode2 la")
	return message






#Cree une reponse de reaction quand le bot detecte un mot du dictionnaire
def reaction(dictThemes, theme, mot):


	reac = random.choice(dictThemes[theme][1])
	reac = reac.split('|')
	message = reac[0].strip()
	fills = reac[1:]

	# print("DEBUG : reaction choisie : " + message)
	# print("DEBUG : fills : " + str(fills))

	while '*' in message and 0 < len(fills):
		message = remplacer(message, fills[0], mot)
		fills.pop(0)

	#message = message.split("*")

	#print(message)
	#message = message[0] + fill + message[1]
	# for i in range(0,len(message)-1):
	# 	reponse = reponse + message[i]
	# 	reponse = reponse + fill.strip()
		#print("iteratio :" + str(i) + "reponse = " + reponse)

	#reponse = reponse + message[-1]



	return message

def check_Coherence(answer,keyFileName, valueFileName = ""):
	keys = read_word_list_file(keyFileName)
	if valueFileName != "":
		values = read_word_list_file(valueFileName)
	answer = removePunctuation(answer)

	for k in keys:
		if findStringInString(k, answer):
			if valueFileName != "":			
				for v in values:
					if findStringInString(v, answer):
						return (k,v)
			return (k,'')
	return ('','')

def findStringInString(word, phrase):
	word = word.upper().strip()
	phrase = phrase.upper()
	index = phrase.find(word)
	if index != -1 and (index == 0 or phrase[index-1].isspace()) and (index+len(word) == len(phrase) or phrase[index+len(word)].isspace()):
		return True
	else:
		return False

def testMathias():
	dico = stock_Words_And_Questions("mode2")
	print(dico)
	print(analyzeSentence("Salut haha ouais ki lol", dico))
	return

def testNathan():
	u = User("Nathanaelle")
	getInformationFromAnswer("frère germain", u)
	print(u.findSomeone("germain"))
	stockDataInUser(u)
	u2 = readDataFromUser(u)

	# while True :
	# 	name = input("name pls :\n")
	# 	if check_Connexion(name, "utilisateurs"):
	# 		user1 = user.User(name)
	# 		user1.famille['soeur'] = "Hombeline"
	# 		print("Oh content de te revoir ", name)
	# 		stockDataInUser(user1)
	# 		tmp = readDataFromUser(user1)
	# 		print(tmp.infos[0])
	# 		print(tmp.famille)
	# 	else:
	# 		print("Enchanté ", name)
	# 		fichier = open(os.path.join("Users",name), "a")

	# 		fichier.close()

def testBrian():
	jeSuis("Je suis sale putain de merde.")

if __name__=="__main__":
	mode = int(sys.argv[1])
	print(mode)

	while(mode != 4):
		while (mode < 0 or mode > 7): 
			mode = int(input("Choisissez un mode entre 0, 1, 2 et 3 (4 pour quitter) "));
		if(mode == 0):
			calou();
		elif(mode == 1):
			mode1();
		elif(mode == 2):
			mode2();
		elif(mode == 3):
			mode3();
		elif(mode == 4):
			testMathias();
		elif(mode == 5):
			testNathan();
		elif(mode == 6):
			testBrian();
		else:
			break;
		mode = -1
