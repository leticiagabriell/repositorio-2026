#sem dicionario 
matricula = 2026001
name1= "ana silva"
telefone1 = "9999-8888"

#com dicionario
aluno = {
    "marricula":2026001,
    "nome":"Ana silva",
    "telefone":"9999-8888"
}

print(aluno)

contato = {
    "@camilaqueiroz" : "camila queiros",
    "@brumamarquezine" : "Bruna m.",
    "@sheromenezes" : "sheron m.",
    "@paolaoliveira" : "paola o.",
    "@joao:":"joao.o"
}

print(contato)
print(type(contato))

#acesso direto
print(contato["@camilaqueiroz"])

# acesso seguro com get()
print(contato.get( "@paolaoliveira"))
print(contato.get( "@inexistente"))
print(contato.get( "@inexistente", "nao incontrado"))

#add novo elemento
contato ["@giovanna"] = "Giovanna"
print("Apos add:",contato)

#atualiza elemento exitencia
contato ["@paolaoliveira"] = "Paola olaveira"
print("Apois add:",contato)

contato.update({
    "@brumamarquezine":"Bruna marquezine",
    "@brumamarquezine": "Camila Q."
})

print("apos atualizaçao:",contato)

#remove e retorna 
removido = contato.pop("@paolaoliveira")
print(f"Removido: {removido}")
print("Apois o pop:",contato)


#del remove sem retornar
del contato["@camilaqueiroz"]
print("Apos o del:",contato)

#esvaziar tudo 
copia = dict(contato)
contato.clear()
print("Apos clear:",contato)
print("copia:",copia)

print("numero de contato:",len(contato)) #tamanho do dicionario


#virificar existencia
if "@joao" in contato:
    print(f"Encontrado:{contato['@joao']}")

if "@inexistente" in contato:
    print("existe")
else:
    print("nao existe")
    