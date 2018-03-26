from random import randint, uniform
from time import sleep

#Renvoie une reponse plutot nulle et non constructive
def reponseNulle(tabMots):

	rng = randint(1,2)
	text = ""

	for i in range(rng):
		text += tabMots[randint(0,len(tabMots) - 1)]

	return text

repliques = []
repliques.append("Waf! ")
repliques.append("Wuf! ")
repliques.append("Wef! ")
repliques.append("Wif! ")
repliques.append("Wof! ")
repliques.append("Wouf! ")
repliques.append("Wigrecf! ")
  
while True:

	
	text = input("Moi    : ")
	sleep(uniform(0.5,1.5))
	print("Toutou : " + reponseNulle(repliques))

