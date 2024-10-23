

#concatenando dados
def concatenar_strings():
  str1 = input('Digite primeira string: ')
  str2 = input('Digite primeira string: ')

  print(f'{str1} {str2}')

def repetindo_textos():
  str1 = input('Digite uma string: ')
  number1 = int(input('Digite um quantidade de repetições: '))

  for i in range(0, number):
    print(str1)

def basic_math():
  number1 = float(input('Digite um valor numérico: '))
  number2 = float(input('Digite um valor numérico: '))

  if number1 > 0 and number2 > 0:
    print('operações e resultados')
    print(f'soma: {number1 + number2}')
    print(f'subtração: {number1 - number2}')
    print(f'multiplicação: {number1 * number2}')
    print(f'divisão: {number1 / number2}')
  else:
    print('valores precisam ser maior do que zero')
  
