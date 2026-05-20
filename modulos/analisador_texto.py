import re
# Parte 1
def conta_palavras(texto: str) -> int:
    palavras = texto.split()
    return len(palavras)


# Parte 2
def palavra_mais_longa(texto: str) -> str:
    palavras = texto.split()
    return max(palavras, key=len)


# Parte 2
def frequencia_vogais(texto: str) -> dict:
    vogais = {}

    for letra in texto.lower():
        if letra in 'aeiou':
            vogais[letra] = vogais.get(letra, 0) + 1 # Forma mais simples do que o duplo if else

    return vogais

# Parte 2
def conta_frases(texto: str) -> int:
    frases = re.split(r'[.!?]+', texto)

    frases_validas = [f for f in frases if f.strip()]

    return len(frases_validas)


# Parte 1
def remove_espacos_duplicados(texto: str) -> str:
    return ' '.join(texto.split())


# Parte 3
def salva_relatorio(texto: str, nome_arquivo: str) -> None:

    relatorio = f"""
    RELATÓRIO

    Número de caracteres: {len(texto)}
    Número de palavras: {conta_palavras(texto)}
    Palavra mais longa: {palavra_mais_longa(texto)}
    Número de frases: {conta_frases(texto)}

    Frequência de vogais:
    {frequencia_vogais(texto)}
    """

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(relatorio)


# Parte 3
def procurar_palavra(texto: str) -> str:
    palavraUsuario = str(input("Insira uma palavra:"))
    contagem = 0
    for palavra in texto.lower().split():
        if palavra == palavraUsuario:
            contagem += 1
    if contagem == 0:
        return "Palavra não encontrada"
    else: 
       return f"A palavra aparece {contagem} vezes."
    
def subsPalavra(texto: str, palavra_old: str, palavra_new) -> str:
    palavras = texto.split()
    for i in range(len(palavras)): 
        if palavras[i] == palavra_old:
            palavras[i] = palavra_new
    return ' '.join(palavras)