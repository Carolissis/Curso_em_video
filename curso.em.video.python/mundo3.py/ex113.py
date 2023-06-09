def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro valido\033[m)')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferio não digitar esse número\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número real valido\033[m)')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferio não digitar esse número\033[m')
            return 0
        else:
            return n

inteiro = leiaint('Digite um número inteiro: ')
real = leiafloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')