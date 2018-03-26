from random import randint, uniform
from time import sleep

def read_word_list_file(filename):
    wordlist = []
    with open(filename, "r") as filepointer:
        for line in filepointer.readlines():
            word = line.strip()
            if word=="": continue
            wordlist.append(word)
    return wordlist

def read_word_list_file(filename):
    wordlist = []
    with open(filename, "r") as filepointer:
        for line in filepointer.readlines():
            word = line.strip()
            if word=="": continue
            wordlist.append(word)
    return wordlist

def mathias():
	text = ""
	while continuer(text):
		text = input("Moi    : ")
		sleep(uniform(0.5,1.5))
		print("Toutou : " + repliques[randint(0,6)])

def mode1():
	return

#Renvoie une reponse plutot 
def reponseNulle():
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

