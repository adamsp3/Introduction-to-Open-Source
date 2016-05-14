from networkx import *
import re,sys,gzip

def distance(a, b):
	if (len(a) != len(b)):
		return 1
	d = 0
	for i in range(0, len(a)):
		try:
			j = b.index(a[i])
			b = b[:j] + b[j+1:]
		except:
			d += 1

	return d


def words_graph(filename, wordlen):
	f = open(filename, 'r')
	mygraph = Graph(name = "words")
	for line in f.readlines():
		if not (line.startswith('*')):
			w = line[0:wordlen]
			mygraph.add_node(w)
	num = number_of_nodes(mygraph)
	words = mygraph.nodes()
	for i in (0, len(words)):
		if (i < len(words) -1 and distance(words[i], words[i+1]) == 1):
			mygraph.add_edge(words[i], words[i+1])
	return mygraph

if __name__ == '__main__':
	from networkx import *
	five = words_graph("words_dat.txt", 5)
	four = words_graph("words4.dat", 4)
	sp = shortest_path(five, 'chaos', 'order')
	print "shortest path between 'chaos' and 'order' is:\n", sp
	sp=shortest_path(five, 'nodes', 'graph')
	print "shortest path between 'nodes' and 'graph' is:\n", sp
	sp=shortest_path(five, 'pound', 'marks')
	print "shortest path between 'pound' and 'marks' is:\n", sp
	sp = shortest_path(four, 'cold', 'warm')
	print "shortest path between 'chaos' and 'order' is:\n", sp
	sp=shortest_path(four, 'love', 'hate')
	print "shortest path between 'nodes' and 'graph' is:\n", sp






