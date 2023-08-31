# Alunos: Amanda de Oliveira Barbosa dos Santos, Felyppe Pardino da Silva e Larissa Cristina Alves de Costa

"""Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de operações que serão realizadas entre dois conjuntos de dados.
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da operação (U para união, l para interseção, D para diferença e C produto cartesiano), a segunda e terceira linhas conterão os elementos dos conjuntos separados por virgulas."""

import os

conj1 = {0}
ler_conj1 = ''
ler_conj2 = ''
conj2 = {0}
conj3 = {0}
resp = []
i = 0
linhas = 0
operacao = ''

nome_arquivo = str(input('Digite o nome do arquivo: '))

if os.path.exists(f'{nome_arquivo}.txt'):

    with open(f"{nome_arquivo}.txt") as c:
        qtd_operacoes = int(c.readline())
        while i < qtd_operacoes:
            conj1.clear()
            conj2.clear()
            operacao = c.readline().rstrip()
            ler_conj1 = c.readline().rstrip().replace(' ','')
            conj1.update(ler_conj1.split(','))
            ler_conj2 = c.readline().rstrip().replace(' ','')
            conj2.update(ler_conj2.split(','))
            if (operacao == 'U'):
                conj3 = conj1.union(conj2)
                mensagem = f'União: conjunto 1 {conj1}, conjunto 2 {conj2}. Resultado: {conj3}'
                resp.append(mensagem)
            elif (operacao == 'I'):
                conj3 = conj2.intersection(conj1)
                mensagem = f'Intersecção: conjunto 1 {conj1}, conjunto 2 {conj2}. Resultado: {conj3}'
                resp.append(mensagem)
            elif (operacao == 'D'):
                conj3 = conj1.difference(conj2)
                mensagem = f'Diferença: conjunto 1 {conj1}, conjunto 2 {conj2}. Resultado: {conj3}'
                resp.append(mensagem)
            elif (operacao == 'C'):
                conj3 = [i+str(j) for i in conj1 for j in conj2]
                mensagem = f'Produto Cartesiano: conjunto 1 {conj1}, conjunto 2 {conj2}. Resultado: {conj3}'
                resp.append(mensagem)
            i += 1

    while linhas < qtd_operacoes:
      print(resp[linhas], '\n')
      linhas += 1
else:
    print("Arquivo não encontrado!")