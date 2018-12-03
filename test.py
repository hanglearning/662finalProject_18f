# Hang Chen
# Yueran Zhang
# Rongxuan Hu

# 2018F UD CISC662 Final Project main py

import os, os.path
import subprocess
import sys

# git clone google test files for the first run
if len([name for name in os.listdir('graph-coloring-algos/googletest') if os.path.isfile(name)]) == 0:
	taskHere = "cd graph-coloring-algos; git clone https://github.com/abseil/googletest.git"
	FNULL = open(os.devnull, 'w')
	retcode = subprocess.call(taskHere, stdout=FNULL, stderr=subprocess.STDOUT)

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
		nodes_file = ''
		if mapChoice != 'g':
			nodes_file = open("map-generator/" + str(map_nodes) + "nodes.txt", "r")
		else:
			nodes_file = open("map-generator/newMap/" + str(map_nodes) + "nodes.txt", "r")
		nodes_file_content = nodes_file.read()
		nodes_file.close()
		map_file.write(nodes_file_content)
		map_file.write("\n\n")
		map_file.write("    " + algoCamel + "* " + algo + " = new " + algoCamel + "(k" + str(map_nodes) + ");")
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
	showColoringResults()

	# execute other algorithms
	# Map of Australia
	if mapChoice == 'a':
		# write to map files for these other algorithms
		print("2 - Coloring the Map of Australia by other algorithms with auto set colors\n")
		writeToOtherAlgosMapFile("aus")
	# Map of USA
	else:
		print("2 - Coloring the Map of USA by other algorithms with auto set colors\n")
		writeToOtherAlgosMapFile("usa")
	taskHere = "cd graph-coloring-algos; make; ./color-test"
	output = subprocess.check_call(taskHere, shell=True)

def showColoringResults():
	showResult = input("Would you like to show the coloring result?(y/n):")
	while showResult not in ['y', 'n']:
		showResult = input("Please only input 'y' or 'n'..")
	print()
	if showResult == 'y':
		if mapChoice == 'a':
			with open('radio-coloring/Australia/results.txt', 'r') as fin:
				print (fin.read())
		elif mapChoice == 'b':
			with open('radio-coloring/USA/results.txt', 'r') as fin:
				print (fin.read())
		else:
			with open('radio-coloring/UserDIY/results.txt', 'r') as fin:
				print (fin.read())
		fin.close()
	print()

def regeneratePythonScript(numOfNodes, numOfColors):
	# regenerate new python scirpt
	# replace text content for specific lines in a text file https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
	with open('radio-coloring/UserDIY/radio.py', 'r') as file:
	    data = file.readlines()
	# line 17 and 140 replace number of colors
	newColorList = []
	for i in range(1, numOfColors + 1):
		newColorList.append(str(i))
	data[16] = "        self.bands = ['"
	data[139] = "    domains = {state: ['"
	for j in range(0, len(newColorList)):
		if j != numOfColors - 1:
			data[16] += (newColorList[j] + "', '")
			data[139] += (newColorList[j] + "', '")
		else:
			data[16] += (newColorList[j] + "']\n")
			data[139] += (newColorList[j] + "'] for state in solver.states}\n")
	# line 124 replace map file location
	if numOfNodes != 2:
		if mapChoice == 'g':
			data[123] = "    filename = \"map-generator/newMap/" + str(numOfNodes) + "nodes_radio.txt\"\n"
		else:
			data[123] = "    filename = \"map-generator/" + str(numOfNodes) + "nodes_radio.txt\"\n"
	else:
		if neighbourOrSep == 'n':
			data[123] = "    filename = \"map-generator/2nodes_radio.txt\"\n"
		else:
			data[123] = "    filename = \"map-generator/2nodes_radio_separate.txt\"\n"
	# write the script back
	with open('radio-coloring/UserDIY/radio.py', 'w') as file:
	    file.writelines(data)
	file.close()


if mapChoice == 'a' or mapChoice == 'b':
	# Map of Australia or USA
	
	# execute algorithms
	ausAndUsa(mapChoice)

else:
	# ask for the number of colors input
	# print("How many colors do you want to test backtracking algorithm? (Color number is smartly assigned by other algorithms)")
	print("How many colors do you want?")
	while True:
		try:
			numOfColors = int(input("Must be a positive int: "))
			break
		except ValueError:
		   print("A positive int is an integer in [1, ∞]")

	# ask for the number of nodes input
	if mapChoice == 'g':
		# print("How many nodes do you want to be filled in the map for the map to be colored?")
		print("====================")
		print("Note: for simplicity of code and testing purpose, we have dropped the support of less than 5 nodes.")
		print("====================")
		print("How many nodes do you want?")
		while True:
			try:
				numOfNodes = int(input("Must be a larger than 4 int: "))
				while numOfNodes < 5:
					numOfNodes = int(input("A larger than 4 positive int is an integer in [5, ∞]: "))
				break
			except ValueError:
			   continue

		# determine coloring map
		if numOfNodes == 2:
			# will use the only two possible existing maps for 2 nodes
			neighbourOrSep = input("Would you like the two nodes be neighbours or separate?(n/s):")
			while neighbourOrSep not in ['n', 's']:
				neighbourOrSep = input("Please only input 'n' or 's'..")
		else:
			# generate map
			taskHere = "python3.6 map-generator/mapNodesGenerator.py " + str(numOfNodes)
			output = subprocess.check_call(taskHere, shell=True)

		regeneratePythonScript(numOfNodes, numOfColors)
		# execute backtracking on the new generated map(if numOfNodes == 2)
		taskHere = "i=0; while [ $i -lt 5 ]; do python2.7 radio-coloring/UserDIY/radio.py radio-coloring/UserDIY/constraints; ((i++)); done"
		output = subprocess.check_call(taskHere, shell=True)
		# show coloring results
		showColoringResults()

		print("2 - Coloring the nodes at your choice by other algorithms with auto set colors\n")
		# regenerate other algos C++ scripts
		writeToOtherAlgosMapFile(numOfNodes)
		# run algorithms
		taskHere = "cd graph-coloring-algos; make; ./color-test"
		output = subprocess.check_call(taskHere, shell=True)

	else:

		if mapChoice == 'c':
			numOfNodes = 100
		elif mapChoice == 'd':
			numOfNodes = 300
		elif mapChoice == 'e':
			numOfNodes = 400
		elif mapChoice == 'f':
			numOfNodes = 500

		# regenerate py script and execute
		regeneratePythonScript(numOfNodes, numOfColors)
		taskHere = "i=0; while [ $i -lt 5 ]; do python2.7 radio-coloring/UserDIY/radio.py radio-coloring/UserDIY/constraints; ((i++)); done"
		output = subprocess.check_call(taskHere, shell=True)
		showColoringResults()

		print("2 - Coloring previously set " + str(numOfNodes) + " nodes by other algorithms with auto set colors\n")
		# regenerate c++ script and execute
		writeToOtherAlgosMapFile(numOfNodes)
		taskHere = "cd graph-coloring-algos; make; ./color-test"
		output = subprocess.check_call(taskHere, shell=True)

