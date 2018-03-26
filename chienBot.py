from random import randint, uniform
from time import sleep

def mathias():
	repliques = []
	repliques.append("Waf! ")
	repliques.append("Wuf! ")
	repliques.append("Wef! ")
	repliques.append("Wif! ")
	repliques.append("Wof! ")
	repliques.append("Wouf! ")
	repliques.append("Wigrecf! ")
	while True:

		text = input("Moi   : ")
		sleep(uniform(0.5,1.5))
		print("Calou : " + repliques[randint(0,6)])

def read_word_list_file(filename):
    wordlist = []
    with open(filename, "r") as filepointer:
        for line in filepointer.readlines():
            word = line.strip()
            if word=="": continue
            wordlist.append(word)
    return wordlist

#Renvoie une reponse plutot nulle et non constructive
def reponseNulle(tabMots):

	rng = randint(1,2)
	text = ""

	for i in range(rng):
		text += tabMots[randint(0,len(tabMots) - 1)]

	return text


  
while True:

	
	text = input("Moi    : ")
	sleep(uniform(0.5,1.5))
	print("Toutou : " + reponseNulle(repliques))





if __name__=="__main__":
	mode = "-1"
	while ((int(mode) < 0) or (int(mode) > 3)): 
		mode = input();
	{
		0 : "Mode 0",
		1 : "Mode 1",
		2 : "Mode 2",
		3 : "Mode 3"
	}[int(mode)]



