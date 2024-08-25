def main():
    with open('operacoes.txt','r') as arquivo:
        #DESCOBRIR COMO FAZER VALIDAÇÃO DE TODAS AS LINHAS, PARA SE CASO ENCONTRAR ALGUMA FALHA FAZER UM BREAK E MANDAR REESCREVER O ARQUIVO TXT
        num_operacao = int(arquivo.readline().strip()[0])
        for _ in range(num_operacao):
            cod_operacao = arquivo.readline().strip()[0]
            conjunto1 = set(arquivo.readline().strip().split(', '))
            conjunto2 = set(arquivo.readline().strip().split(', '))
            if cod_operacao == "U":
                operacao = "União"
                resultado = sorted(conjunto1.union(conjunto2))
            elif cod_operacao == "I":
                operacao = "Intersecção"
                resultado = sorted(conjunto1.intersection(conjunto2))
            elif cod_operacao == "D":
                operacao = "Diferença"
                resultado = sorted(conjunto1.difference(conjunto2))
            elif cod_operacao == "C":
                operacao = "Cartesiano"
                resultado = sorted({(a, b) for a in conjunto1 for b in conjunto2})
            else:
                print("ERRO NENHUMA LETRA FOI DIGITADA")
                break
            print("{}: conjunto 1: {}, conjunto 2: {}. Resultado: {}".format(operacao, conjunto1, conjunto2, resultado))

if __name__ == '__main__':
    main()