import socket
import cv2
import numpy as np


# Retorna o path

class SocketPown:
	def __init__(self, path, fileName):
		self.path = path
		self.fileName = fileName
		self.filePath = ""
		self.fileLoad = False
	def cd(self):
		jpath = ""
		lastBar = 0
		
		# Varre a string de tras para frente, procurando a primeira barra nesse sentido,
		# que sera a ultima no sentido normal
		for i in range(len(self.path)-1,0,-1):
			if(self.path[i] == '/'):
				# Nao inclui a barra na string
				lastBar = i+1
				break
		
		for i in range(0,lastBar):
			jpath += self.path[i]
		
		
		print('JPATH :' + jpath)
		self.filePath = jpath
		
	def load(self):
		print("Load arquivo")
		"Carregar o arquivo do path"
		
		
		self.fileLoad = open(self.path, 'r').read()
	
	def send(self):
		pass
		
	def recv(self):
		print('function - recv -')
		'''Enviar o arquivo via socket'''
		# Abrir thread
		# Sistema de parear?
		if(self.fileLoad):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			server = ('localhost', 3200)
			print('Listening on %s' % server)
			sock.bind(server)
			sock.listen(1)
			
			while True:
				print('Wait for connection' )
				con, addr = sock.accept()
				while True:
					data = con.recv()
					print('data received %s' %data)
					if(data == 'break'):
						break;
			
			print('Connection closed')
			con.close()
			break;
				
		
		
