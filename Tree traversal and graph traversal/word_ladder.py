# Given two words of equal length, find the shortest path from one to the other, changing just one letter at a time 

# e.g HEAD -> heal -> teal -> tell -> tall -> TAIL

"""

Build a graph where each word in our dictionary is a vertex, and edges are defined by pairs 
of words that differ by only 1 letter, then BFS from start to end words 

Dev goals: 
    - Build graph itself 
    - Perform any kind of traversal (find any path)
    - Perform BFS (shortest path)
    - Track/print the path itself 

Options: 
    - Not build graph, just O(n) scan to expand each vertex 
    - Build graph by brute force: for each word, consider if every word is a neighbour: O(n^2)
    - Scan words, and group together sets that match each pattern "FOU?" etc.

    {"FOU?": ["FOUR", "FOUL", ...]}

    {"FOUR": ["DOUR", "SOUR", ..., "FOUL],
     "FOUL": ["FOUR", "FOAL", ...]}

Plan: 
    - For each word, consider "templates" of the form "?OUR", "F?UR" etc and add the word to a dictionary 
where keys are the template, and values are words that match templates
    - Build graph where keys are words, values are sets of connected words, as defined by each pair of words in each template bucket 
    - Search this graph (ultimately with BFS)
"""
from collections import defaultdict

def build_graph(words):
    buckets = defaultdict(list)
    for w in words: 
        for i in range(len(w)):
            template = ''.join(ch if i != j else '?' for j, ch in enumerate(w))
            buckets[template].append(w)

    graph = defaultdict(list)
    for bucket in buckets.values():
        for x in bucket: 
            for y in bucket:
                if x != y:
                    graph[x].append(y)
    
    return graph

def ladder(graph, start, goal):
    q = [(start, [start])]
    visited = set()
    while q: 
        x, path = q.pop(0)
        if x == goal: 
            return path
        for y in graph[x]:
            if y not in visited:
                q.append((y, path + [y]))
                visited.add(y)
    return False


if __name__ == '__main__':
    with open('words.txt', 'r') as f: 
        graph = build_graph(w.strip().lower() for w in f.readlines())
    
    print(ladder(graph, 'pig', 'sty'))
    print(ladder(graph, 'pig', 'pig'))
    print(ladder(graph, 'pig', 'pit'))
    print(ladder(graph, 'pig', 'piggy'))
    print(ladder(graph, 'aloof', 'piggy'))