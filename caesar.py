lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Cipher:
	def __init__(self, text):
		self.text = text
	
	def __str__(self):
		return self.text

	def encrypt(self, shift):
		shift %= 26
		table = str.maketrans(lower + upper, lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift])
		return Cipher(self.text.translate(table))

	def decrypt(self, shift):
		shift %= 26
		table = str.maketrans(lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift], lower + upper)
		return Cipher(self.text.translate(table))

	def brute(self):
		for i in range(26):
			yield i, str(self.decrypt(i))