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
          'qual é o teu nome?':'O meu nome é Bot!', 
          'quantos anos tens?': 'Sou muito jovem',
          'como está a meteorologia em Portugal nos últimos dias?':'Está muito calor!',
          'preferes este tempo ou o inverno?':'gosto mais deste tempo, mas é demasiado calor',
          'como gostas de passar o tempo?':'gosto muito de ler e aprender coisas novas',
          'que tipo de livros gostas?':'um pouco de tudo! mas os meus favoritos são romances históricos',
          'qual o último livro que leste?':'No tempos das cerejas, sobre uma Lisboa após a segunda guerra mundial',
          'e o próximo?':'vou começar um sobre a Ucrânia no tempo da União Soviética',
          'como é bom viajarmos para outros países e tempos sem sair do lugar, não achas?':'sim! melhor sensação do mundo',
          'espero que continues sempre a ler!':'eu também!obrigado',
          
    }

    for chave, resposta in respostas.items():
         if isinstance(chave, tuple):
            if comando in chave:
                 return resposta
    else: 
         if chave in comando:
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