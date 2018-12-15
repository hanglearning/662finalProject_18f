# !/usr/bin/python
__author__ = 'sagar'

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
        self.bands = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
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
        with open("radio-coloring/UserDIY/results.txt", 'w') as output_file:
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
                available_states.remove(state)
                result = self.forward_check(assigned_states, prunned, available_states)
                if not result:
                    available_states.append(state)
                    assigned_states.remove(state)
                    self.stateband.pop(state)
                    self.back_track_counter += 1
                else:
                    return result

            for neighbour in neighboour_domains.keys():
                domains[neighbour] = neighboour_domains[neighbour][:]

        return False


def main():
    start = time.time()
    solver = RadioSolver()
    
    filename = "map-generator/135nodes_radio.txt"
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
    domains = {state: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'] for state in solver.states}

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
    logging.info("Execution time : " + str((time.time() - start) * 1000) + "ms")


if __name__ == '__main__':
    main()
