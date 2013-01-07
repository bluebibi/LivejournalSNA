import networkx as net
import urllib
import matplotlib.pyplot as plt

def read_lj_friends(g, name):
  response = urllib.urlopen('http://www.livejournal.com/misc/fdata.bml?user=' + name)
	for line in response.readlines():
		print line
		if line.startswith('#'): continue
		parts = line.split()
		if len(parts)!=2 : continue
		
		if parts[0] == '<':
			g.add_edge(parts[1], name)
		else:
			g.add_edge(name, parts[1])

def snowball_sampling(g, center, max_depth=2, current_depth=0, sample_list=[]):
	print center, current_depth, max_depth, sample_list
	if current_depth==max_depth:
		print 'out of depth'
		return sample_list
	if center in sample_list:
		return sample_list
	else:
		sample_list.append(center)
		read_lj_friends(g, center)
		for node in g.neighbors(center):
			sample_list=snowball_sampling(g, node, max_depth=max_depth, current_depth=current_depth+1, sample_list=sample_list)
	return sample_list

g = net.Graph()
#read_lj_friends(g, 'valerois')

#g.number_of_nodes()
#snowball_sampling(g, 'valerois')
#net.draw(g)
#plt.show()
