import base64

# Função encrypt para criptografar a mensagem:
  # Recebe uma mensagem como entrada e retorna uma lista de inteiros representando 
  # a mensagem criptografada. Cada caractere da mensagem é convertido em um número 
  # inteiro usando a função ord, e em seguida é aplicada a fórmula pow(ord(char), e, n) 
  # para calcular o valor criptografado correspondente.
def encrypt(key_file, input_file, output_file):
    # Leitura da chave pública
    with open(key_file, 'r') as file:
        key_data = file.readlines()
        e = int(key_data[0].strip())
        n = int(key_data[1].strip())

    # Leitura do dado a ser criptografado
    with open(input_file, 'r') as file:
        message = file.read()
        encoded_message = base64.b64encode(message.encode()).decode()

    # Criptografia
    cipher = [mod_pow(ord(char), e, n) for char in encoded_message]

    # Escrita do resultado criptografado em um arquivo de saída
    with open(output_file, 'w') as file:
        file.write(' '.join(str(num) for num in cipher))

# A função retorna o resultado da exponenciação modular, ou seja, o valor de base
# elevado à potência exponent, mas reduzido pelo módulo modulus.
  # base: O número base que será elevado à potência.
  # exponent: O expoente ao qual a base será elevada.
  # modulus: O valor do módulo usado na operação.
def mod_pow(base, exp, modulus):
    result = 1
    base = base % modulus

    while exp > 0:
        if exp & 1:
            result = (result * base) % modulus
        exp >>= 1
        base = (base * base) % modulus

    return result

# Solicitar ao usuário os nomes dos arquivos
chave_file = input("Digite o nome do arquivo contendo as chaves: ")
entrada_file = input("Digite o nome do arquivo de entrada: ")
saida_file = input("Digite o nome do arquivo de saída: ")

# Verificar se os nomes dos arquivos possuem a extensão ".txt"
if not chave_file.endswith(".txt") or not entrada_file.endswith(".txt") or not saida_file.endswith(".txt"):
    print("Erro: Os nomes dos arquivos devem ter a extensão .txt")
    exit(1)

# Exemplo de uso
#encrypt('chave_publica.txt','dados.txt','criptografado.txt')
encrypt(chave_file,entrada_file,saida_file)
