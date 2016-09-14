class Pokemon:

    def __init__(self, name, life):
        self.name = name
        self.life = life

p = Pokemon("Pickachu", 100)

print(p.life)
print(p.name)