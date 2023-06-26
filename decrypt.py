import base64

# Função decrypt para descriptografar a mensagem:
  # Recebe uma lista de inteiros representando a mensagem criptografada e retorna 
  # a mensagem descriptografada. Para cada número na lista cipher, é aplicada a fórmula
  # pow(char, d, n) para calcular o valor descriptografado correspondente, e em seguida
  # é convertido de volta para caractere usando a função chr.
def decrypt(key_file,input_file,output_file):
    # Leitura da chave privada
    with open(key_file, 'r') as file:
        key_data = file.readlines()
        d = int(key_data[0].strip())
        n = int(key_data[1].strip())

    # Leitura dos números inteiros longos criptografados
    with open(input_file, 'r') as file:
        cipher_data = file.read().split()
        cipher = [int(num) for num in cipher_data]

    # Descriptografia
    message = [chr(mod_pow(char, d, n)) for char in cipher]
    decrypted_message = ''.join(message)
    decoded_message = base64.b64decode(decrypted_message).decode()

    # Escrita dos dados descriptografados em um arquivo de saída
    with open(output_file, 'w') as file:
        file.write(decoded_message)

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
#decrypt('chave_privada.txt','criptografado.txt','descriptografado.txt')
decrypt(chave_file,entrada_file,saida_file)
