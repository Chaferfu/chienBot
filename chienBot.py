
from functions import *
from user import *
import sys
from random import randint, uniform
import random 
from time import sleep
import os
import pickle
import user

def mode1():
	calou()
	return

def repliqueMode2(text,dico,smalltalk):

	themeDetecte, motDetecte = analyzeSentence(text, dico)
	if themeDetecte == "no":
		jeSuisDetecte, reponse = jeSuis(text)			
		if jeSuisDetecte == "no":
			reponse = random.choice(smalltalk)

	else:
		reponse = reaction(dico, themeDetecte, motDetecte)

	return reponse



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

	name = input("name pls :\n")
	u = User(name)
	if check_Connexion(name, "utilisateurs"):
		print("Oh content de te revoir ", name)
		u = readDataFromUser(u)
	else:
		print("Enchanté ", name)
	text = ""
	while continuer(text):
		temps = time()
		text = input("Moi                 : ")
		reponse = ""
		getInformationFromAnswer(text, u)

		if reponse != "":
			print("Nathanaelle Poilane : " + reponse)
			stockDataInUser(u)

		else:
			reponse = repliqueMode2(text, dico,smalltalk)
			print("Nathanaelle Poilane : " + reponse)

	return

if __name__=="__main__":
	mode = int(sys.argv[1])
	print(mode)

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
			testMathias();
		elif(mode == 5):
			testNathan();
		elif(mode == 6):
			testBrian();
		else:
			break;
		mode = -1
