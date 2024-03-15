# Given a regular chessboard, find a way to move a knight such that it lands on every square precisely once 

BOARD_SIZE = 5

DELTAS = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2))

def find_next(current, path):
    """
    Given the current position and path so far, return a lsit of possible next steps.
    """
    out = []
    for dx, dy in DELTAS: 
        cx, cy = current[0] + dx, current[1] + dy 
        if 0 <= cx < BOARD_SIZE and 0 <= cy < BOARD_SIZE and (cx, cy) not in path:
            out.append((cx, cy))
    return out


def tour(start = (0, 0)):
    """
    Do a DFS of the graph formed by the valid moves of a knight on a 
    standard chessboard. Find a path of unique vertices of length 63. 

    Model the path as a Python dict, since ordering is maintained, and we can use it for O(1) membership testing.
    """
    s = [(start, {start: None})]

    while s: 
        current, path = s.pop()
        if len(path) == BOARD_SIZE * BOARD_SIZE: 
            return path 
        
        candidates = find_next(current, path)
        for c in candidates: 
            path_copy = path.copy()
            path_copy[c] = None 
            s.append((c, path_copy))
        
    return None
    
if __name__ == '__main__':
    print(tour())