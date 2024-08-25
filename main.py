def main():
    with open('operacoes.txt','r') as file:
        num_operacao = int(file.readline())
        resultados = []
        for _ in range(num_operacao):
            cod_operacao = file.readline().strip()
            conjunto1 = set(file.readline().strip().split(','))
            conjunto2 = set(file.readline().strip().split(','))
            if cod_operacao == "U":
                resultado = conjunto1.union(conjunto2)
            elif cod_operacao == "I":
                resultado = conjunto1.intersection(conjunto2)
            elif cod_operacao == "D":
                resultado = conjunto1.difference(conjunto2)
            elif cod_operacao == "C":
                resultado = {(a, b) for a in conjunto1 for b in conjunto2}
            else:
                resultado = "ERRO"
            resultados.append(resultado)
        print(resultados)

if __name__ == '__main__':
    main()