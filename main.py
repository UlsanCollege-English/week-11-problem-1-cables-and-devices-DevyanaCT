
## main.py
```python
"""
HW01 — Cables and Devices

Implement:
- build_graph(edges, directed=False)
- degree_dict(graph)

Do NOT add type hints. Use only the standard library.
"""

def build_graph(edges, directed=False):
    """Return a dictionary: node -> list of neighbors.

    edges: list of (u, v) pairs.
    directed: if True, add only u->v; if False, add both u->v and v->u.

    TODO (8 Steps):
    1) Read & Understand: what is an edge here?
    2) Re-phrase: say the goal in your own words.
    3) Identify I/O: define input and output shapes.
    4) Break down: plan a loop that builds the dict; handle new keys.
    5) Pseudocode: write steps in comments above your code.
    6) Write the code.
    7) Debug: print and check small cases (do this locally).
    8) Optimize: write big-O in README.
    """
    raise NotImplementedError


def degree_dict(graph):
    """Return a dictionary: node -> degree (number of neighbors).

    For directed graphs built with directed=True, this is out-degree.
    For undirected graphs, this equals the usual degree.

    TODO: implement after you finish build_graph.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # Optional manual check
    sample = [('PC1','SW1'), ('SW1','PR1'), ('PR1','PC2')]
    print("Sample edges:", sample)
    # Fill in calls below after you implement functions
    # g = build_graph(sample, directed=False)
    # print("Graph:", g)
    # print("Degrees:", degree_dict(g))
    pass

## main.py
```python
"""
HW01 — Cables and Devices

Implement:
- build_graph(edges, directed=False)
- degree_dict(graph)

Do NOT add type hints. Use only the standard library.
"""

def build_graph(edges, directed=False):
    """Return a dictionary: node -> list of neighbors.

    edges: list of (u, v) pairs.
    directed: if True, add only u->v; if False, add both u->v and v->u.

    TODO (8 Steps):
    1) Read & Understand: what is an edge here?
    2) Re-phrase: say the goal in your own words.
    3) Identify I/O: define input and output shapes.
    4) Break down: plan a loop that builds the dict; handle new keys.
    5) Pseudocode: write steps in comments above your code.
    6) Write the code.
    7) Debug: print and check small cases (do this locally).
    8) Optimize: write big-O in README.
    """
    raise NotImplementedError


def degree_dict(graph):
    """Return a dictionary: node -> degree (number of neighbors).

    For directed graphs built with directed=True, this is out-degree.
    For undirected graphs, this equals the usual degree.

    TODO: implement after you finish build_graph.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # Optional manual check
    sample = [('PC1','SW1'), ('SW1','PR1'), ('PR1','PC2')]
    print("Sample edges:", sample)
    # Fill in calls below after you implement functions
    # g = build_graph(sample, directed=False)
    # print("Graph:", g)
    # print("Degrees:", degree_dict(g))
    pass
