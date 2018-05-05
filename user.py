from chienBot import *
import functions as f
import itertools

class User:
	
	def __init__(self, prenom):
		# infos : prénom, age, adresse
		self.infos = []
		self.infos.append(prenom)

		# sports :
		self.sport = []

		# gouts [Like - Dislike]:
		self.gouts = [[], []]

		# relations :
		self.relation = {}

		# etat :
		self.etat = 0

	def findSomeone(self, nom):
		for key,valeur in self.relation.items():
			if nom.upper() in valeur:
				return key
		return ""
	
	def findSport(self, sport):
		for a in sport:
			if a.upper() in self.sport:
				return True;

	# ajoute un gout
	def addDislike(self,k,b):
		if k:
			for a in b:
				if a not in self.gouts[1] and a != '':
					self.gouts[1].append(a)
				else:
					print("Nathanaelle Poilane : " + f.getRandomPhraseFrom("questionDislike", a.lower(), "*"))
					text = input("Moi                 : ")

	# ajoute un gout
	def addLike(self,k,b):
		if k:
			for a in b:
				if a not in self.gouts[0] and a != '':
					self.gouts[0].append(a)
				else:
					print("Nathanaelle Poilane : " + f.getRandomPhraseFrom("questionLike", a.lower(), "*"))
					text = input("Moi                 : ")

	# permet d'afficher les informations stockées sur le gout
	def printGoutsUser(self):
		print("Goûts  : ")
		print("Like : ")
		for k in self.gouts[0]:	
			print("\t-" + str(k).lower())
		print("Dislike : ")
		for k in self.gouts[1]:	
			print("\t-" + str(k).lower())	

	# ajoute un sport
	def addSport(self,sport):
		for a in sport:
			if a not in self.sport and a != '':
				self.sport.append(a)
			else:
				print("Nathanaelle Poilane : " + f.getRandomPhraseFrom("questionSport",a.lower(), "*"))
				text = input("Moi                 : ")


	# permet d'afficher les informations sotckées sur le sport
	def printSportUser(self):
		print("Sport  : ")
		for k in self.sport:	
			print("\t-" + k.lower())
	
	# Pose une question pour que une information stockée puisse être stocké dans le user.
	def askQuestionToCompleteAnswer(sxelf,question, fileWordToUnderstand, element = None, x = None):
		words = []
		with open(fileWordToUnderstand, "r") as filepointer:
			for line in filepointer.readlines():
				line = line.strip()
				words.append(line)
		if(element != None and x != None):
			question = question.replace(x, element.lower())

		print("Nathanaelle Poilane : " + question)
		text = input("Moi                 : ")
		for w in words:
			if f.findStringInString(w, text):
				return w
		return "inconnu"

	# ajoute un membre de la famille en fonction d'une clé k (ex:Tante) et d'une valeur v (ex:George).
	# si un des deux est nul, il n'y a pas d'ajout.
	def addRelation(self,k,v):
		for rel, nom in itertools.zip_longest(k,v):
			if (nom != None and self.findSomeone(nom) == "") or nom == None:
				if nom == None:
					nom = self.askQuestionToCompleteAnswer("Oh vraiment, c'est quoi son nom ?","valuesNames")
				elif rel == None:
					rel = self.askQuestionToCompleteAnswer("Ah, c'est qui * ?","keyRelation", nom, "*")
				if nom != None and rel != None:
					if rel not in self.relation:
						self.relation[rel] = []
					if nom not in self.relation[rel]:
						self.relation[rel].append(nom)
			elif nom != None and rel == None:
				words = []
				with open("relationAnswer", "r") as filepointer:
					for line in filepointer.readlines():
						line = line.strip()
						words.append(line)

				key = self.findSomeone(nom)
				for w in words:
					if f.findStringInString(key, w):
						print("Nathanaelle Poilane : " + f.getRandomPhraseFrom("questionRelation",nom.lower(), "*", w.lower(), "#"))
						text = input("Moi                 : ")

	# permet d'afficher les informations sotckées sur la famille
	def printRelationUser(self):
		print("Relations :")
		for k in self.relation:
			print("Nombre ",k.lower()+("s " if len(self.relation[k]) > 1 else " "),len(self.relation[k]), " : ")
			for name in self.relation[k]:
				print("\t-" + name.lower())

	def changeMood(self, val):
		self.etat += val
		if self.etat <= -5:
			print("Nathanaelle Poilane : " + f.getRandomPhraseFrom("questionBadmood",self.infos[0], "*"))
			text = input("Moi                 : ")
		if self.etat >= 5:
			print("Nathanaelle Poilane : " + f.getRandomPhraseFrom("questionGoodMood",self.infos[0], "*"))
			text = input("Moi                 : ")


	def getMood(self):
		if etat >= 0:
			return "PPR"
		if etat < 0:
			return "VNR"

	# permet d'afficher l'ensemble des informations stockées
	def printInformationUser(self):
		print("Information User ", self.infos[0])
		self.printSportUser()
		self.printRelationUser()
		self.printGoutsUser()
