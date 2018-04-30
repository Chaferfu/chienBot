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

		# anecdotes
		self.anecdotes = []


	def findSomeone(self, nom):
		for key,valeur in self.relation.items():
			if nom.upper() in valeur:
				return key
		return
	
	def findSport(self, sport):
		if sport.upper() in self.sport:
			return True;

	# ajoute un gout
	def addDislike(self,k,b):
		for a in b:
			if a not in self.gouts[1] and a != '':
				self.gouts[1].append(a)

	# ajoute un gout
	def addLike(self,k,b):
		for a in b:
			if a not in self.gouts[0] and a != '':
				self.gouts[0].append(b)

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
				self.sport.append(sport)

	# permet d'afficher les informations sotckées sur le sport
	def printSportUser(self):
		print("Sport  : ")
		for k in self.sport:	
			print("\t-" + k.lower())
			
	def askQuestionToCompleteAnswer(self,question, fileWordToUnderstand, element = None, x = None):
		words = []
		with open("valuesNames", "r") as filepointer:
			for line in filepointer.readlines():
				line = line.strip()
				words.append(line)
		if(element != None and x != None):
			question.replace(x, element)

		print("Nathanaelle Poilane : " + question)
		text = input("Moi                 : ")
		for w in words:
			if f.findStringInString(w, text):
				return w
		return ""

	# ajoute un membre de la famille en fonction d'une clé k (ex:Tante) et d'une valeur v (ex:George).
	# si un des deux est nul, il n'y a pas d'ajout.
	def addRelation(self,k,v):
		for a, b in itertools.zip_longest(k,v):
			if a == None:
				a = self.askQuestionToCompleteAnswer("Oh vraiment, c'est quoi son nom ?","valuesNames")
			elif b == None:
				b = self.askQuestionToCompleteAnswer("Ah, c'est qui * ?","keyRelation", v, "*")
			if a != None and b != None:
				if a in self.relation:
					self.relation[a].append(b)
				else:
					self.relation[a] = []
					self.relation[a].append(b)

		# if k != "" or v != "":
		# 	if v == "":
		# 		v = self.askQuestionToCompleteAnswer("Oh vraiment, c'est quoi son nom ?","valuesNames")
		# 	elif k == "":
		# 		k = self.askQuestionToCompleteAnswer("Ah, c'est qui * ?","keyRelation", v, "*")
		# 	if k != "" and v != "" :
		# 		if k in self.relation:
		# 			self.relation[k].append(v)
		# 		else:
		# 			self.relation[k] = []
		# 			self.relation[k].append(v)

	# permet d'afficher les informations sotckées sur la famille
	def printRelationUser(self):
		print("Relations :")
		for k in self.relation:
			print("Nombre ",k.lower()+("s " if len(self.relation[k]) > 1 else " "),len(self.relation[k]), " : ")
			for name in self.relation[k]:
				print("\t-" + name.lower())

	def changeMood(self, val):
		self.etat += val

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
