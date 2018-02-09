import subprocess
from subprocess import PIPE

class Wfile:
    def __init__(self, nameFile):
        self.nameFile = nameFile
        self.readFile = ""

    def find(self):
        print("Wfile.find " + self.nameFile)
        arq = "path.txt"
        command = ['find','.', '-name', self.nameFile]

        with open(arq, 'r+') as out:
            st = subprocess.Popen(['find','.', '-name', self.nameFile], stdout=out)

        return True


    def read(self):
        arq = "path.txt"
        arqv = open(arq, 'r')
        arqv = arqv.readlines(5)
        tam = len(arqv[0])-1
        arqv = arqv[0]

        return str(arqv[:tam:])
