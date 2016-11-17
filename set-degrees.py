#!/usr/bin/env python3

import pygraphviz as pgv

G5_4 = {
    'name': 'G5_4',
    'graph': {
        'a': ['b', 'c', 'd', 'e'],
        'b': ['a', 'c', 'd', 'e'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['a', 'b', 'c', 'e'],
        'e': ['a', 'b', 'c', 'd'],
        }
    }

G5_34 = {
    'name': 'G5_34',
    'graph': {
        'a': ['b', 'c', 'd', 'e'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'e'],
        'd': ['a', 'b', 'e'],
        'e': ['b', 'c', 'd'],
        }
    }

G5_24 = {
    'name': 'G5_24',
    'graph': {
        'a': ['b', 'c', 'd', 'e'],
        'b': ['a', 'c'],
        'c': ['a', 'b'],
        'd': ['a', 'e'],
        'e': ['a', 'd'],
        }
    }

G5_14 = {
    'name': 'G5_14',
    'graph': {
        'a': ['b', 'c', 'd', 'e'],
        'b': ['a'],
        'c': ['a'],
        'd': ['a'],
        'e': ['a'],
        }
    }

G5_234 = {
    'name': 'G5_234',
    'graph': {
        'a': ['b', 'c', 'd', 'e'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'e'],
        'd': ['a', 'b'],
        'e': ['a', 'c'],
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
    (min(degrees), max(degrees))

def uniq_degrees_of(graph):
    return set(degrees_of(graph))

def complement_of(graph):
    vertices = set(graph.keys())
    return {vertex: list(vertices - set(edges)) for vertex, edges in graph.items()}

def main():
    for g in [G5_4, G5_34, G5_24, G5_14, G5_234]:
        graph = g['graph']
        degrees_str = ', '.join([str(d) for d in uniq_degrees_of(graph)])

        G = pgv.AGraph(label=g['name'] + ': ' + degrees_str)

        for node in graph:
            G.add_node(node, label=node + ': δ' + str(len(graph[node])))
            for edge in graph[node]:
                G.add_edge(node, edge)
        G.draw(g['name'] + '.svg', prog='dot')

if __name__ == '__main__':
    main()
