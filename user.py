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

	# ajoute un membre de la famille en fondtion d'une clé k (ex:Tante) et d'une valeur v (ex:George).
	# si un des deux est nul, il n'y a pas d'ajout.
	def addFamilyMember(self,k,v):
		if k != "":
			if v != "":
				if k in self.famille:
					self.famille[k].append(v)
					print("ajout")
				else:
					self.famille[k] = []
					self.famille[k].append(v)
					print("cration")

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
