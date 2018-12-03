import subprocess

print("https://github.com/hanglearning/662finalProject_18f")
print("Welcome to Rongxuan, Yueran and Hang's Graph Coloring Algorithms Mini Benchmark Platform!")
print("This automation script is written for our CISC662 final project, 2018F.")
print("")
print("With great appreciation, algorithms code borrowed and modified from:")
print("https://github.com/bhandaresagar/graph-coloring-radio-problem")
print("https://github.com/brrcrites/graph-coloring ")
print("")
print("Available algorithms for testing:")
print("1 - backtracking")
print("2 - DSATUR")
print("3 - MCS")
print("4 - lmXRLF")
print("5 - Hybrid TabuCol")
print("6 - Hybrid DSATUR")
print("7 - TabuCol")
print("")
print("Available maps to color:")
print("a - Map of Australia")
print("b - Map of USA")
print("c - 100 Nodes, previously generated")
print("d - 300 Nodes, previously generated")
print("e - 400 Nodes, previously generated")
print("f - 500 Nodes, previously generated")
print("g - Randomly generate a new map at your choice of number of nodes")
mapChoice = input("Please indicate the testing map - ")
while mapChoice not in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
	mapChoice = input("Please only input a letter from 'a' to 'g':")

def writeToOtherAlgosMapFile(map_nodes):
	algos = ["dsatur", "hybrid_dsatur", "hybrid_lmxrlf", "lmxrlf", "mcs", "tabucol"]
	for algo in algos:
		# clear code
		open('graph-coloring-algos/Tests/' + algo + '_tests.cpp', 'w').close()
		# start writing
		map_file = open('graph-coloring-algos/Tests/' + algo + '_tests.cpp', "a")
		map_file.write("#include <gtest/gtest.h>")
		if algo == "tabucol":
			map_file.write("\n\n")
			map_file.write("#include <climits>")
		map_file.write("\n\n")
		map_file.write("#include \"../Header/" + algo + ".hpp\"")
		map_file.write("\n\n")
		# snake case to camel case https://stackoverflow.com/questions/19053707/converting-snake-case-to-lower-camel-case-lowercamelcase
		algoCamel = algo.split('_')
		algoCamel = ''.join(x.capitalize() for x in algoCamel)
		map_file.write("using GraphColoring::" + algoCamel + ";")
		map_file.write("\n\n")
		map_file.write("TEST(" + algoCamel + "Tests, " + algoCamel + "K5ColorTest) {")
		map_file.write("\n\n")
		# py append file content to another https://www.sanfoundry.com/python-program-append-contents-file-another/
		nodes_file = open("map-generator/" + map_nodes + "-nodes.txt", "r")
		nodes_file_content = nodes_file.read()
		nodes_file.close()
		map_file.write(nodes_file_content)
		map_file.write("\n\n")
		map_file.write("    " + algoCamel + "* " + algo + " = new " + algoCamel + "(k" + map_nodes + ");")
		map_file.write("\n\n")
		map_file.write("    map<string,int> resultant = " + algo + "->color();")
		map_file.write("\n\n")
		map_file.write("    delete " + algo + ";")
		map_file.write("\n\n")
		map_file.write("}")
		map_file.close()

def ausAndUsa(_choice):

	# backtracking
	# Map of Australia
	if mapChoice == 'a':
		print("1 - Coloring the Map of Australia by backtracking algorithms with 3 colors")
		taskHere = "i=0; while [ $i -lt 5 ]; do python2.7 radio-coloring/Australia/radio.py radio-coloring/Australia/constraints-au; ((i++)); done"
	# Map of USA
	else:
		print("1 - Coloring the Map of USA by backtracking algorithms with 4 colors")
		taskHere = "i=0; while [ $i -lt 5 ]; do python2.7 radio-coloring/USA/radio.py radio-coloring/USA/constraints-usa; ((i++)); done"
	output = subprocess.check_call(taskHere, shell=True)
	showResult = input("Would you like to show the coloring result?(y/n):")
	while showResult not in ['y', 'n']:
		showResult = input("Please only input 'y' or 'n'..")
	if showResult == 'y':
		if mapChoice == 'a':
			with open('radio-coloring/Australia/results.txt', 'r') as fin:
				print (fin.read())
		else:
			with open('radio-coloring/USA/results.txt', 'r') as fin:
				print (fin.read())
		fin.close()

	# execute other algorithms
	# Map of Australia
	if mapChoice == 'a':
		# write to map files for these other algorithms
		print("2 - Coloring the Map of Australia by other algorithms with auto set colors")
		writeToOtherAlgosMapFile("aus")
	# Map of USA
	else:
		print("2 - Coloring the Map of USA by other algorithms with auto set colors")
		writeToOtherAlgosMapFile("usa")
	taskHere = "cd graph-coloring-algos; make; ./color-test"
	output = subprocess.check_call(taskHere, shell=True)


if mapChoice == 'a' or 'b':
	# Map of Australia or USA
	
	# execute algorithms
	ausAndUsa(mapChoice)



