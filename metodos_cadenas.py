chain1 = "Hola soy jose"
chain2 = "hola machine"
chain3 = "Hola soy una chain Hola"
chain_numeric = "12345 Hola"
print(type(chain1))
""" print(dir(chain1)) """

result = chain1.split()
print(result)
result2 = chain2.startswith("hola")
print(result2)
result3 = chain1.endswith("jose")
print(result3)
result4 = chain3.find("Hola")
print(result4)
result5 = chain3.join("Hola")
print(result5)
result6 = chain3.replace("Hola", "Adios")
print(result6)
result7 = chain3.isnumeric()
print(result7)
result8 = chain_numeric.isnumeric()
print(result8)
result9 = chain_numeric.isalpha()
print(result9)
result10 = chain3.count("Hola")
print(result10)
result11 = len(chain3)
print(result11)
