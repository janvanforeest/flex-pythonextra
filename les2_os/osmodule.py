import os

mapnaam = input("Welke naam wil je voor de map? ")

lengte_mapnaam = 0

while lengte_mapnaam == 0:
    mapnaam = input("Welke naam wil je voor de map? ")

    lengte_mapnaam = len(mapnaam)
    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)
        print("De map " + mapnaam + " is gemaakt.")
    else:
        print("Je hebt geen naam ingevoerd")