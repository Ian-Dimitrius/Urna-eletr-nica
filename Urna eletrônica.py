print("==Urna eletrônica==")

candidato1 = 0
candidato2 = 0
candidato3 = 0
nulo = 0

voto = float(input("Digite o número do seu candidato:"))

if voto == 22:
    candidato1 += 1
    print("Você votou no candidato 1")

elif voto == 44:
    candidato2 += 1
    print("Você votou no candidato 2")
  

elif voto == 66:
    candidato3 += 1 
    print("Você votou no candidato 3")

elif voto == 0:
    nulo += 1 
    print("Você votou nulo")

elif voto !=22 and voto != 44 and voto != 66 and voto != 0:
    print("Voto inválido")

print("Resultado da votação:")
print(" Votos candidato 1:", candidato1)
print("Votos candidato 2:", candidato2)
print("Votos candidato 3:", candidato3)
print("Votos nulos:", nulo)

