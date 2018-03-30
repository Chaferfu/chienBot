from random import randint, uniform
from time import sleep

def mathias():
	repliques = []
	repliques = read_word_list_file("mode0")
	derniere = ""
	text = ""
	while continuer(text):

		text = input("Moi   : ")
		sleep(uniform(0.5,1.5))
		reponse = reponseNulle(repliques)
		while reponse == derniere:
			reponse = reponseNulle(repliques)


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

repliques = []
repliques.append("Waf!")
repliques.append("Wuf!")
repliques.append("Wef!")
repliques.append("Wif!")
repliques.append("Wof!")
repliques.append("Wouf!")
repliques.append("Wigrecf!")

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
