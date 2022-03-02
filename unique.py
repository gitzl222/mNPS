#coding= utf-8
import sys

filter=sys.argv[1]
result=sys.argv[2]

list=[]
outfile=open(result,'w')
Infile=open(filter,'r').readlines()
#To filter out the best match which have a highest reads identity of unique Subject id and output a XX.result.txt.
for line in Infile:
	linelist=line[:-1].split('\t')
	geneid='\t'.join(linelist[0:2])
	query=linelist[2]
	if query not in list:
		list.append(query)
		outfile.write(line)
	else:
		pass
outfile.close()


