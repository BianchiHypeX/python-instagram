# atenção sinta-se livre para utilizar isso da forma que preferir e fazer modificações.
# instagram: @cake.js

# se quiser respostas além do 'Sim' 'Não' basta digitar dentro do answers na linha 9, mas lembre-se de por 'resposta',
# exemplo: answers = ['Sim', 'Não', 'Claro', 'Não!']

from random import choice

answers = ['Sim', 'Não']

while True:
    
    question = input("Sua mensagem: ")

    if question.isalpha() != True and not ' ' in question:
        print('erro')
        continue
    
    else:
        print(choice(answers))
        continue
        
# caso for reproduzir isso em um video ou tutorial, dê os créditos
# feito com ❤ por bianchi
