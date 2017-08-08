import dj
import string
import json
import sys
from functools import reduce
from os import path

def strDiff(strA,strB):
	return reduce((lambda diff,(a,b): diff + (not a is b)), zip(list(strA),list(strB)),0)

def findPath(fileName,word1,word2):
	name,ext = path.splitext(fileName)
	word1,word2 = word1.upper(),word2.upper()
	if(path.isfile(name + '.json')):
		graph = json.loads(open(name + ".json","r").read()) # Let's read this json file
	else:
		words = open(name + ".txt","r").read().upper().split() # Let's read and sort this text file
		graph = {word:{neigh:1 for neigh in words if strDiff(word,neigh) is 1} for word in words}
		open(name + ".json","w").write(json.dumps(graph)) # Save the graph for the next time
		
	if(not word1 in graph):
		print word1 + ' is not listed in the file'
	elif(not word2 in graph):
		print word2 + ' is not listed in the file'
	else:
		print '\n'.join(dj.shortestPath(graph,word1,word2)) # Everything cool happens in this line
		
if(len(sys.argv) is 4):
	findPath(sys.argv[1],sys.argv[2],sys.argv[3])
else:
	print "Please provide 3 arguments <file> <word> <word>"