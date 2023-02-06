# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:12:03 2022

Modified on Monday Feb 6 22h 2023

@author: les plus forts : Kilian / Mathis / Victor / Kevin / Vincent / Aymeric /  Timothee / Anthony 
"""
import math

# Programme de Calcul

# Constantes
g=9.80665;    #constante de gravité en m/s2
R=8,31432;    #constante des gaz parfaits en J.K-1
p0=1.292;     #masse volumique de l'air sec à 0°C et pression ambiante en kg/m3
M=28.9644;    #masse molaire de l'air en g/mol
Pa=101325;    #pression ambiante ou pression à l'extérieur en Pa

# Variables
"""
f;            #poussée en newtons (N)
m;            #masse de la fusée en m
S;            #Surface de la fusée


ve;           #vitesse d'éjection des gaz en m/s
qm;           #débit massique en kg/s

A1;           #aire de la section de sortie de la tuyère en m2
P1;           #pression à la sortie de la tuyère en Pa

Cx;           #coefficient de trainee [Pour des MiniFusées, il est courant de prendre un Cx compris entre 0,4 et 0,8, avec 0,6 en moyenne en fonction ]
Cy;           #coefficient de portance []

z;            #hauteur de la fusée (avec 0m le point de départ) en m
t;            #temps depuis le début de lancement en s
v;            #vitesse de l'appareil en m/s
T;            #température à l’altitude donnée exprimée en degré Kelvin [°K]

Vmax;         #vitesse max de la fusée

Sa;           #Surface d'un aileron haut
La;           #Longueur d'un aileron haut
la;           #Largeur d'un aileron haut
ma;           #masse d'un aileron haut
pa;           #masse volumique d'un aileron haut
Ea;           #Epaiseur de l'aileron haut

Sb;           #Surface d'un aileron bas 
Lb;           #Longueur d'un aileron bas
lb;           #Largeur d'un aileron bas
mb;           #masse d'un aileron bas 
pb;           #masse volumique d'un aileron bas
Eb;           #Epaiseur de l'aileron haut

Hc;           #Hauteur de la fusée soit du bati (ici 2 mètres)
Dc;           #Diamètre du bati

Vd;           #Volume du reservoir
pd;           #masse volumique du gaz
Dd;           #Débit du propulseur
Rr;           #Diamètre du reservoir
     

Coeff;        #coefficient aérodynamique
"""
                
# ===== POUSSEE DU MOTEUR =====
def poussee(qm, ve, A1, P1, Pa, T, h):
    return qm*ve + A1*(P1-pression_altitude(Pa, T, h));

# ===== RESISTANCE DE L'AIR =====

def coeficient_frottement_air(Cx,S):
    return p0*Cx*S;


def resistance_aileron():           #Pas encore trouvé
    return 0;

def resistance_bati():              #Pas encore trouvé
    return 0;
    

# Calcul de la pression en fonction de la hauteur
def H(T):
    return M*g/(R*T);

def pression_altitude(Pa, T, z):
    return Pa*math.exp(H(T)*z);

def massevolumique_altitude(delta_h, T):
    return p0*math.exp(delta_h/H(T));       #je n'ai pas trouvé à quoi correspondait delta h (variation de la distance donc ici h delta_h=h-0)

# Calcul de la hauteur
def hauteur(v, t):
    return v*t;

# ===== CALCULS DES FORCES =====

# La force de Portance
def force_portance(Cz, p, v, S):
    return 0.5*Cz*p*S*v**2;

# La force de Trainee
def force_trainee(Cx, p, v, S):
    return 0.5*Cx*p*S*v**2;

def forces_aérodynamiques(Coeff):
    return 1/2* massevolumique_altitude(delta_h, T)*S*Coeff*v**2;                        #Pas encore trouvé

def Pression_Dynamique(Coeff):    
    return forces_aérodynamiques(Coeff)/(Coeff);
 
# ====== PARTIE PARACHUTE ========
def surface_parachute(mp, p, Cx, v):
    return (2*mp*g)/(p*Cx*v**2);

def vitesse_parachute(mp, p, Cx, S):
    return math.sqrt((2*mp*g)/(p*S*Cx))


# ===== POIDS DE LA FUSEE =====

def masse_ailerons_haut(Sa,pa):
    return Sa*pa;

def masse_ailerons_bas(Sb,pb):
    return Sb*pb;

def masse_batie (Hc,Rc):
    return Rc**2*Hc*math.pi;

#On suppose de le reservoir est stocké dans un cylindre de hauteur Hr et de diamètre Dr pouvant contenir le volume initiale Vd
def masse_reservoir(Vd,pd,Dd,t):
    return Vd*pd-Dd*t;
    
def masse_accessoires_capteurs():
    return XXX;

def poids_total(Sa,pa,Sb,pb,Hc,Rc):
    return  masse_ailerons_haut(Sa,pa)+masse_aileronq_bas(Sb,pb)+masse_batie (Hc,Rc+reservoir(Vd,pd,Dd,t));



# ====== CENTRE D'INERTIE ======

#on suppose que les ailerons sont aligné ainsi que la disposition des composants à l'intérieur son equilibré 
#n est en présence de deux plans de symetrie suivant y et z ainsi z et x sont centrés
            

def centre__inertie_bati():
    return (1/12)*masse_batie(Hc,Rc)*(3*(Dc/2)**2+Hc**2);
 
def centre_inertie_ailerons_haut():
    return (Ea*la**3)/12 + masse_ailerons_haut(Sa,pa)*(La/2)**2+(la/2)**2);


def centre_inertie_ailerons_bas():
    return (Eb*lb**3)/12 + masse_ailerons_bas(Sb,pb)*(Lb/2)**2+(lb/2)**2);

    
#On suppose de le reservoir est représenté comme un cylindre de diamiètre Rr
def hauteur_reservoir(Vd,Rr):
      return ((Vd *2)/(math.pi *(Rr/2)^2))

def centre_inertie_reservoir():
    return (1/12)*masse_reservoir(Vd,pd,Dd,t)*(3*(Rr/2)**2+ hauteur_reservoir(Vd,Rr)**2);
    
def centre_intertie_suivant_y():
    return   (1/poids_total(Sa,pa,Sb,pb,Hc,Rc))*(centre__inertie_bati()*masse_batie(Hc,Rc)+centre_inertie_ailerons_haut()*masse_ailerons_haut(Sa,pa)+centre_inertie_ailerons_bas()*masse_ailerons_bas(Sb,pb)+centre_inertie_reservoir()*masse_reservoir(Vd,pd,Dd,t))

def moment_d_inertie():
    return Xxx;




