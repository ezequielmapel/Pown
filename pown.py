# Python main

import pytesseract as ocr
import numpy as np
import cv2

from PIL import Image
# other class
import socket_pown as sp
import wfile_pown as wp


# tipando a leitura para os canais de ordem RGB
imagem = Image.open('image.png').convert('RGB')


npimagem = np.asarray(imagem).astype(np.uint8)

npimagem[:, :, 0] = 0 # zerando o canal R (RED)
npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)

im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

binimagem = Image.fromarray(thresh)

phrase = ocr.image_to_string(binimagem, lang='por')
phrase = phrase.lower().encode('utf-8');

cont = ""


for i in range(len(phrase),0,-1):
    cont +=phrase[i-1]

    if(cont[::-1] == 'png'):
        cont +="."
phrase = cont[::-1]
print("Nome do arquivo: %s"%(phrase))






# criando objeto Wfile
wFile = wp.Wfile(phrase)
wFile.find()


# instanciando objeto Socket Pown e passando o Path retornado por Wfile / E o nome do arquivo.
SocketPown = sp.SocketPown(wFile.read(), phrase)
SocketPown.cd()
SocketPown.load()

