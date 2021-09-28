import random
import base64
import hashlib

class cryptor():
	def __init__(self, x, y, role):
		self.toServer = x
		self.toServerSend = 0
		self.toClient = y
		self.toClientSend = 0
		self.role = role
		
	def decrypt(self, crypted):
		message = ""
		crypted = base64.b64decode(crypted)
		if self.role == "client":
			for x in crypted:
				m = hashlib.md5()
				m.update("%d" %(self.toClient + self.toClientSend))
				message += chr((ord(x) - ord(m.digest()[0])) % 255)
				self.toClientSend += 1
		else:
			for x in crypted:
				m = hashlib.md5()
				m.update("%d" %(self.toServer + self.toServerSend))
				message += chr((ord(x) - ord(m.digest()[0])) % 255)
				self.toServerSend += 1
		return message
		
	def encrypt(self, message):
		crypted = ""
		if self.role == "client":
			for x in message:
				m = hashlib.md5()
				m.update("%d" %(self.toServer + self.toServerSend))
				crypted += chr((ord(x) + ord(m.digest()[0])) % 255)
				self.toServerSend += 1
		else:
			for x in message:
				m = hashlib.md5()
				m.update("%d" %(self.toClient + self.toClientSend))
				crypted += chr((ord(x) + ord(m.digest()[0])) % 255)
				self.toClientSend += 1							
		return base64.b64encode(crypted)