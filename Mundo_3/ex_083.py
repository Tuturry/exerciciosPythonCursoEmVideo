# Crie um programa onde o usuário digite uma expressão qualquer que
# use parênteses. Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []

for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            # Remover o último elemento da pilha.
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está incorreta.')
    