# programme de suppression de l'intru

intru_1 = input("Nom de l'intru 1 : ")
score_1 = int(input("Score de l'intru 1 : "))
intru_2 = input("Nom de l'intru 2 : ")
score_2 = int(input("Score de l'intru 2 : "))

response = "Le nom de l'intru est : "
if score_1>score_2:
    response+=intru_2
else:
    response+=intru_1
print(response)