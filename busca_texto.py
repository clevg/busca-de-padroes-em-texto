import time

# Algoritmo Shift-And
def shift_and(text, pattern):
    m = len(pattern)
    n = len(text)
    mask = [0] * 255
    for i in range(m):
        mask[ord(pattern[i])] |= 1 << i
    result = []
    state = 0
    for i in range(n):
        state = ((state << 1) | 1) & mask[ord(text[i])]
        if state & (1 << (m - 1)):
            result.append(i - m + 1)
    return result

# Algoritmo de força bruta
def forca_bruta(text, pattern):
    result = []
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            result.append(i)
    return result

# Índice tipo arquivo invertido
def criar_indice(text):
    indice = {}
    words = text.split()
    for i, word in enumerate(words):
        if word not in indice:
            indice[word] = [i]
        else:
            indice[word].append(i)
    return indice

# Leitura de arquivo real
def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return file.read()

# Programa principal
if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo de texto (.txt): ").strip()
    padrao = input("Digite o padrão a ser buscado: ").strip()

    try:
        texto = ler_arquivo(caminho)
        print(f"\nArquivo carregado com {len(texto)} caracteres.\n")

        # Shift-And
        inicio = time.time()
        resultado_shift = shift_and(texto, padrao)
        fim = time.time()
        print(f" Shift-And encontrou {len(resultado_shift)} ocorrências em {fim - inicio:.6f} segundos.")

        # Força Bruta
        inicio = time.time()
        resultado_bruta = forca_bruta(texto, padrao)
        fim = time.time()
        print(f" Força Bruta encontrou {len(resultado_bruta)} ocorrências em {fim - inicio:.6f} segundos.")

        # Índice Invertido
        inicio = time.time()
        indice = criar_indice(texto)
        fim = time.time()
        palavras_encontradas = indice.get(padrao, [])
        print(f" Índice invertido encontrou {len(palavras_encontradas)} ocorrências em {fim - inicio:.6f} segundos.")

    except FileNotFoundError:
        print(" Arquivo não encontrado. Verifique o caminho e tente novamente.")
