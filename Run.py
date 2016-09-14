import PokemonReader
import Pokemon

list_pokemons = PokemonReader.readData()

for pokemon in list_pokemons:
    print(pokemon)