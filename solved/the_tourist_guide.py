#!/usr/bin/env python
# Solution to the tourist guide problem found in:
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=37&page=show_problem&problem=1040

import sys
from heapq import heappush, heappop, heapify
from math import ceil


def str2inttuple(string):
    """Parse a string to integers tuple"""
    return tuple(int(v) for v in string.split())


def read_input(filename):
    """Function to parse input files"""
    with open(filename, 'r') as ifile:
        test_cases = []
        for line in ifile:
            # Parse the first line of each test case
            n_nodes, n_edges = str2inttuple(line)
            # if the values are zeros there are no more test cases
            if n_nodes == 0 and n_nodes == 0:
                break
            else:
                graph = {v: [] for v in range(1, n_nodes+1)}
                # For each edge line, put the edge into the graph
                for _ in range(n_edges):
                    edge = str2inttuple(ifile.next())
                    graph[edge[0]].append((edge[1], edge[2]))
                    graph[edge[1]].append((edge[0], edge[2]))
                # Get the start and end nodes and the number of tourists
                start, end, tourists = str2inttuple(ifile.next())
                # Save the test case
                test_cases.append({'start': start,
                                   'end': end,
                                   'tourists': tourists,
                                   'graph': graph})
        return  test_cases


def find_min_travels(start, end, tourists, graph):
    """This function calculates the minimal number of travels the guide has to
    do.

    It visits first the cities which minimal route bus capacity is the highest.
    To to do so, it has a max heap of the minimal capacities to get to a city
    following a certain path.
    We also keep a set of visited edges so we don't get into infinite loops.
    """
    # Case when you don't need to move the tourists
    if start == end:
        return 0

    current = start
    current_capacity = -float('inf') # Negative infinite

    # We use the negative of the capacity because heapq is a min heap
    to_visit = [(-capacity, neighbor) for neighbor, capacity in graph[current]]
    heapify(to_visit)
    visited = set()
    while(True):
        for neighbor, capacity in graph[current]:
            # Use canon edges: sorted nodes
            edge = min(neighbor, current), max(neighbor, current)
            if edge not in visited:
                visited.add(edge)
                heappush(to_visit, (max(current_capacity, -capacity), neighbor))
        try:
            current_capacity, current = heappop(to_visit)
        except IndexError:
            raise LookupError('No path found from {} to {}'.format(start, end))
        if current == end:
            break
    return int(ceil(float(tourists)/(-current_capacity-1)))


if __name__ == '__main__':
    for test_id, test_case in enumerate(read_input(sys.argv[1]), 1):
        #print(test_case)
        #break
        travels = find_min_travels(test_case['start'], test_case['end'],
                                   test_case['tourists'], test_case['graph'])
        print('Scenario #{}'.format(test_id))
        print('Minimum Number of Trips = {}'.format(travels))
