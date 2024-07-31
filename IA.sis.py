#Colocar os filmes
filmes = {
    "Drama": ["O Poderoso Chefão", "Os Intocáveis", "Forrest Gump"],
    "Comédia": ["Meninas Malvadas", "Se Beber, Não Case!"],
    "Ficção Científica": ["Star Wars", "Matrix", "De Volta para o Futuro", "Guardiões da Galáxia"],
    "Romance": ["Titanic", "A Culpa é das Estrelas", "La La Land"]
}
    
  # Variável para armazenar o nome do filme gostado
filme_gostado = input("Digite o nome do filme que você gostou: ")  

# Variável para armazenar o gênero do filme
genero_encontrado = None

# Procura o filme na lista de filmes
for genero, lista_filmes in filmes.items():
    if filme_gostado in lista_filmes:
        genero_encontrado = genero
        break

# Recomenda filmes do mesmo gênero
if genero_encontrado:
    recomendacoes = [filme for filme in filmes[genero_encontrado] if filme != filme_gostado]
    print("Filmes recomendados do gênero", genero_encontrado, ":", recomendacoes)
else:
    print("Filme não encontrado na base de dados.")






