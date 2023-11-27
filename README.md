# Project-ransomware-DIO
Projeto de Ransomware projetado para o Boot Camp Santander Cybersecurity

Foram criados 3 arquivos: encrypt.py, decrypt.py e data.txt.

No arquivo data foi escrito um texto com uma flag.

O arquivo encrypt.py ao ser executado, vai abrir, ler e fechar o arquivo data.txt.
Em seguida ele remove o arquivo data.txt.
No passo seguinte é atribuido uma chave para criptografar os dados.
Logo depois, é feito a criptografia dos dados.
Por fim, ele cria o novo arquivo, insere os dados encriptografados no novo arquivo e salva no diretório.

Já o arquivo decrypt.py ao ser executado, vai abrir, ler e fechar o arquivo data.txt.
Em seguida é atribuido a chave para descriptografar os dados.
No passo seguinte, é feito a decriptografia dos dados.
Logo depois ele remove o arquivo decriptografado.
Por fim, ele cria o novo arquivo, insere os dados decriptografados no novo arquivo e salva no diretório.
