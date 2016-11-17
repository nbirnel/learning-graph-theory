#!/usr/bin/env python3

import pygraphviz as pgv

G2 = {
    'name': 'G2',
    'graph': {
        'a': [],
        'b': [],
        }
    }

H2 = {
    'name': 'H2',
    'graph': {
        'a': ['b'],
        'b': ['a'],
        }
    }

G3 = {
    'name': 'G3',
    'graph': {
        'a': ['b'],
        'b': ['a'],
        'c': [],
        }
    }

H3 = {
    'name': 'H3',
    'graph': {
        'a': ['c'],
        'b': ['c'],
        'c': ['a', 'b'],
        }
    }

G4 = {
    'name': 'G4',
    'graph': {
        'a': ['c'],
        'b': ['c'],
        'c': ['a', 'b'],
        'd': [],
        }
    }

H4 = {
    'name': 'H4',
    'graph': {
        'a': ['b', 'd'],
        'b': ['a', 'd'],
        'c': ['d'],
        'd': ['a', 'b', 'c'],
        }
    }

G5 = {
    'name': 'G5',
    'graph': {
        'a': ['b', 'd'],
        'b': ['a', 'd'],
        'c': ['d'],
        'd': ['a', 'b', 'c'],
        'e': [],
        }
    }

H5 = {
    'name': 'H5',
    'graph': {
        'a': ['c', 'e'],
        'b': ['c', 'e'],
        'c': ['a', 'b', 'e'],
        'd': ['e'],
        'e': ['a', 'b', 'c', 'd'],
        }
    }

G6 = {
    'name': 'G6',
    'graph': {
        'a': ['c', 'e'],
        'b': ['c', 'e'],
        'c': ['a', 'b', 'e'],
        'd': ['e'],
        'e': ['a', 'b', 'c', 'd'],
        'f': []
        }
    }

H6 = {
    'name': 'H6',
    'graph': {
        'a': ['b', 'd', 'f'],
        'b': ['a', 'd', 'f'],
        'c': ['d', 'f'],
        'd': ['a', 'b', 'c', 'f'],
        'e': ['f'],
        'f': ['a', 'b', 'c', 'd', 'e'],
        }
    }

def add_isolated_vertex(graph):
    last_node = sorted(graph.keys())[-1]
    new_node = chr(ord(last_node) +1)
    isolated_vertex = {new_node: []}
    copy = graph.copy()
    copy.update(isolated_vertex)
    return copy

def degrees_of(graph):
    return [len(edges) for node, edges in graph.items()]

def minimax_of(graph):
    degrees = degrees_of(graph)
    return (min(degrees), max(degrees))

def complement_of(graph):
    vertices = set(graph.keys())
    return {vertex: list(vertices - set(edges)) for vertex, edges in graph.items()}

def main():
    for g in [G2, H2, G3, H3, G4, H4, G5, H5, G6, H6]:
        graph = g['graph']
        degrees_str = ', '.join([str(d) for d in minimax_of(graph)])

        G = pgv.AGraph(label=g['name'] + ': ' + degrees_str)

        for node in graph:
            G.add_node(node, label=node + ': δ' + str(len(graph[node])))
            for edge in graph[node]:
                G.add_edge(node, edge)
        G.draw(g['name'] + '.svg', prog='dot')

if __name__ == '__main__':
    main()
