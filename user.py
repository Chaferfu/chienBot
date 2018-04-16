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