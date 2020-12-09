- 1- Créer un script `sum.sh` qui prend 2 variables a(=20) et b(=30) et affiche une varibale  sum=a+b
- 2- Créer un script `nameUser.sh ` qui afficher le nom de l'utilisateur ainsi que la date du jour. Le script devra demander le nom à l'utilisateur et qui l'écrit dans la console
- 3- Créer un script `compt.sh ` qui affiche une variable count (compteur) qui s'incrémente et s'arrète au chiffre 5
- 4- Créer un script `for.sh` qui affiche les chiffre de 10 à 1 sur une ligne à l'aide d'une boucle for 
- 5- Créer un script `if.sh` qui demande un nombre à l'utilisateur et indique si c'est un nombre à 1, 2 ou 3 chiffres 
- 6- Créer un script `cmd.sh` qui demande deux arguments (X et Y)  à l'utilisateur, qui les lis et affiche la somme dans l'interface de commande 
- 7- Créer un dossier test et un script `dir.sh` qui affiche les dossiers dans le repertoire 
- 8- Créer un nouveau fichier txt (non vide) et créer un script `lines.sh` qui itère dans votre répertoire et affiche seulement les fichiers et compte le nombre de lignes et de mots de chacun des fichiers. Afficher seulement les fichier non vides
- Se renseigner sur le fichier `.bashrc` sur votre VM, éditez le avec un alias (si vous ne savez pas ce que c'est renseignez vous sur les alias)
- Faite un alias sur votre machine pour accéder à votre VM 
- Faire une fonction `gitacp()` qui prend en entrée un message de plusieurs mots sous forme de string et qui effectue un push sur un repo git avec les commandes usuelles de git (add, commit et push)








for F in *
do
      if [[ $F -gt 0 ]]
      then
            echo "ligne : " `wc -l $F`
            echo "mot :" `wc -w $F`
      fi
done