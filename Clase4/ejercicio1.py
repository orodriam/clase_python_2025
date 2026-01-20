nombres = ["Oscar", "Ivan", "Rodriguez", "Amado"]

for palabra in nombres:
    print("\n", palabra.lower(), ",")
    
    letras = []
    for i, letra in enumerate(palabra):
        if i == 2:  #posicion de la mayuscula 
            letras.append(letra.upper())
        else:
            letras.append(letra.lower())
    
    print(", ".join(letras))
