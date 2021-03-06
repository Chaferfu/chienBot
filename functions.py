from random import randint, uniform
import random 
from time import sleep, time
import os
import pickle
import user

# Cherche si une entrée de l'utilisateur se refère à un thème connu
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

# Waf
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

def check_Coherence(answer,keyFileName, valueFileName = ""):
	tmp = ([], [])
	keys = read_word_list_file(keyFileName)
	if valueFileName != "":
		values = read_word_list_file(valueFileName)
	answer = removePunctuation(answer)

	for k in keys:
		if findStringInString(k, answer):
			tmp[0].append(k)
	if valueFileName != "":			
		for v in values:
			if findStringInString(v, answer):
					tmp[1].append(v)
	return tmp

# Au début du mode 3, cherche si l'utilisateur est déjà connu
def check_Connexion(name, filename):
	with open(filename, "r") as filepointer:
		for line in filepointer.readlines():
			if name == line.strip():
				return True

	with open(filename, 'a') as filepointer:
		filepointer.write(name + "\n")
	return False

# Récupère des informations relatives à l'humeur de l'utilisateur en fonction de ses réponses
def checkMood(answer, user):
	k, v = check_Coherence(answer, "Mood/joie")
	if k:
		user.changeMood(3)
	k, v = check_Coherence(answer, "Mood/tranquillite")
	if k:
		user.changeMood(1)
	k, v = check_Coherence(answer, "Mood/tristesse")
	if k:
		user.changeMood(-2)
	k, v = check_Coherence(answer, "Mood/colere")
	if k:
		user.changeMood(-3)
	k, v = check_Coherence(answer, "Mood/degout")
	if k:
		user.changeMood(-1)

# Permet de quitter le mode actuel si l'utilisateur dit "Au revoir !"
def continuer(text):
	if(text.lower().find("au revoir") == 0 or text.lower().find("bye") == 0 or text.lower().find("adieu") == 0):
		return False
	return True

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

# Renvoie True si la chaine word est dans la chaine phrase
def findStringInString(word, phrase):
	word = word.upper()
	phrase = phrase.upper()
	index = phrase.find(word)
	if index != -1 and (index == 0 or phrase[index-1].isspace()) and (index+len(word) == len(phrase) or phrase[index+len(word)].isspace()):
		return True
	else:
		return False

# Met en majuscule le contenu du fichier passe en parametre
def functionWriteFileUpper(filename):
	tmp = []
	with open(filename, "r") as filepointer:
		for line in filepointer.readlines():
			tmp.append(line.upper())
	with open(filename, "w") as filepointer:
		for t in tmp:
			filepointer.write(t.upper())

# Fonction principale du mode 3 : analyse la réponse de l'utilisateur et
# recupere le plus d'informations possible
def getInformationFromAnswer(answer, u):
	k,v = check_Coherence(answer, "keyRelation","valuesNames")
	u.addRelation(k,v)
	k,v = check_Coherence(answer, "keySports")
	u.addSport(k)
	checkMood(answer, u)
	with open("fichiersGouts", "r") as filepointer:
		for line in filepointer.readlines():
			line = line.split()
			k,v = check_Coherence(answer, "like", line[0])
			u.addLike(k,v)
			k,v = check_Coherence(answer, "dislike", line[0])
			u.addDislike(k,v)
	u.printInformationUser()

def jeSuis(line):
	line = removeQuantifiers(line)
	print(line)
	index = removePunctuation(removeQuantifiers(line.lower())).find("je suis ")
	if index  != -1:
		reponse = "Pourquoi es-tu "
		if line[index+8:index+12] == "plus":
			reponse += "plus " + line[index+12:len(line)].split()[0] + " ?"
		elif line[index+8:index+13] == "moins":
			reponse += "moins " + line[index+13:len(line)].split()[0] + " ?"
		else:
			reponse += line[index+8:len(line)].split()[0] + " ?"
		return "yes", reponse
	index = removePunctuation(removeQuantifiers(line.lower())).find("je serai ")
	if index != -1:
		reponse = "Pourquoi seras-tu "
		if line[index+9:index+13] == "plus":
			reponse += "plus " + line[index+13:len(line)].split()[0] + " ?"
		elif line[index+9:index+14] == "moins":
			reponse += "moins " + line[index+14:len(line)].split()[0] + " ?"
		else:
			reponse += line[index+9:len(line)].split()[0] + " ?"
		return "yes", reponse
	index = removePunctuation(removeQuantifiers(line.lower())).find("j'étais ")
	if index != -1:
		reponse = "Pourquoi étais-tu "
		if line[index+8:index+12] == "plus":
			reponse += "plus " + line[index+12:len(line)].split()[0] + " ?"
		elif line[index+8:index+13] == "moins":
			reponse += "moins " + line[index+13:len(line)].split()[0] + " ?"
		else:
			reponse += line[index+8:len(line)].split()[0] + " ?"
		return "yes", reponse
	index = removePunctuation(removeQuantifiers(line.lower())).find("je fus ")
	if index != -1:
		reponse = "Pourquoi fus-tu "
		if line[index+7:index+11] == "plus":
			reponse += "plus " + line[index+11:len(line)].split()[0] + " ?"
		elif line[index+7:index+12] == "moins":
			reponse += "moins " + line[index+12:len(line)].split()[0] + " ?"
		else:
			reponse += line[index+7:len(line)].split()[0] + " ?"
		return "yes", reponse
	index = removePunctuation(removeQuantifiers(line.lower())).find("j'ai été ")
	if index != -1:
		reponse = "Pourquoi as-tu été "
		if line[index+9:index+13] == "plus":
			reponse += "plus " + line[index+13:len(line)].split()[0] + " ?"
		elif line[index+9:index+14] == "moins":
			reponse += "moins " + line[index+14:len(line)].split()[0] + " ?"
		else:
			reponse += line[index+9:len(line)].split()[0] + " ?"
		return "yes", reponse
	index = removePunctuation(removeQuantifiers(line.lower())).find("j'avais été' ")
	if index != -1:
		reponse = "Pourquoi avais-tu été "
		if line[index+11:index+15] == "plus":
			reponse += "plus " + line[index+15:len(line)].split()[0] + " ?"
		elif line[index+11:index+16] == "moins":
			reponse += "moins " + line[index+16:len(line)].split()[0] + " ?"
		else:
			reponse += line[index+11:len(line)].split()[0] + " ?"
		return "yes", reponse
	return "no", ""

# Cree une reponse de reaction quand le bot detecte un mot du dictionnaire
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

# Lorsqu'un utilisateur se reconnecte, charge les donnees enregistrees lors
# de la derniere session
def readDataFromUser(user):
	with open('Users/' + user.infos[0], "rb") as u:
		unserialiazed_data = pickle.load(u)
		return unserialiazed_data

# Decoupe le texte d'un fichier en un tableau de mots
def read_word_list_file(filename):
    wordlist = []
    with open(filename, "r") as filepointer:
        for line in filepointer.readlines():
            word = line.strip()
            if word=="": continue
            wordlist.append(word)
    return wordlist

# Retire tous les elements de ponctuation d'une chaine de caracteres
def removePunctuation(line):
	line = line.replace(',', '')
	line = line.replace('.', '')
	line = line.replace('!', '')
	line = line.replace('?', '')
	line = line.replace(';', '')
	line = line.replace(':', '')

	return line

# Retire tous les quantifieurs d'une chaine de caracteres
def removeQuantifiers(line):
	words = read_word_list_file("quantifieurs")
	for w in words:
		line = line.replace(str(w), "")

	return line

# Renvoie une reponse plutot nulle et non constructive
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

# A la fin d'une session du mode 3, enregistre dans un fichier toutes les 
# informations collectees
def stockDataInUser(user):
	with open('Users/' + user.infos[0], "wb") as u:
		pickle.dump(user, u, protocol = pickle.HIGHEST_PROTOCOL)

# Renvoie les mots & réponses contenues dans le fichier
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
