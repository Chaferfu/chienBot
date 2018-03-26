from random import randint, uniform
from time import sleep


repliques = []
repliques.append("Waf!")
repliques.append("Wuf!")
repliques.append("Wef!")
repliques.append("Wif!")
repliques.append("Wof!")
repliques.append("Wouf!")
repliques.append("Wigrecf!")
  
while True:

	
	text = input("Moi    : ")
	sleep(uniform(0.5,1.5))
	print("Toutou : " + repliques[randint(0,6)])

#Renvoie une reponse plutot 
def reponseNulle():
	return