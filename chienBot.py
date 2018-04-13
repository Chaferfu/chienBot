from random import randint, uniform
import random 
from time import sleep
import os

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
			line = line.strip()
			if line[0] in ['£','@']:
				key = line[0]
				if key == '£':
					theme = line[1:]
					dictThemes[theme] = ([], [])				
			elif(key == '£'):
	#			line = line.replace(' ', '')
				dictThemes[theme][0].append(line.split('|'))
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

			reponse = random.choice(smalltalk)
			while reponse == derniere:
				reponse = random.choice(smalltalk)

		else:
			reponse = reaction(dico, themeDetecte, motDetecte)
			while reponse == derniere:
				reponse = reaction(dico, themeDetecte, motDetecte)


		print("Nathanaelle Poilane : " + reponse)
		derniere = reponse

	return

def mode3():
	print("mode 3")
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
def findTheme(word, dico):
	for theme, valeur in dico.items():
		for w in valeur[0]:
			for variante in w:
				if variante != '' and (variante == word.replace(' ', '').lower()):
					# print("Le mot " + variante +" de la famille " + str(w) +" appartient au thème " + theme)

					return theme, w

	return "mot absent", []

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

def analyzeSentence(line, dico):
	nbOcc = {}
	wordsInTheme = {}
	theme = ""
	nothingfound = True

	for key in dico.keys():
		wordsInTheme[key] = []
		nbOcc[key] = 0
		# print(key)
	line = removePunctuation(line)
	words = line.split(' ')
	# print(words)
	for word in words:
		# print(word)
		#print("HEEEY")
		#print(findTheme(word, dico))
		theme, wordArray = findTheme(word, dico)
		if(theme != "mot absent"):
			# print("Theme trouv : " + theme)
			nbOcc[theme] += 1
			wordsInTheme[theme].append(wordArray)


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



#Cree une reponse de reaction quand le bot detecte un mot du dictionnaire
def reaction(dictThemes, theme, mot):

	reac = random.choice(dictThemes[theme][1])
	reac = reac.split('|')
	message = reac[0].strip()
	genre = reac[1].strip()
	reponse = ""
	if genre == 'ms':
		fill = mot[0]
	elif genre == 'fs':
		fill = mot[1]
	elif genre == 'mp':
		fill = mot[2]
	elif genre == 'fp':
		fill = mot[3]
	else:
		print("oula ca bug erreur genre reponse\n")
	message = message.split("*")

	#print(message)
#	message = message[0] + fill + message[1]
	for i in range(0,len(message)-1):
		reponse = reponse + message[i]
		reponse = reponse + fill
		#print("iteratio :" + str(i) + "reponse = " + reponse)

	reponse = reponse + message[-1]

	return reponse

def testMathias():
	dico = stock_Words_And_Questions("mode2")
	print(dico)

	print(analyzeSentence("Salut haha ouais ki lol", dico))
	return

def testNathan():
	while True :
		name = input("name pls :\n")
		if check_Connexion(name, "utilisateurs"):
			print("Oh content de te revoir ", name)
		else:
			print("Enchanté ", name)
			fichier = open(os.path.join("Users",name), "w")
			fichier.close()

def testBrian():
	d = stock_Words_And_Questions("mode2")
	k,w = analyzeSentence("J'aime les dauphins, un chien et la dépression.",d)
	r = reaction(d,k,w)
	print(r)
	return

if __name__=="__main__":
	mode = "-1"
	while(int(mode) != 4):
		while ((int(mode) < 0) or (int(mode) > 7)): 
			mode = input("Choisissez un mode entre 0, 1, 2 et 3 (4 pour quitter) ");
		if(int(mode) == 0):
			calou();
		elif(int(mode) == 1):
			mode1();
		elif(int(mode) == 2):
			mode2();
		elif(int(mode) == 3):
			mode3();
		elif(int(mode) == 4):
			testMathias();
		elif(int(mode) == 5):
			testNathan();
		elif(int(mode) == 6):
			testBrian();
		else:
			break;
		mode = "-1"
