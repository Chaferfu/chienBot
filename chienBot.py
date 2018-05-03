from functions import *
from user import *
import sys

def mode1():
	calou()
	return

def mode2():

	smalltalk = read_word_list_file("mode2_hmmm")
	dico = stock_Words_And_Questions("mode2")
	derniere = ""

	text = ""
	while continuer(text):

		text = input("Moi                 : ")

		themeDetecte, motDetecte = analyzeSentence(text, dico)

		sleep(uniform(0.5,1.5))

		if themeDetecte == "no":

			reponse = random.choice(smalltalk)
			while reponse == derniere:
				reponse = random.choice(smalltalk)

		else:
			reponse = reaction(dico, themeDetecte, motDetecte)
			while reponse == derniere:
				reponse = reaction(dico, themeDetecte, motDetecte)


		print("Nathanaelle Poilane : " + reponse)
		derniere = reponse

	return

def mode3():
	name = input("name pls :\n")
	u = User(name)
	if check_Connexion(name, "utilisateurs"):
		print("Oh content de te revoir ", name)
		u = readDataFromUser(u)
	else:
		print("Enchanté ", name)
	text = ""
	while continuer(text):
		text = input("Moi                 : ")
		reponse = ""
		getInformationFromAnswer(text, u)
		print("Nathanaelle Poilane : " + reponse)
	stockDataInUser(u)
	tmp = readDataFromUser(u)
	tmp.printInformationUser()
	return

def testMathias():
	dico = stock_Words_And_Questions("mode2")
	print(dico)
	print(analyzeSentence("Salut haha ouais ki lol", dico))
	return

def testNathan():
	u = User("Nathanaelle")
	getInformationFromAnswer("frère germain", u)
	print(u.findSomeone("germain"))
	stockDataInUser(u)
	u2 = readDataFromUser(u)

	# while True :
	# 	name = input("name pls :\n")
	# 	if check_Connexion(name, "utilisateurs"):
	# 		user1 = user.User(name)
	# 		user1.famille['soeur'] = "Hombeline"
	# 		print("Oh content de te revoir ", name)
	# 		stockDataInUser(user1)
	# 		tmp = readDataFromUser(user1)
	# 		print(tmp.infos[0])
	# 		print(tmp.famille)
	# 	else:
	# 		print("Enchanté ", name)
	# 		fichier = open(os.path.join("Users",name), "a")

	# 		fichier.close()

def testBrian():
	mode3()

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
