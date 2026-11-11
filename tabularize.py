#!/usr/bin/env python3
'''
	USEAGE

	./tabularize.py data.csv

		creates data.tex
'''
from sys import argv,exit
argc=len(argv)

type='long'
dlm=',' # csv delimiter

if argc != 2:
	print("PLEASE PROVIDE EXACTLY 1 COMMAND LINE ARGUMENT")
	exit(-1)

fin=argv[1]
root=fin.split('.')[0]
fout=root+'.tex'

text=''
text=text+"\\toprule\n"

n_words=0
with open(fin,'r') as IN:
	tin=IN.read()
with open(fout,'w') as OUT:
	for line in tin.split('\n'):
		n=len(line.split(dlm))
		if n<=1: continue
		# text=text+'\\\\'+'\n'
		if n > n_words:
			n_words = n
		# print(line.split(dlm))
		for i,word in enumerate(line.split(dlm)):
			text=text+word+'\t'
			if i < n-1:
				text=text+'& '
		text = text + '\\\\\n'
	text=text+'\n\\bottomrule\n'
	if type=='long':
		text=text+'\\end{longtable}\n'	
	else:
		text=text+'\\end{tabular}\n'	
	lcr=''
	for i in range(n_words):
		lcr=lcr+'c'

	if type=='long':
		text="\\begin{longtable}{"+lcr+"}\n" + text
	else:
		text="\\begin{tabular}{"+lcr+"}\n" + text
	OUT.write(text)
