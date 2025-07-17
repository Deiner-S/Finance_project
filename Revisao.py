
"""Manipulação de lista"""
frutas = ['maçã', 'banana', 'laranja']
frutas.append("append")
print(frutas)
frutas.insert(1,"insert")
print(frutas)
frutas.pop()
print(frutas)
frutas.remove("insert")
print(frutas)
frutas.sort()
print(frutas)
lista2 = ["uva","abacaxi","amecha"]
frutas.extend(lista2)
print(frutas)
what = frutas[frutas.index("uva")]
print(what)

"""Iterando lista de formas diversas"""

for i in frutas:
    print(f"{i}")

for i in range(len(frutas)):
    print(frutas[i])


"""Comprehension
Sempre retorna a mesma estrutura a qual está sendo aplicado
extrutura básica: resultado / iteração / condição(opcional)
"""
print([result[::-1] for result in frutas])

print([result for result in frutas if result.lower().startswith("a")])




