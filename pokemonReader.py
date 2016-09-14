import csv;
import Pokemon

list= [];

def readData():

    file = open("pokemon.csv",newline="");
    reader = csv.reader(file)

    for row in reader:
        nr = row[0];
        Name = row [1];
        Type1 = row[2];
        Type2 = row[3];
        Total = row [4]
        HP = row[5]
        Attack = row[6]
        Defence = row[7]
        spAtack = row[8]
        spDef = row[9]
        Speed = row[10]
        Generation = row[11]
        Legendary = row[12]


        pokemon = Pokemon.Pokemon(nr,Name,Type1,Type2,Total,HP,
                      Attack,Defence,spAtack,spDef,
                      Speed,Generation,Legendary);
        list.append(pokemon)


    del list[0];

    return list

