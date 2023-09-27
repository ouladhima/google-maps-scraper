liste_ville = open("liste_villes.txt" , 'r' , encoding='utf-8')
liste_ville = [x.replace('\n','') for x in liste_ville.readlines()]

queries = []
for el in liste_ville[0:5]:
    SingleQuery = {"keyword" : f"Ecole supérieur en {el}",
                   "max_results" : 5}
    queries.append(SingleQuery)
    

queries = queries

# queries = [
#     {
#         "keyword": "Ecole supérieur en ile-de-France  ",
#         "max_results" : 50,
#     },
# ]

number_of_scrapers = 12