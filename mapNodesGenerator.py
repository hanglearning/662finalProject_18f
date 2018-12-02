import sys
from random import randint

NODES_NUMBER = 100

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
  open('demofile.txt', 'w').close()
  for node in range(1, NODES_NUMBER + 1):
    f = open("demofile.txt", "a")
    f.write("    ")
    f.write("vector<string> node_k")
    f.write(str(node))
    f.write(" = { \"k")
  
    neighborList = NeighborGenerator(node)
    neighborList.sort()
    neighborNum = len(neighborList)
    for i in range(0, neighborNum):
      f.write(str(neighborList[i]))
      if i != (neighborNum - 1):
        f.write("\", \"k")

    f.write("\" };")
    f.write("\n")
    f.close()

mapGenerator()

for algo in algos:
  print("#include <gtest/gtest.h>")
  if algo == "tabucol":
    print("#include <climits>")
  print()
  print("#include \"../Header/" + algo + ".hpp\"")
  print()
  print("using GraphColoring::" + algo.capitalize() + ";")
  print()
  print("TEST(" + algo.capitalize() + "Tests, " + algo.capitalize() + "K5ColorTest) {")
  

