class user:
	__accounts = 0
	__totalMoney = 0
	__privatekey = 7411
	def __init__(self, username, password, amount=0):
		self.username = username
		self.password = password
		self.balance = amount
		user.__accounts += 1
		user.__totalMoney += amount
	def encrypt(self):
		letters = "abcdefghijklmnopqrstuvwxyz!@#$%&*?~123456789"
		encrypted = ""
		for letter in self.username:
			newindex = (letters.find(letter) + __privatekey) % 34
			encrypted += letters[newindex]
		self.username = encrypted
    	
    	


