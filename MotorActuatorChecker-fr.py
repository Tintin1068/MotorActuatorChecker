# Définition des constantes
g = 9.81 # Accélération de la pesanteur en m/s²
L = float(input("Course du vérin (en mm) : ")) / 1000
# Course du vérin en m (0.205 pour la version SRT150)
p = 5 # Pas de vis en mm

# Saisie des données par l'utilisateur
m = float(input("Poids du châssis (en kg) : "))
s = float(input("Vitesse de déplacement désirée (en mm/s) : "))
t = 1
mu = 0.01
d = float(input("Distance entre l'axe du moteur et le point d'application de la force (en mm) : "))
n = int(input("Nombre de vérins : "))
k = float(input("Rendement du vérin : "))


a = 2 * s / 1000 / t**2

# Calcul de la force exercée par le vérin
F = k * m * a + mu * k * m * g


# Calcul du couple du moteur
C = F * d / 1000

# Calcul de la vitesse de rotation du moteur
v = s / t / p # Vitesse de déplacement du vérin en m/s
RPM = v * 60 # Vitesse de rotation du moteur en tours par minute

if 4 != n:
    div = 4 / n
    C = F * d / 1000 * div
# Affichage du résultat
print(f"Le couple minimal des moteurs sur les vérins SRT100 est de {C:.2f} N.m")
print(f"La vitesse de rotation maximale des moteurs sur les vérins SRT100 est de {RPM:.2f} tours par minute")

