# Exercices de POO


#### Le compte bancaire

Écrire un programme python qui permet de définir une classe CompteBancaire(), qui permette d’instancier des objets tels que compte1, compte2, etc. Le constructeur de cette classe initialisera deux attributs d’instance nom et solde, avec les valeurs par défaut ’Dupont’ et 1000.

Trois autres méthodes seront définies :

- depot(somme) permettra d’ajouter une certaine somme au solde ;
- retrait(somme) permettra de retirer une certaine somme du solde ;
- affiche() permettra d’afficher le nom du titulaire et le solde de son compte.


Exemples d’exécution:
```
>>> compte1 = CompteBancaire(‘Duchmol’, 800)
>>> compte1.depot(350)
>>> compte1.retrait(200)
>>> compte1.affiche()
Le solde du compte bancaire de Duchmol est de 950 euros.
>>> compte2 = CompteBancaire()
>>> compte2.depot(25)
>>> compte2.affiche()
Le solde du compte bancaire de Dupont est de 1025 euros.

```


#### La surcharge d'opérateur 

Définir une classe Point avec un constructeur, un point est définit soit par deux coordonnées x et y, s’il s’agit d’une représentation d’un point au plan ou par trois coordonnées x, y et z, s’il s’agit d’une représentation d’un point en espace.

La classe Point doit contenir une méthode ToString qui affiche le point.

Exemple d’exécution:
```
>>>P1=Point(2,3)
>>>P1.ToString()
P(2.00 , 3.00)
>>>P2=Point(1,-5,6)
>>>P2.ToString()
P(1.00 , -5.00 , 6.00)
```


#### L'héritage simple

Définir les classes suivantes:

- Une classe DateNaissance avec trois attributs, jour, mois, année et une méthode ToString qui convertit la date de naissance en chaine de caractères
- Une classe Personne  avec trois attributs, nom, prénom et date de naissance et une méthode polymorphe Afficher pour afficher les données de chaque personne.
- Une classe Employé qui dérive de la classe Personne, avec en plus un attribut Salaire et la redéfinition de la méthode Afficher.
- Une classe Chef qui dérive de la classe Employé, avec en plus un attribut Service et la redéfinition de la méthode Afficher.

Exemple d’exécution:

```
>>>P=personne(“Ilyass”,”Math”,DateNaissance(1,7,1982))
>>>P.afficher()
Nom: Ilyass 
Prénom: Math
Date de naissance: 01 / 07 / 1982

>>>E=employe(“Ilyass”,”Math”,DateNaissance(1,7,1985),7865.548)
>>>E.afficher()
Nom: Ilyass 
Prénom: Math
Date de naissance: 01 / 07 / 1985
Salaire: 7865.55

>>>Ch=chef(“Ilyass”,”Math”,DateNaissance(1,7,1988),7865.548,”Ressource humaine”)
>>>Ch.afficher()
Nom: Ilyass 
Prénom: Math
Date de naissance: 01 / 07 / 1988
Salaire: 7865.55
Service: Ressource humaine
```

#### Le polymorphisme

Une boîtes aux lettres recueille des courrier qui peuvent être des lettres ou des colis.

Une lettre est caractérisée par :

son poids (en grammes)
le mode d’expédition (express ou normal)
son adresse de destination
son adresse d’expédition
son format (“A3” ou “A4”)
Un colis est caractérisé par :

son poids (en grammes)
le mode d’expédition (express ou normal)
son adresse de destination
son adresse d’expédition
son volume (en litres )
Il faut donc définir aussi les deux méthodes:

calculTimbre: qui calcule le prix du Timbre
ToString qui affiche un courrier
Règles pour calculer le prix du Timbre :

en mode d’expédition normal :

Le montant nécessaire pour affranchir une lettre dépend de son format et de son poids : Formule : montant = tarif de base + 1.0 * poids (kilos), où le tarif de base pour une lettre “A4” est de 2.50, et 3.50 pour une lettre “A3”

Le montant nécessaire pour affranchir un colis dépend de son poids et de son volume : Formule : montant = 0.25 volume (litres) + poids (kilos) 1.0

en mode d’expédition express : les montants précédents sont doublés, quelque soit le type de courrier

##### Exemple d’exécution :
```
>>>L1=Lettre(“Lille”,”Paris”,80,”normal”,”A4″)
>>>L1.ToString()
Lettre:
Adresse destination: Lille 
Adress expedition: Paris
Poids: 80.00 grammes
Mode: normal 
Format:A4
Prix du timbre:0.20
>>>C1=Colis(“Marrakeche”,”Barcelone “,3500,”expresse”,2.25)
>>>C1.ToString()
Collis:
Adresse destination: Marrakeche 
Adress expedition: Barcelone 
Poids: 3500.00 grammes
Mode: expresse 
Volume: 2.25 litres
Prix du timbre:3937.50
```