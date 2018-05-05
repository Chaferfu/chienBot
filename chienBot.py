
from functions import *
from user import *
import sys

def mode1():
	calou()
	return

def mode2():

	smalltalk = read_word_list_file("FichiersAnalyse/mode2_hmmm")
	dico = stock_Words_And_Questions("FichiersAnalyse/mode2")
	derniere = ""
	text = ""
	while continuer(text):

		text = input("Moi                 : ")

		themeDetecte, motDetecte = analyzeSentence(text, dico)

		sleep(uniform(0.5,1.5))

		if themeDetecte == "no":
			jeSuisDetecte, reponse = jeSuis(text)			
			if jeSuisDetecte == "no":
				reponse = random.choice(smalltalk)
				while reponse == derniere:
					reponse = random.choice(smalltalk)

		else:
			reponse = reaction(dico, themeDetecte, motDetecte)
			while reponse == derniere:
				print("DEBUG : meme message, je reconstruis une nouvelle reaction")
				reponse = reaction(dico, themeDetecte, motDetecte)


		print("Nathanaelle Poilane : " + reponse)
		derniere = reponse


def mode3():
	smalltalk = read_word_list_file("FichiersAnalyse/mode2_hmmm")
	dico = stock_Words_And_Questions("FichiersAnalyse/mode2")

	name = input("Entrez votre nom s'il vous plait :\n")
	u = User(name)
	if check_Connexion(name, "utilisateurs"):
		print("Oh content de te revoir", name)
		u = readDataFromUser(u)
	else:
		print("Enchanté", name)
		stockDataInUser(u)
	text = ""
	while True:
		text = input("Moi                 : ")
		reponse = ""
		if continuer(text):
			getInformationFromAnswer(text, u)
			if text == "info":
				u.printInformationUser()		
			if reponse != "":
				print("Nathanaelle Poilane : " + reponse)
				stockDataInUser(u)
			else:
				reponse = checkCava(text, u)
				if reponse == "":
					reponse = repliqueMode2(text, dico,smalltalk)
				print("Nathanaelle Poilane : " + reponse)
		else:
			print("Nathanaelle Poilane : A bientôt !")
			break;

	return

if __name__=="__main__":
	mode = int(sys.argv[1])

	while(mode != 4):
		while (mode < 0 or mode > 7): 
			mode = int(input("Choisissez un mode entre 0, 1, 2 et 3 (4 pour quitter) "));
		if(mode == 0):
			calou();
		elif(mode == 1):
			mode1();
		elif(mode == 2):
			mode2();
		elif(mode == 3):
			mode3();
		elif(mode == 4):
			break;
		mode = -1
