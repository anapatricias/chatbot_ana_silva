import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #    return 'Olá tudo bem!'
    # if comando == 'como estás':
    #    return 'Estou bem, obrigado!'
    # if comando == 'como te chamas?':
     #   return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #    return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #    return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #    return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #    return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
         ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',

    # novos comentários 
    ('qual é o teu nome', 'qual o teu nome', 'como te chamas'): 'O meu nome é Bot!',
    ('quantos anos tens', 'qual a tua idade'): 'Sou muito jovem',
    ('meteorologia em portugal', 'tempo em portugal', 'clima em portugal'): 'Está muito calor!',
    ('preferes este tempo ou o inverno', 'gosta mais do verão ou do inverno'): 'Gosto mais deste tempo, mas é demasiado calor',
    ('como gostas de passar o tempo', 'o que gostas de fazer'): 'Gosto muito de ler e aprender coisas novas',
    ('que tipo de livros gostas', 'quais os teus livros favoritos'): 'Um pouco de tudo! Mas os meus favoritos são romances históricos',
    ('qual o último livro que leste', 'último livro que leste'): 'No tempos das cerejas, sobre uma Lisboa após a segunda guerra mundial',
    ('qual é o próximo livro', 'próximo livro que vais ler'): 'Vou começar um sobre a Ucrânia no tempo da União Soviética',
    ('como é bom viajar sem sair do lugar', 'viajar sem sair do lugar'): 'Sim! Melhor sensação do mundo',
    ('espero que continues sempre a ler', 'continue a ler'): 'Eu também! Obrigado',
}

          

    for chave, resposta in respostas.items():
             for frase in chave:
                 if frase in comando:
                     return resposta
            
    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()