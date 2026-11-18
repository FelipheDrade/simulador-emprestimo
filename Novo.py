from time import sleep
print ('Vamos fazer o seu empretismo bancario para comprar uma casa')
sleep (1.5)
casa = float(input('Qual o valor da casa que voce deseja comprar?R$'))
sleep (0.5)
salario = float(input('Qual o seu salario Mensal?:'))
sleep (0.5)
meses = int(input('Em quantos meses voce deseja pagar?:'))
limite = casa / meses
prestaçao = salario * 0.30
if limite < prestaçao:
    print ('O seu empretismo foi \033[32maprovado!!!')
elif limite > prestaçao:
    print('O seu emprestimo foi \033[31mnegado!!!')
else:
    print ('O seu emprestimo vai entrar em analise')
print ('O valor mensal das parcelas, foram de R$',limite,", e a sua prestação é de", prestaçao, )
