diccionario = {
"CRINGE": "Algo excepcionalmente raro o embarazoso",
"LOL": "Una respuesta común a algo gracioso",
"ROFL": "ROFL se utiliza como reacción a algo gracioso, similar a LOL"
"XD": "Una reacció a algo extraño o que causo much gracia" 
}

word = input("Escribe una palabra moderna que no entiendas (¡utiliza mayúsculas!):")

# .values()
if word in diccionario.keys():
print(diccionario[word])
else:
print("Todavía no tenemos esta palabra... Pero estamos trabajando en ella.")
