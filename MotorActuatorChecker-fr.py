g = 9.81
L = float(input("Course du vérin (en mm) : ")) / 1000
p = 5 
m = float(input("Poids du châssis (en kg) : "))
s = float(input("Vitesse de déplacement maximale désirée (en mm/s) : "))
t = 1
mu = 0.01
L = float(input("Course du vérin (en mm) : ")) / 1000
n = int(input("Nombre de vérins : "))
k = 0.8

if n == 1:
    d = 100
else:
    if n == 2:
        d = 55
    else:
        if n == 3:
            d = 35
        else:
            if n == 4:
                d = 25
            else:
                if n == 5:
                    d = 20
                else:
                    if n == 6:
                        d = 16.6666
                    else:
                        if n == 7:
                            d = 14.2857
                        else:
                            if n == 8:
                                d = 12.5
                            else:
                                if n > 8:
                                    print("Le nombre de vérins ne peut pas dépasser 8.")
                                    d = 0

a = 2 * s / 1000 / t**2
F = k * m * a + mu * k * m * g
C = F * d / 1000
v = s / t / p
RPM = v * 60
div = 4 / n
C = F * d / 1000 * div
print(f"Le couple minimal des moteurs sur les vérins SRT100 est de {C:.2f} N.m")
print(f"La vitesse de rotation maximale des moteurs est de {RPM:.2f} tours par minute.")
