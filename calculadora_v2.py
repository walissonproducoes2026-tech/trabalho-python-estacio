saida = ''
def adicao(num1, num2): 
            return num1 + num2

def subracao(num1, num2): 
            return num1 - num2

def multiplicao(num1, num2): 
            return num1 * num2

def divisao(num1, num2): 
            if num2 == 0:
                return 'Não foi possível realizar a divisão por 0'
            else:
                return num1 / num2
            return resultado
def calculadora(num1, num2, operacao):
            if operacao == '+' or operacao.lower() == 'soma':
                resultado = adicao(num1, num2)

            elif operacao == '-' or operacao.lower() == 'subracao':
                resultado = subracao(num1,num2)

            elif operacao == '*' or operacao.lower() == 'multiplicacao':
                resultado = multiplicao(num1,num2)

            elif operacao == '/' or operacao.lower() == 'divisão':
                resultado = divisao(num1,num2)

            else:
                resultado='Operação Invalída!'

            return resultado

while saida.lower() != 'n':   
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao_escolhida = input('Digite a operação (+, -, \*, / ou nome): ')
    resultado = calculadora(num1, num2, operacao_escolhida)
    print('Resultado da operação: ', resultado)
    saida = input('Deseja continuar? (S/N): ')