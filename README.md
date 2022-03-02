
Speedy carding and keywords extraction of Blastn result files
* The blast.filter.py is used to extract bacterial species names from RefSeq bacterial database which matched to the Query id in Blastn result files firstly and write Subject id, species name, Query id and other informations including % identity, alignment length et al. into XX_py.blast.txt.\
Usage: python blast.filter.py XX.blast.txt bac.name.txt XX_py.blast.txt\
     *the XX.blast.txt is the Blastn result file\
     *grep “>” bac.fasta > bac.name.txt   #preparation of bac.name.txt
* Furthermore, the unique.py is used to filter out the best match which have a highest reads identity of unique Subject id and output XX.result.txt.\
Usage: python unique.py XX_py.blast.txt XX.result.txt
* the XX.result.txt and following command are used to the final statistics of names and number of matched bacterial species reads:\
  cut -f2 XX.result.txt |sort >XX.final.txt\
  cut -f1,2 -d ‘’ XX.final.txt |sort |uniq -c|sort -k 1 -n -r >XX.output





