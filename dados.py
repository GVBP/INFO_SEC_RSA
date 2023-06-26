mensagem = """\
Este é um exemplo de dado a ser criptografado.
Trabalho RSA - NP3
"""

with open('dados.txt', 'w') as arquivo:
    arquivo.write(mensagem)

print("Arquivo 'dados.txt' criado com sucesso!")
