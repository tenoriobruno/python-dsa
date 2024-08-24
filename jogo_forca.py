import random
from unidecode import unidecode

def print_forca(tentativas):
    stages = [
        '''
           --------
           |      |
           |      
           |      
           |      
           |      
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      
           |      
        ''',
        '''
           --------
           |      |
           |      O
           |     /|
           |      
           |      
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      
           |      
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |      
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |      
        '''
    ]
    print(stages[5 - tentativas])

frutas = ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza",
    "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Goiânia",
    "Belém", "Porto Alegre", "Guarulhos", "Campinas", "São Luís",
    "São Gonçalo", "Maceió", "Duque de Caxias", "Campo Grande", "Natal",
    "Teresina", "São Bernardo do Campo", "Nova Iguaçu", "João Pessoa", "Santo André",
    "São José dos Campos", "Jaboatão dos Guararapes", "Ribeirão Preto", "Osasco", "Uberlândia",
    "Feira de Santana", "Sorocaba", "Niterói", "Cuiabá", "Aracaju",
    "Juiz de Fora", "Joinville", "Londrina", "Belford Roxo", "Santos",
    "Ananindeua", "Campos dos Goytacazes", "Mauá", "Carapicuíba", "Olinda",
    "Caxias do Sul", "São João de Meriti", "Resende", "Vila Velha", "Serra",
    "Taubaté", "Volta Redonda", "Betim", "Governador Valadares", "Cariacica",
    "Mogi das Cruzes", "Petrópolis", "Uberaba", "Pelotas", "Caucaia",
    "Ponta Grossa", "Itaquaquecetuba", "Rio Branco", "Cascavel", "Novo Hamburgo",
    "Vitória da Conquista", "Barueri", "Franca", "Praia Grande", "Blumenau",
    "Paulista", "Limeira", "Diadema", "Juazeiro do Norte", "São José do Rio Preto",
    "Macapá", "Colombo", "Santarém", "São Vicente", "Marília",
    "Boa Vista", "Porto Velho", "Florianópolis", "São José dos Pinhais", "Piracicaba",
    "Canoas", "Foz do Iguaçu", "Viamão", "Maringá", "Montes Claros",
    "Jundiaí", "Rio Verde", "Anápolis", "Caxias", "Praia Grande"]
frutas = [fruta.upper() for fruta in frutas]
frutas = [unidecode(fruta) for fruta in frutas]
indice_escolhido = random.randint(0, len(frutas) - 1)
palavra_forca = frutas[indice_escolhido]
tentativas = 5
letras_erradas = []
tamanho_palavra = len(palavra_forca) - palavra_forca.count(" ") 
letras_descobertas = []

print(f"Jogo da forca. É uma cidade com {tamanho_palavra} letras.")
for letra in palavra_forca:
    if letra == " ":
        letras_descobertas.append(" ")
    else:
        letras_descobertas.append("_")

print(" ".join([letra for letra in letras_descobertas]))
print_forca(tentativas)

while tentativas >= 1:   
    letra_digitada = input("\nDigite uma letra: ").upper()
    if letra_digitada not in palavra_forca:
        tentativas -= 1
        letras_erradas.append(letra_digitada)
        print_forca(tentativas)
    else:
        i = 0
        for letra in palavra_forca:
            if letra_digitada == letra:
                letras_descobertas[i] = letra_digitada
            i += 1
    print(f"Letras já descobertas: ", end="")
    print(" ".join([letra for letra in letras_descobertas]))
    if "".join(letras_descobertas) == palavra_forca:
        print(f"\nParabéns!!! Você ganhou!!! :D A cidade é {palavra_forca}")
        break
    if tentativas == 0:
        print(f"\nVocê perdeu! :/ A cidade é {palavra_forca}")
        break
    print (f"{tentativas} Tentativas restantes")
    print(f"Letras já erradas: ", end="")
    for letra in letras_erradas:
            print(letra, end=" ")
    print("")   