from random import randint, uniform
from time import sleep

def mathias():
	motsCles = ["gamelle",'promener','promenade','chat','miaou']
	repliques = read_word_list_file("mode0")
	derniere = ""
	triggered = False

	text = ""
	while continuer(text):

		text = input("Moi   : ")
		jeDis = text.split(" ")

		nomPrononce = False

		for mot in jeDis:
			if mot == "Calou" or mot == "calou":
				nomPrononce = True

		for mot in jeDis:
			if mot in motsCles:
				triggered = True


		sleep(uniform(0.5,1.5))

		if nomPrononce:
			print("Calou : " + "Oui, c'est moi.")
		else:

			reponse = reponseNulle(repliques)
			while reponse == derniere:
				reponse = reponseNulle(repliques)

			if triggered:
				reponse = reponse.upper()

			print("Calou : " + reponse)
			derniere = reponse


def read_word_list_file(filename):
    wordlist = []
    with open(filename, "r") as filepointer:
        for line in filepointer.readlines():
            word = line.strip()
            if word=="": continue
            wordlist.append(word)
    return wordlist

#renvoie les mots & réponses contenue dans le fichier
def stockWordsAndQuestions(filename):
    dictThemes = {}
    theme 
    mots = []
    questions = []
    with open(filename, "r") as filepointer:
        for line in file.readlines():
            word = line.split(" ")
            while word[0] != '@':
                if word[0] == '£':
                    theme = word[0]
                else:
                    mots.append(word)
                line = file.readlines()
                word = line.split(" ")

            word = line.split(" ")
            while word[0] != '$':
                questions.append(word)
                line = file.readlines()
                word = line.split(" ")
def mode1():
	return

def continuer(text):
	if(text == "Au revoir !"):
		return False
	return True

#Renvoie une reponse plutot nulle et non constructive
def reponseNulle(tabMots):

	rng = randint(1,3)
	text = ""

	for i in range(rng):
		text += tabMots[randint(0,len(tabMots) - 1)]
		text += " "
	return text


if __name__=="__main__":
	mode = "-1"
	while ((int(mode) < 0) or (int(mode) > 3)): 
		mode = input("Entrez ");
	{
		0 : mathias(),
		1 : mode1(),
		2 : "Mode 2",
		3 : "Mode 3"
	}[int(mode)]
