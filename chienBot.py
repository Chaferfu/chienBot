from random import randint, uniform
from time import sleep

def mathias():
	repliques = []
	repliques = read_word_list_file("mode0")
	while True:

		text = input("Moi   : ")
		sleep(uniform(0.5,1.5))
		print("Calou : " + reponseNulle(repliques))

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
            while word[0] != '@'
                if word[0] == '£'
                    theme = word[0]
                else
                    mots.append(word)
                line = file.readlines()
                word = line.split(" ")

            word = line.split(" ")
            while word[0] != '$'
                questions.append(word)
                line = file.readlines()
                word = line.split(" ")

#Renvoie une reponse plutot nulle et non constructive
def reponseNulle(tabMots):

	rng = randint(1,3)
	text = ""

	for i in range(rng):
		text += tabMots[randint(0,len(tabMots) - 1)]

	return text


if __name__=="__main__":
	mode = "-1"
	while ((int(mode) < 0) or (int(mode) > 3)): 
		mode = input();
	{
		0 : mathias(),
		1 : "Mode 1",
		2 : "Mode 2",
		3 : "Mode 3"
	}[int(mode)]



