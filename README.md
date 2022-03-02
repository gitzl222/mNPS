* Speedy carding and keywords extraction of Blastn result files\
For extracting bacteria name of each blast hit,\
run the blast.filter.py by Python in Nanoporefastareadsfile;\
For keeping the best blast hit of each reads,\
run the unique.py by Python in the same directory.


* Speedy carding and keywords extraction of Blastn result files\
The blast.filter.py is used to extract bacterial species names from RefSeq bacterial database which matched to the Query id in Blastn result files firstly and write Subject id, species name, Query id and other informations including % identity, alignment length et al. into XX_py.blast.txt.,\ 
Usage: python blast.filter.py XX.blast.txt bac.name.txt XX_py.blast.txt,\
grep “>” bac.fasta > bac.name.txt #preparation of bac.name.txt,\
Furthermore, the unique.py is used to filter out the best match which have a highest reads identity of unique Subject id and output XX.result.txt.,\
Usage: python unique.py XX_py.blast.txt XX.result.txt,\
Both the scripts should be performed in Nanoporefastareadsfile.



