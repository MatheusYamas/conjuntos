#FUNÇÃO MAIN
def main():
    #LISTA OS ARQUIVOS TXT
    operacoes = ['operacoes/operacao1.txt', 'operacoes/operacao2.txt', 'operacoes/operacao3.txt']
    #LOOP ENTRE OS ARQUIVOS TXT
    for operacao in operacoes:
        print("\nArquivo {}".format(operacao))
        #LEITURA DOS ARQUIVOS TXT
        with open(operacao, 'r') as arquivo:
            #LEITURA DA PRIMEIRA LINHA DO ARQUIVO TXT
            num_operacao = int(arquivo.readline().strip()[0])
            #VERIFICAÇÃO REFERENTE A PRIMEIRA LINHA
            if num_operacao > 0:
                #UM LOOP DO CODIGO DE ACORDO COM QUANTAS OPERAÇÕES DESEJAR
                for _ in range(num_operacao):
                    #LEITURA DA SEGUNDA LINHA DO CODIGO, PARA OBTER A OPERAÇÃO DESEJADA
                    cod_operacao = arquivo.readline().strip().upper()[0]
                    #LEITURA DO PRIMEIRO CONJUNTO
                    conjunto1 = set(arquivo.readline().strip().split(', '))
                    #LEITURA DO SEGUNDO CONJUNTO
                    conjunto2 = set(arquivo.readline().strip().split(', '))
                    #VERIFICAÇÃO DA OPERAÇÃO ESCOLHIDA
                    if cod_operacao == "U":
                        tipo_operacao = "União"
                        resultado = sorted(conjunto1.union(conjunto2))
                    elif cod_operacao == "I":
                        tipo_operacao = "Intersecção"
                        resultado = sorted(conjunto1.intersection(conjunto2))
                    elif cod_operacao == "D":
                        tipo_operacao = "Diferença"
                        resultado = sorted(conjunto1.difference(conjunto2))
                    elif cod_operacao == "C":
                        tipo_operacao = "Cartesiano"
                        resultado = sorted({(a, b) for a in conjunto1 for b in conjunto2})
                    else:
                        print("A SEGUNDA LINHA DIGITADA NÃO POSSUI OS VALORES CORRETOS")
                        break
                    #PRINT DO RESULTADO DA OPERAÇÃO
                    print("{}: conjunto 1: {}, conjunto 2: {}. Resultado: {}".format(tipo_operacao, conjunto1, conjunto2, resultado))
            else:
                print("A PRIMEIRA LINHA DIGITADA NÃO É UM VALOR CORRETO.")
#ENVIA PARA A FUNÇÃO MAIN
if __name__ == '__main__':
    main()