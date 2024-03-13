# Program like `pstree` which takes the output of the `ps` command line program 
# and reformats it visually as a tree, to show related processes together 

"""
- Read from stdin 
- Use first line to determine/validate pid, ppid 
- For each subsequent line 
    - Tokenize by splitting
    - Extract pid, ppid etc. 
    - Create instance of process with "children" attribute 
    - Recursively check if ppid of this process is pid of any process in our tree 
        - If so, add as a child 
        - Else, add this process to root, and check if any root process should be 
parented under this one
- For each process in root: 
    print that process's info, then recursively run this print routine 
"""

import sys 

class Process(object): 
    def __init__(self, pid, ppid, info):
        self.pid = pid 
        self.ppid = ppid 
        self.info = info 
        self.children = []
    
def print_processes(processes, depth = 0):
    for p in processes: 
        print(' ' * depth, p.pid, p.info)
        print_processes(p.children, depth + 1)

def find(node, test):
    if test(node):
        return node 
    
    for child in node.children:
        parent = find(child, test)
        if parent is not None: 
            return parent 
    return None 

def main():
    header = sys.stdin.readline().split()
    try: 
        pid_idx = header.index('PID')
        ppid_idx = header.index('PPID')
    except ValueError:
        print('Usage: ps -o pid,ppid,[etc] | python3 pstree.py', file = sys.stderr)
        exit(1)
    
    # tokenize process info and group into a tree
    root = []
    for line in sys.stdin:
        parts = line.split()
        pid = parts[pid_idx]
        ppid = parts[ppid_idx]
        info = ''.join(x for i, x in enumerate(parts) if i not in {pid_idx, ppid_idx})
        proc = Process(pid, ppid, info)

        for node in root: 
            parent = find(node, lambda n: n.pid == ppid)
            if parent is not None: 
                parent.children.append(proc)
                break 
        else: 
            for i, p in enumerate(root):
                if p.ppid == pid: 
                    proc.children.append(p)
                    root.pop(i)
                    break 
            root.append(proc)

    
    # print tree
    print_processes(root)


if __name__ == '__main__':
    main()

