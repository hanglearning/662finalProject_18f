import sys
from random import randint

# get user inputs
arguments = sys.argv
NODES_NUMBER = int(arguments[1])

algos = ["dsatur", "hybrid_dsatur", "hybrid_lmxrlf", "lmxrlf", "mcs", "tabucol"]

# nodeNum is the current node
# nodeSeq is the temp neighbor node of the current node
def NeighborGenerator(nodeNum):
  start = randint(1, NODES_NUMBER - 1)
  end = randint(1, NODES_NUMBER)
  nodelist = []
  while end <= start:
    end = randint(1, NODES_NUMBER)
  for j in range(start, end + 1):
    nodeSeq = randint(1, NODES_NUMBER)
    while nodeSeq == nodeNum or (nodeSeq in nodelist):
      nodeSeq = randint(1, NODES_NUMBER)
    nodelist.append(nodeSeq)
  return nodelist

def mapGenerator():
  open('map-generator/newMap/' + str(NODES_NUMBER) + 'nodes.txt', 'w').close()
  open('map-generator/newMap/' + str(NODES_NUMBER) + 'nodes_radio.txt', 'w').close()

  for node in range(1, NODES_NUMBER + 1):
    nodes_file = open('map-generator/newMap/' + str(NODES_NUMBER) + 'nodes.txt', "a")
    nodes_radio_file = open('map-generator/newMap/' + str(NODES_NUMBER) + 'nodes_radio.txt', "a")
    nodes_file.write("    vector<string> node_k")
    nodes_file.write(str(node))
    nodes_radio_file.write(str(node))
    nodes_file.write(" = { \"k")
    nodes_radio_file.write(" ")
    neighborList = NeighborGenerator(node)
    neighborList.sort()
    neighborNum = len(neighborList)
    for i in range(0, neighborNum):
      nodes_file.write(str(neighborList[i]))
      nodes_radio_file.write(str(neighborList[i]))
      if i != (neighborNum - 1):
        nodes_file.write("\", \"k")
        nodes_radio_file.write(" ")

    nodes_file.write("\" };")
    nodes_file.write("\n")
    nodes_file.close()
    nodes_radio_file.write("\n")
    nodes_radio_file.close()

  nodes_file = open('map-generator/newMap/' + str(NODES_NUMBER) + 'nodes.txt', "a")
  nodes_file.write("    map<string,vector<string>> k")
  nodes_file.write(str(NODES_NUMBER))
  nodes_file.write(" = { ")
  for i in range(1, NODES_NUMBER + 1):
    nodes_file.write("{\"k")
    nodes_file.write(str(i))
    nodes_file.write("\", node_k")
    nodes_file.write(str(i))
    if i != NODES_NUMBER:
      nodes_file.write("}, ")
    else:
      nodes_file.write("} };")
  nodes_file.close()

mapGenerator()

# for algo in algos:
#   print("#include <gtest/gtest.h>")
#   if algo == "tabucol":
#     print("#include <climits>")
#   print()
#   print("#include \"../Header/" + algo + ".hpp\"")
#   print()
#   print("using GraphColoring::" + algo.capitalize() + ";")
#   print()
#   print("TEST(" + algo.capitalize() + "Tests, " + algo.capitalize() + "K5ColorTest) {")
  

