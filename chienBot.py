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
    
    with open(filename, "r") as filepointer:
        for line in file.readlines():
        	theme
			mots = []
			questions = []
			while line != '@':
            	if line == '£':
                	line = file.readlines()
                    theme = line
                else:
                    mots.append(line)
                line = file.readlines()

            line = file.readlines()
            while line != '$':
                questions.append(line)
                line = file.readlines()
            dictThemes[theme] = (mots, questions)

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



if __name__=="__main__":
	d = stockWordsAndQuestions("mode2")
	for x in d:
		print (x)
		for y in d[x]
			print(y, ':', d[x][y])
			
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
		else:
			break;
		mode = "-1"
