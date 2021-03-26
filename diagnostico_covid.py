

def ler_arquivo(nome_do_arquivo):
    """Lê o arquivo 'nome_do_arquivo' contendo linhas com dois dados separados por '#' e retorna estes dados
    em um dicionário onde a chave é o primeiro dado da linha e o valor é o segundo dado da linha"""
    d = dict()
    with open(nome_do_arquivo, 'r') as arq:
        while True:
            linha = arq.readline().rstrip('\n').split('#')
            if linha == ['']:
                break
            d[linha[0]] = linha[1]
    return d


def compara_strings(string1, string2):
    """Função que compara duas strings de mesmo tamanho caractere por caractere: Se houver similiaridade acima de
    50% retorna verdadeiro, senão retorna falso"""
    count = 0       # Inicializa um contador com zero ocorrências
    for indice in range(len(string1)):
        if string1[indice] == string2[indice]:
            count += 1
    if count/len(string1) > 0.5:
        return True
    else:
        return False


virus_arquivo = 'rna_covid.txt'
pessoa_arquivo = 'dna_pessoa(1).txt'
virus, pessoa = 0, 0
try:
    virus = ler_arquivo(virus_arquivo)
except FileNotFoundError:
    print(f'''
    O arquivo {repr(virus_arquivo)} não foi encontrado.
    Certifique-se de nomear o arquivo corretamente e de mantê-lo no mesmo diretório deste programa e tente novamente
    ''')

try:
    pessoa = ler_arquivo(pessoa_arquivo)
except FileNotFoundError:
    print(f'''
    O arquivo {repr(pessoa_arquivo)} não foi encontrado.
    Certifique-se de nomear o arquivo corretamente e de mantê-lo no mesmo diretório deste programa e tente novamente
    ''')

if virus!=0 and pessoa!=0:
    for nome_do_virus, rna in virus.items():
        infectados = []
        titulo = ' CPFs possivelmente infectados pela mutação ' + repr(nome_do_virus) + ' do Coronavírus '
        print(f'\n{titulo:-^100}')
        for cpf, dna in pessoa.items():
            if compara_strings(rna, dna):
                infectados.append(cpf)
        if len(infectados) == 0:
            texto = 'Ninguém possui DNA compatível com o RNA da mutação ' + repr(nome_do_virus) + ' do vírus\n'
            print(f'\n{texto:^100}')
        else:
            indice = 0
            while indice < len(infectados):
                count = 0
                while indice < len(infectados) and count < 6:
                    if indice + 1 == len(infectados):
                        print(infectados[indice])
                    else:
                        print(infectados[indice], end=', ')
                    count += 1
                    indice += 1
                print()