from random import randint, uniform
import random 
from time import sleep, time
import os
import pickle
import user

#Renvoie une réplique en utilisant l'algorithme du mode 2
def repliqueMode2(text,dico,smalltalk):

	themeDetecte, motDetecte = analyzeSentence(text, dico)
	if themeDetecte == "no":
		jeSuisDetecte, reponse = jeSuis(text)			
		if jeSuisDetecte == "no":
			reponse = random.choice(smalltalk)

	else:
		reponse = reaction(dico, themeDetecte, motDetecte)
	return reponse

# Remplace les symboles '*' dans le message selectionne en utilisant le mot choisi
# et en acordant correctement les mots et les determinants les précédant 
def remplacer(message, remplacement, mot):
	if ',' in remplacement:
			determinant = remplacement.split(' ')[0].strip()
			# print("DEBUG   determinant : " + str(determinant))
			determinant = determinant.split(',')

			fill = remplacement.split(' ')[1].strip()

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

# Cherche si une entrée de l'utilisateur se refère à un thème connu
def analyzeSentence(line, dico):
	
	theme = ""
	nothingfound = True

	
	line = removePunctuation(line)
	nbOcc, wordsInTheme = findThemes(line, dico)

	bestOcc = max([ nbOcc[k] for k in nbOcc])
	for k, v in nbOcc.items():
		if 0<v :
			nothingfound = False

	if nothingfound:
		return "no", []

	for k in nbOcc.keys():
		if nbOcc[k] == bestOcc:
			return k, random.choice(wordsInTheme[k])

	#should be dead code from here
	print("ca bug :(")
	
# Bot utilisé dans le mode 1
# Calou dit des phrases construites aléatoirement à base d'aboiements
# propose aussi d'autres fonctionnalites listees dans le rapport
def calou():
	motsCles = ["gamelle",'promener','promenade','chat','miaou']
	repliques = read_word_list_file("FichiersAnalyse/mode0")
	repliquesRares = read_word_list_file("FichiersAnalyse/mode1")
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

# cherche dans un ou deux fichiers s'il y a une cohérence dans la réponse de l'utilisateur
# en comparant avec les mostd es fichiers, renvoi deux listes de mots. 
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

# Au début du mode 3, cherche si l'utilisateur est déjà connu.
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
def findThemes(line, dico):

	nbOcc = {}
	wordsInTheme = {}

	for key in dico.keys():
		wordsInTheme[key] = []
		nbOcc[key] = 0

	for theme, valeur in dico.items():
		for w in valeur[0]:
			for variante in w:
				if findStringInString(variante, line):				
					hypothese = variante.strip().split(' ')
					tokens = line.lower().strip().split(' ')
					for tok in tokens:
						if tok == hypothese[0]:
							nbOcc[theme] += 1
							wordsInTheme[theme].append(w)
						
					
	return nbOcc, wordsInTheme

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
	k,v = check_Coherence(answer, "FichiersAnalyse/keyRelation","FichiersAnalyse/valuesNames")
	u.addRelation(k,v)
	k,v = check_Coherence(answer, "FichiersAnalyse/keySports")
	u.addSport(k)
	checkMood(answer, u)
	with open("FichiersAnalyse/fichiersGouts", "r") as filepointer:
		for line in filepointer.readlines():
			line = line.split()
			k,v = check_Coherence(answer, "FichiersAnalyse/like", "FichiersAnalyse/" + line[0])
			u.addLike(k,v)
			k,v = check_Coherence(answer, "FichiersAnalyse/dislike",  "FichiersAnalyse/" + line[0])
			u.addDislike(k,v)

def jeSuis(line):
	line = removeQuantifiers(line)
	print(line)
	index = removePunctuation(removeQuantifiers(line.lower())).find("je suis ")
	if index  != -1:
		reponse = "Pourquoi es-tu " + line[index+8:len(line)].split()[0] + " ?"
		return "yes", reponse
	index = removePunctuation(removeQuantifiers(line.lower())).find("je serai ")
	if index != -1:
		reponse = "Pourquoi seras-tu " + line[index+8:len(line)].split()[0] + " ?"
		return "yes", reponse
	index = removePunctuation(removeQuantifiers(line.lower())).find("j'étais ")
	if index != -1:
		reponse = "Pourquoi étais-tu " + line[index+8:len(line)].split()[0] + " ?"
		return "yes", reponse
	index = removePunctuation(removeQuantifiers(line.lower())).find("je fus ")
	if index != -1:
		reponse = "Pourquoi fus-tu " + line[index+8:len(line)].split()[0] + " ?"
		return "yes", reponse
	index = removePunctuation(removeQuantifiers(line.lower())).find("j'ai été ")
	if index != -1:
		reponse = "Pourquoi as-tu été " + line[index+8:len(line)].split()[0] + " ?"
		return "yes", reponse
	index = removePunctuation(removeQuantifiers(line.lower())).find("j'avais été' ")
	if index != -1:
		reponse = "Pourquoi avais-tu été " + line[index+8:len(line)].split()[0] + " ?"
		return "yes", reponse
	return "no", ""



#Cree une reponse de reaction quand le bot detecte un mot du dictionnaire
def reaction(dictThemes, theme, mot):


	reac = random.choice(dictThemes[theme][1])
	reac = reac.split('|')
	message = reac[0].strip()
	fills = reac[1:]
	while '*' in message and 0 < len(fills):
		message = remplacer(message, fills[0], mot)
		fills.pop(0)
	return message

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

# Retire tous les elements de pnctuation d'une chaine de caracteres
def removePunctuation(line):
	line = line.replace(',', '')
	line = line.replace('.', '')
	line = line.replace('!', '')
	line = line.replace('?', '')
	line = line.replace(';', '')
	line = line.replace(':', '')

	return line

def removeQuantifiers(line):
	words = read_word_list_file("FichiersAnalyse/quantifieurs")
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
				dictThemes[theme][0].append(line.split('|'))
			elif(key == '@'):
				dictThemes[theme][1].append(line)
	return dictThemes

# renvoi une phrase aléatoire du fichier filename en remplacant des éléments de la phrase par d'autres expressions
# pour personnaliser la réponse.
def getRandomPhraseFrom(filename, wordToChange, expressionToChange, wordToChange2 = None, expressionToChange2 = None):
	phrase = []
	with open(filename, "r") as filepointer:
		for line in filepointer:
			line = line.strip()
			phrase.append(line)
	finalPhrase = random.choice(phrase)
	finalPhrase = finalPhrase.replace(expressionToChange, wordToChange)
	if expressionToChange2 != None:
		finalPhrase = finalPhrase.replace(expressionToChange2, wordToChange2)
	return finalPhrase
