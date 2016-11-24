=====================
Learning Graph Theory
=====================

My notes and code from reading `The Fascinating World of Graph Theory`
(Benjamin, Chartrand & Zhang).

Chapter 1
=========

A *graph* `G` is a finite nonempty set `V` of objects called 
*vertices*, *nodes*, or *points*
together with a set `E` consisting of 2-element subsets of `V`.
Each element of `E` is known as an *edge* (or *arc*,  or *line*).
`G` may be written `G = (V, E)`. 
The vertex set may be written `V(G)`,
and the edge set `E(G)`.

The number `n` of vertices in graph `G` is called the *order* of `G`
and the number `m` of edges it's *size*.

A *complete graph* of order `N` (represented K\ :sub:`N`\ ) is a graph of `N` 
vertices with every two vertices joined by an edge.

A graph denoted K\ :sub:`N,N` has two sets of N vertices, where each vertex in 
one set is joined to all vertices in the other set.

An edge `e = uv` of a graph *joins* the vertices `u` and `v`;
`u` and `v` are *adjacent*, and are *neighbors* of eachother.
`u` and `e` are *incident*, as are `v` and `e`.

An edge has *orientation* if the direction of the relationship between it's
incident vertices is meaningful.

Two vertices which are not incident of the same edge are *non-adjacent*.

Two edges which are incident of the same vertex are *adjacent edges*.

If it is useful to discuss particular vertices of a graph `G`,
`G` is known as a *labelled graph*. 
Otherwise it is an *unlabelled graph*.

A graph of exactly one vertex is a *trivial graph*.
A graph of 2 or more vertices is a *non-trivial graph*.

A graph of no edges is an *empty graph*. 
A *nonempty graph* contains at least one edge.

The *degree* deg\ :sub:`G`\ *v* (or more simple deg *v*) is the number of
edges of vertex `v` of graph `G`.

A vertex of degree 0 is an *isolated vertex*, while a vertex of degree 1 is an
*end vertex*. A vertex in a graph of order `N` can have at most `N-1` degrees.

The *minimum degree* δ(`G`) and *maximum degree* Δ(`G`) of graph `G` are the
number of incident edges of the vertices with the least and most number of
incident edges respectively.

**First Theorem of Graph Theory** -- The *Handshaking Lemma*: 
In any graph, the sum of degrees of the vertices is twice the number of edges.

Thus, a graph of order `n` can have at most `m = n(n-1)/2` edges.

A vertice is *even* or *odd* according to whether it's degree is even or odd.

Every graph has an even number of odd vertices.

Chapter 2
=========

A graph `G` of order 2 or more is *irregular* if every two vetices of `G` have
different degrees.

**Party Friends Theorem**
There are no irregular graphs.

An *almost irregular* graph has exactly one pair vertices of the same degree.

The *complement* :math:`\overline{G}` of a graph `G` is the graph having the 
same vertices as G, where any two vertices `u` and `v` of :math:`\overline{G}`
are adjacent if an only if they are not adjacent in `G`.

If `v` is a vetext in graph `G` of order `n`,
the degree of v in :math:`\overline{G}` is equal to :math:`n - 1 - deg\  v`.
FIXME Why?

And thus two vertices `u` and `v` have the same degree in graph 
:math:`\overline{G}` if and only if they have the same degree in graph `G`.

**Two almost irregular graphs theorem**
For each integer `n≥2`, there are exactly two almost irregular graphs of order
`n`, and they are complements of eachother.

**Theorem 2.3**
For any set of postive integers whose largetst integer is `n`, there is a graph
of order `n + 1`, the degrees of whose vertices are precisely those integers.

.. graphviz:: K3.dot

