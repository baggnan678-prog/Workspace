temperatures = [30, 32, 35, 33, 31, 29, 28]
jours = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")

"""temperatures= []
for i in range(7):
    nombre=(int(input('Entré une température ')))
    while nombre<-20 or nombre>60:
        print("Veuillez ressayer, la temperature doit etre entre -20 et 60")
        nombre=(int(input('Entré une température ')))
    temperatures.append(nombre)"""
print("1. Température du mercredi :", temperatures[2], "°C")

print("2. Température maximale :", max(temperatures), "°C")
print("   Température minimale :", min(temperatures), "°C")

moyenne = sum(temperatures) / len(temperatures)
print(f"3. Moyenne des températures : {moyenne:.2f} °C")

print("4. Jours où la température dépasse 32°C :")
for i in range(len(jours)):
    if temperatures[i] > 32:
        print("  -", jours[i], ":", temperatures[i], "°C")
print("5. Températures par jour :")
for jour, temp in zip(jours, temperatures):
    print(f"   {jour} : {temp}°C")