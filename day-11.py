import sys

from collections import defaultdict
from functools import cache
from pathlib import Path


example = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

example_2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        

    def pt1(self, v, num):
        for neighbour in self.graph[v]:
            if neighbour == 'out':
                num += 1
            else:
                num = self.pt1(neighbour, num)
        
        return num
    
    @cache
    def pt2(self, v, seen_dac, seen_fft):
        if v == 'out':
            return 1 if seen_dac and seen_fft else 0

        seen_dac = seen_dac or v == "dac"
        seen_fft = seen_fft or v == "fft"

        return sum(self.pt2(neighbor, seen_dac, seen_fft) for neighbor in self.graph[v])


def process_input(text: str):
    lines = text.split('\n')

    g = Graph()

    for line in lines:
        parent, children_str = line.split(':')
        children = children_str.strip().split()
        for child in children:
            g.addEdge(parent, child)

    return g


if __name__ == "__main__":
    problem = process_input(
        example if len(sys.argv) == 1
        else Path(sys.argv[1]).open().read()
    )

    pt2_example = process_input(example_2)

    print(problem.pt1('you', 0))
    print(pt2_example.pt2('svr', False, False) if len(sys.argv) == 1 else problem.pt2('svr', False, False))