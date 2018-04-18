class User:
	
	def __init__(self, prenom):
		# infos : prénom, age, adresse
		self.infos = []
		self.infos.append(prenom)

		# famille : 
		self.famille = {}

		# sports :
		self.sport = []

		# gouts :
		self.gouts = [[], []]

		# relations :
		self.relation = {}

		# etat :
		self.etat = 0

		# anecdotes
		self.anecdotes = []

	# ajoute un gouts
	def addGouts(self,k,b):


	# permet d'afficher les informations sotckées sur le gouts
	def printGoutsUser(self):


	# ajoute un sport
	def addSport(self,sport):
		if sport not in self.sport:
			self.sport.append(sport)

	# permet d'afficher les informations sotckées sur le sport
	def printSportUser(self):
		print("Sport  : ")
		for k in self.sport:	
			print("\t-" + k.lower())
			
		print("")

	# ajoute un membre de la famille en fonction d'une clé k (ex:Tante) et d'une valeur v (ex:George).
	# si un des deux est nul, il n'y a pas d'ajout.
	def addFamilyMember(self,k,v):
		if k != "":
			if v != "":
				if k in self.famille:
					self.famille[k].append(v)
				else:
					self.famille[k] = []
					self.famille[k].append(v)

	# permet d'afficher les informations sotckées sur la famille
	def printFamilyUser(self):
		print("Famille :")
		for k in self.famille:
			print("Nombre ",k.lower()+("s " if len(self.famille[k]) > 1 else " "),len(self.famille[k]), " : ")
			for name in self.famille[k]:
				print("\t-" + name.lower())

		print("")
	# ajoute une relation en fonction d'une clé k (ex:Tante) et d'une valeur v (ex:George).
	# si un des deux est nul, il n'y a pas d'ajout.
	def addRelation(self,k,v):
		if k != "":
			if v != "":
				if k in self.relation:
					self.relation[k].append(v)
				else:
					self.relation[k] = []
					self.relation[k].append(v)

	# permet d'afficher les informations sotckées sur la relation
	def printRelationUser(self):
		print("Relations :")
		for k in self.relation:
			print("Nombre ",k.lower()+("s " if len(self.relation[k]) > 1 else " "),len(self.relation[k]), " : ")
			for name in self.relation[k]:
				print("\t-" + name.lower())

		print("")

	# permet d'afficher l'ensemble des informations stockées
	def printInformationUser(self):
		print("Information User ", self.infos[0])
		self.printFamilyUser()
		self.printSportUser()
		self.printRelationUser()
