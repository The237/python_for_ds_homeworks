# limites pour X
LIM_INF_X = 0
LIM_SUP_X = 47

# Limites pour Y
LIM_INF_Y = 0
LIM_SUP_Y = 19


vehicle_x = int(input("Position initiale x du véhicule : "))
if vehicle_x < LIM_INF_X or vehicle_x > LIM_SUP_X:
    print("Le point de destination X donné est hors de la carte : ")

vehicle_y = int(input("Position initiale y du véhicule : "))
if vehicle_y < LIM_INF_Y or vehicle_y > LIM_SUP_Y:
    print("Le point de destination Y donné est hors de la carte : ")

point_x = int(input("Position x du point de distribution : "))
if point_x < LIM_INF_X or point_x > LIM_SUP_X:
    print("Le point de distribution X donné est hors de la carte : ")

point_y = int(input("Position y du point de distribution : "))
if point_y < LIM_INF_Y or point_y > LIM_SUP_Y:
    print("Le point de distribution Y donné est hors de la carte : ")

chemin = []
while point_x != vehicle_x or point_y != vehicle_y:
    direction = input("Veuillez choisir la direction : ")
    if direction == "N":
        vehicle_y -= 1
    elif direction == "NE":
        vehicle_x += 1
        vehicle_y -= 1
    elif direction == "E":
        vehicle_x += 1
    elif direction == "SE":
        vehicle_x += 1
        vehicle_y += 1
    elif direction == "S":
        vehicle_y += 1
    elif direction == "SO":
        vehicle_x -= 1
        vehicle_y += 1
    elif direction == "O":
        vehicle_x -= 1
    elif direction == "NO":
        vehicle_x -= 1
        vehicle_y -= 1
    chemin.append(direction)

print(chemin)
