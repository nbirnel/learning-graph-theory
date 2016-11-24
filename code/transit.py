#!/usr/bin/env python3

#http://legacy.python.org/doc/essays/graphs/
# Copyright (c) 1998, 2000, 2003 Python Software Foundation.
# All rights reserved.
# Licensed under the PSF license.

# Directed graph code

# Modified by Noah Birnel for python3 (replace 'has_key' with 'in')

import pygraphviz as pgv

ft = {
    'name': 'ft',
    'graph': {
        'Seattle': ['Tacoma', 'Everett', 'Bremerton'],
        'Bremerton': ['Port Orchard'],
        'Tacoma': ['Olympia'],
        'Olympia': ['Aberdeen', 'Chehalis'],
        'Aberdeen': ['Astoria', 'Humptulips', 'Ocean Shores'],
        'Astoria': ['Seaside', 'Portland'],
        'Seaside': ['Cannon Beach'],
        'Portland': ['Tillamook', 'Cannon Beach'],
        'Cannon Beach': ['Manzanita'],
        }
    }



def main():
    for g in [ft]:
        graph = g['graph']

        G = pgv.AGraph(label=g['name'])

        for node in graph:
            G.add_node(node, label=node)
            for edge in graph[node]:
                G.add_edge(node, edge)
        #G.draw(g['name'] + '.svg', prog='dot')
        G.write(g['name'] + '.dot')

if __name__ == '__main__':
    main()
