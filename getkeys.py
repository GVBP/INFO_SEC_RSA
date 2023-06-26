import random

# A função generate_key_pair é responsável por gerar um par de chaves para o algoritmo
# de criptografia RSA. Ela recebe dois números primos grandes como parâmetros: p e q.
def generate_key_pair(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    d = mod_inverse(e, phi_n)

    return (e, n), (d, n)

# Função Auxiliar:
  # É a função que retorna o maior divisor comum entre a e b usando o algoritmo de
  # Euclides. É usada para calcular o valor de gcd (phi_n) no exemplo.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Função Auxiliar:
  # É uma função que retorna o inverso multiplicativo modular de a em relação a m
  # usando o algoritmo de Euclides estendido. É usado para calcular a chave privada d.
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError('O inverso modular não existe.')
    return x % m

# Função Auxiliar:
  # É uma função que retorna o maior divisor comum entre a e b, além dos coeficientes
  # de Bézout x e y que satisfazem a identidade de Bézout. É usada para calcular o
  # inverso multiplicativo modular na função mod_inverse.
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

def is_prime(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ler os números primos do arquivo
prime_numbers = []
with open('primekeys.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        if is_prime(number):
            prime_numbers.append(number)

# Verificar se existem pelo menos dois números primos no arquivo
if len(prime_numbers) < 2:
    print("Erro: O arquivo deve conter pelo menos dois números primos.")
    exit(1)

# Selecionar dois números primos aleatórios
p = random.choice(prime_numbers)
q = random.choice(prime_numbers)

# Gerar chave pública e privada
public_key, private_key = generate_key_pair(p, q)

# Salvar chave pública em arquivo
with open('chave_publica.txt', 'w') as file:
    file.write(f'{public_key[0]}\n')
    file.write(f'{public_key[1]}')

# Salvar chave privada em arquivo
with open('chave_privada.txt', 'w') as file:
    file.write(f'{private_key[0]}\n')
    file.write(f'{private_key[1]}')

print("Arquivos 'chave_publica.txt' e 'chave_privada.txt' gerados com sucesso!")
