
#readFile.py

import csv

print("")
print("readFile.py Start --------------------  ")
print("")

filename = "readFile_data.txt"

def readTxt(filename):
	with open (filename,"r",encoding="utf-8") as f:
		txt=f.read()
	return txt 

data=readTxt(filename)
print("readTxt:data=",data)
print("")

def readCsv(filename):
	with open (filename,"r",encoding="utf-8",newline="") as f:
		reader=csv.reader(f,delimiter="\t")
		L = []
		for _ in reader:
			L.append(_)
	return L

data=readCsv(filename)
print("readCsv:data=",data)
print("")

print("readFile.py End --------------------  ")
print("")
