from random import randint, uniform
from time import sleep

def mathias():
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


def read_word_list_file(filename):
    wordlist = []
    with open(filename, "r") as filepointer:
        for line in filepointer.readlines():
            word = line.strip()
            if word=="": continue
            wordlist.append(word)
    return wordlist

#renvoie les mots & réponses contenues dans le fichier
def stockWordsAndQuestions(filename):
	dictThemes = {}
	key = ""
	theme = ""
	mots = []
	questions = []
	with open(filename, "r") as filepointer:
		for line in filepointer:
			line = line.strip()
			if line[0] in ['£','@']:
				key = line[0]
				if key == '£':
					if theme != "":
						mots.pop()
						questions.pop()
						dictThemes[theme] = (mots, questions)
					theme = line[1:]				
			elif(key == '£'):
				mots.append(line)
			elif(key == '@'):
				questions.append(line)
	return dictThemes

def mode1():
	print("mode 1")
	return

def mode2():
	print("mode 2")
	return

def mode3():
	print("mode 3")
	return

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


def reaction(dictThemes, theme, mot):

	rng = randint(0,len(dictThemes[theme][1])-1)
	message = dictThemes[theme][1][rng]
	print(message)

def testMathias():
	return
def testNathan():
	d = stockWordsAndQuestions("mode2")
	for theme,valeur in d.items():
		print(theme, " :")
		for mot in valeur[0]:
			print("mot :",mot)
		for question in valeur[1]:
			print("question :",question)
	return
def testBrian():
	return

if __name__=="__main__":
	mode = "-1"
	while(int(mode) != 4):
		while ((int(mode) < 0) or (int(mode) > 4)): 
			mode = input("Choisissez un mode entre 0, 1, 2 et 3 (4 pour quitter) ");
		if(int(mode) == 0):
			mathias();
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
