for F in $(ls)
do
    if [[ -f $F ]]
    then
    if [[ -s $F ]]
    then
        echo "FICHIER " $F
        echo "LIGNE :" `wc -l < $F`
        echo "MOT :" `wc -w < $F`
        echo ""
    fi
    fi
done