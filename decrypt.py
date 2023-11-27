import os
import pyaes

## abre o arquivo criptografado
file_name = "data.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografar o arquivo
key = b"t35t3r4n50mw4r35"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove o arquivo criptografado
os.remove(file_name)

## cria o arquivo descriptografado
new_file = "data.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
