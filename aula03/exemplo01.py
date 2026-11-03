atual = float(input('Digite seu salario atual: '))
percentual = float(input('Digite a % de aumento salarial: '))
percentual = percentual/100

aumento_salario = .15
valor_aumento = atual * percentual
novo_salario = atual + valor_aumento

print(f'Seu novo salario será R$ {novo_salario:.2f}')
print(f'O valor do seu reajuste foi de {valor_aumento:.2f}')