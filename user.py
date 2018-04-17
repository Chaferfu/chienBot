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
		self.rel = {}

		# etat :
		self.etat = 0

		# anecdotes
		self.anecdotes = []

	# ajoute un sport
	def addSport(self,sport):
		if sport not in self.sport:
			self.sport.append(sport)

	# permet d'afficher les informations sotckées sur le sport
	def printSportUser(self):
		i = 0
		print("Pour ce qui est de tes activités sportives ? Tu m'as déjà parlé de ", end='')
		for k in self.sport:	
			i = i + 1
			print(("ou encore de " if len(self.sport) <= i else ""), end='')
			print(k + (", " if len(self.sport) > i else ""), end='')
			
		print(".")
		print("\nEnfin en tout cas c'est tout ce que tu as pu me dire !")

	# ajoute un membre de la famille en fondtion d'une clé k (ex:Tante) et d'une valeur v (ex:George).
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
		print("Concernant votre famille, voilà tout ce que je sais :")
		for k in self.famille:
			print("Vous avez",len(self.famille[k]),k.lower()+("s " if len(self.famille[k]) > 1 else " "), end='')
			for name in self.famille[k]:
				print("(" + name.lower() + ")", end='')
			print()
		print("\nEt je crois que c'est à peu près tout...")

	# permet d'afficher l'ensemble des informations stockées
	def printInformationUser(self):
		print("Vous voulez savoir tout ce qeu je sais sur vous ? très bien, si vous insistez...")
		self.printFamilyUser()
		self.printSportUser()
