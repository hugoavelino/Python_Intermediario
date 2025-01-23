# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_certas = 0


for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}\n")

    for index, opcao in enumerate(pergunta["Opções"]):
        print(f'{index}. {opcao}')
    print()

    resposta=input('Digite a resposta certa ')
    if resposta.isdigit():
        resposta_int = int(resposta)
        if resposta_int >= len(pergunta['Opções']):
            print("Digite um número entre 0 e 3 seu burro, errou de bobeira! ")
            continue
    else:
        print("Digite um número válido")
        continue
        
    if pergunta['Opções'][resposta_int] == pergunta['Resposta']:
        respostas_certas+= 1
        print('Você acertou parabéns! ')
    
        
        
print(f'Você acertou um total de {respostas_certas} perguntas.')

