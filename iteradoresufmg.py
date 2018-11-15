#1. Escreva uma fun¸c˜ao que receba um inteiro n e uma lista de nomes de arquivos como argumentos
#%e imprima todas as linhas contidas nos arquivos com tamanho maior que n caracteres.
def ylins(arq):
    for lin in open(arq):
        if lin.length() > s:
            yield lin

def q1(n, listNames):
    for arq in listNames:
        lins = yLins(arq)
        for lin in lins:
            print(lin)

#2. Escreva um programa que receba uma lista de nomes de arquivos como argumentos e imprima
#o n´umero total de linhas contidas nos arquivos mas excluindo linhas em branco, isto ´e, linhas
#que contˆem apenas caracteres c para os quais c.isspace () ´e igual a True. Nota: o iterador de
#linhas de arquivos inclui o caractere ’\n’ como parte (´ultimo caractere) da linha (a condi¸c˜ao
#que testa a ocorrˆencia de apenas espa¸cos em uma linha deve considerar isso).
def yCount(arq):
    count = 0
    for lin in open(arq):
        if lin[0] != "\n":
            count += 1
    return count

def q2(listNames):
    count = 0
    for arq in listNames:
        count += yCount(arq)
    print(count)

#3. Escreva um programa que receba uma lista de nomes de arquivos como argumentos e imprima
#i) para cada arquivo, seu nome e o n´umero de linhas contidas no arquivo, e ii) o n´umero total
#de linhas contidas nos arquivos. Teste
def countLines(arq):
    count = 0
    for lin in open(arq):
        count += 1
    print(count)
    return count

def q3(listNames):
    count = 0
    for elem in listNames:
        print(elem)
        count += countLines(elem)
    print(count)

#4. Escreva um programa que receba um inteiro n e um nome f de arquivo como argumentos
#e imprima arquivos com no m´aximo n linhas contendo cada um n linhas do arquivo f: o
#i-´esimo arquivo cont´em as linhas de n´umero (i − 1) ∗ n + 1 a i ∗ n, para i come¸cando de 1 at´e
#que as linhas do arquivo f terminem.
def q4(n, f):
    numFiles = 0, currentLine = 0
    for lin in open(f):
        if(currentLine == n):
            numFiles = numFiles + 1
        else:
            outputFile = open("output"+format(numFiles)+".txt", "a")
            outputFile.write(lin)
            currentLine = currentLine + 1
            outputFile.close()

#Escreva uma fun¸c˜ao enumerate que se comporte como enumerate.
def q5(iterable):
    count = 0
    for elem in iterable:
        yield count, elem
        count += 1
