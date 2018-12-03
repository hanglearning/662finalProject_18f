# !/usr/bin/python
__author__ = 'sagar'

'''
Brief report on the program:

Formulation of problem : The problem given is classic example of map/graph coloring problem. Here each state
represent a node in the map and frequencies represent colors to be assigned. We need to ensure two adjacent states
should not get same frequency.
Proposed solution : There are many efficient solution to solve this problem. Few of them are
(a) Back tracking
(b) Forward checking with back tracking
(c) Arc consistency, etc

Choosing the right approach : Here there are very modest number of states to be assigned frequency to. Hence we need
an algorithm which is fast and will ensure it searches through limited search space. This eliminates back tracking
from the available options as it will search large number of states without limiting the domain. The choices remain
forward checking and arc consistency. Arc consistency is not an algorithm to find the solution, it can help to limit
the search space if we run it before or after assignment of variable. Arc consistency is very useful to propagate the
assignment and detect the collision early. However it is much costly compared to forward checking. Hence here I have
chosen variant of forward checking with most constrained variable and most constraining variable heuristic.

The algorithm is recursive.

Algorithm:
RadioSolver (Input : constraint_file )
OUTPUT : Number of backtracks, result.txt in the format <state> <frequency>

Adjacency_matrix <- create adjacency matrix for states considering neighbouring states
backtrack_counter = 0

forward_check(colored_states, domains, available states)
if length(colored_states) = length(total_states)
return colored_states

next_state <- select best state for assignment from available_states

domain <- current_domain(nex_state)

for all values in domain:
assign domain to state
prune_domain(state, domains)
colored_States.add(state)
result = call forward_check(colored_states, domains, available_states - state)
if result fails:
remove the state from colored states
undo changes in domain
else
return result
algorithm end

function prune_domain(state,domains)
for all neighbours of state remove state.frequency from neighbor.domain

Assumptions: The states and constraints are space separated values

Performance of algorithm: average time required : 0.002 seconds for legacy-constraints-1 file.
Number of backtracks : 0 for all the sample constraint files


Possible improvements in program: The parsing states can be done once and adjacency matrix can be stored in separate
file to avoid recalculation for every run. The heuristic can be improved for ordering of domain values if there is
change in number of states or number of neighbours increases by considerable amount. In case the number of neighbours
is very large arc consistency algorithm can be applied after each assignment.

'''
import sys, os
import logging
import time
import random

# set debug level
logging.basicConfig(level=logging.INFO)


class RadioSolver:
    def __init__(self):
        self.states = []
        self.adjacent = {}  # adjacency matrix
        self.bands = ['Red', 'Green', 'Blue']  # all possible domain values
        self.stateband = {}  # state and frequency assignment
        self.back_track_counter = 0  # total backtracks
        self.max_neighbours_state = ""  # neighbou with maximum neighbours

    def display(self):
        logging.info("adjacent states: " + str(self.adjacent))

    def is_consistent(self):  # utility function to check if assignment is consistent. Can be used to avoid manual
        # checking of output, the function will return false if any of the state and neighbour has same frequency
        output = "";
        for state in self.stateband.keys():
            band = self.stateband[state]
            output += "\n" + state + " " + band

            for neighbour in self.adjacent[state]:
                nband = self.stateband[neighbour]
                output += "\t" + neighbour + " " + nband
                if band == nband:
                    logging.error(state + " " + neighbour)
                    return False
        logging.debug(output)
        return True

    def printAnswer(self):
        # logging.debug("Frequency assignment is consistent : " + str(self.is_consistent()))
        with open("radio-coloring/Australia/results.txt", 'w') as output_file:
            for state in self.stateband.keys():
                output_file.write("%s\n" % (state + " " + self.stateband.pop(state)))
        # print "Number of backtracks: " + str(self.back_track_counter)

    def prune_domains(self, state, band, domains):  # updates the possible domain values of all the neighbours for
        # given state
        for adjacent_state in self.adjacent[state]:
            bands = domains[adjacent_state]
            if band in bands:
                bands.remove(band)
            if len(bands) == 0:
                return []
            domains[adjacent_state] = bands
        return domains

    def get_most_constrained_variable(self, available_states,
                                      domain):  # heuritic to get next best state for assignment

        if len(available_states) == len(self.states):
            return self.max_neighbours_state

        min_domain_states = []
        min_size = 50
        for state in available_states:
            if len(domain[state]) < min_size:
                min_domain_states = [state]
                min_size = len(domain[state])
            elif len(domain[state]) == min_size:
                min_domain_states.append(state)

        # now select the state which is maximum connected
        max_neighbours_state = ""
        max_neighbours = -1
        for state in min_domain_states:
            neighbours = self.adjacent[state]
            if max_neighbours < len(neighbours):
                max_neighbours = len(neighbours)
                max_neighbours_state = state

        return max_neighbours_state

    def forward_check(self, assigned_states, domains, available_states):

        if len(assigned_states) == len(self.states):
            return assigned_states

        # Selecting Most constraining variable from Most Constrained Variable
        state = self.get_most_constrained_variable(available_states, domains)

        current_domain = domains[state]
        neighboour_domains = {}

        for neighbour in self.adjacent[state]:
            neighboour_domains[neighbour] = domains[neighbour][:]

        for band in current_domain:
            prunned = self.prune_domains(state, band, domains)
            if len(prunned) > 0:
                assigned_states.append(state)
                self.stateband[state] = band
                # print("before", available_states)
                available_states.remove(state)
                # print("after", available_states)
                result = self.forward_check(assigned_states, prunned, available_states)
                # print("result", result)
                if not result:
                    available_states.append(state)
                    assigned_states.remove(state)
                    self.stateband.pop(state)
                    # print("before", self.back_track_counter)
                    self.back_track_counter += 1
                    # print("after", self.back_track_counter)
                else:
                    return result

            for neighbour in neighboour_domains.keys():
                domains[neighbour] = neighboour_domains[neighbour][:]

        return False


def main():
    start = time.time()
    solver = RadioSolver()
    filename = "radio-coloring/Australia/adjacent-states-au"
    max_neighbours_state = ""
    max_neighbours = 0
    with open(filename, 'r') as adjacent_states:
        for line in adjacent_states:
            states = line.split()
            key = states.pop(0)
            solver.states.append(key)
            values = states
            solver.adjacent[key] = values
            if max_neighbours < len(values):
                max_neighbours = len(values)
                max_neighbours_state = key

    solver.max_neighbours_state = max_neighbours_state
    logging.debug('Reading from adjacency state file complete')
    domains = {state: ['Red', 'Green', 'Blue'] for state in solver.states}

    constraint_file = sys.argv[1]

    assigned_states = []
    with open(constraint_file, 'r') as constraints:
        for line in constraints:
            if not line.strip():
                break
            constraint = line.split()
            state = constraint[0]
            band = constraint[1]
            solver.stateband[state] = band
            domains[state] = [band]
            assigned_states.append(state)

    for state in solver.stateband.keys():
        solver.prune_domains(state, solver.stateband[state], domains)

    result = solver.forward_check(assigned_states, domains,
                         list(set(solver.states[:]) - set(assigned_states)))
    if not result:
        print ("No assignment possible")
    else:
        solver.printAnswer()
    logging.info("Execution time : " + str(time.time() - start))


if __name__ == '__main__':
    main()
