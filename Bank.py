class user:
	accounts = 0
	
	@classmethod
	def __init__(self, username, password):
		self.username = username
		self.password = password
		user.accounts += 1
	

	def encrypt(self):
		privatekey = 7411
		letters = "abcdefghijklmnopqrstuvwxyz"
		encrypted = ""
		for letter in self.username:
			if letter in letters:
				newindex = (letters.find(letter) + privatekey) % 26
				encrypted += letters[newindex]
			elif letter.lower() in letters:
				newindex = (letters.find(letter.lower()) + privatekey) % 34
				encrypted += letters[newindex].upper()
			
			self.username = encrypted
	

