"""
Problem: LeetCode 981 - Time Based Key-Value Store

Key Idea:
To implement a time-based key-value store, we can use a dictionary to store the values associated with each key. For each key, we store a list of tuples representing the timestamp and the corresponding value. When querying a key at a specific timestamp, we perform binary search on the list of timestamps associated with that key to find the largest timestamp less than or equal to the given timestamp.

Time Complexity:
1. The time complexity of the 'set' operation is O(1), as it involves adding a new value to the dictionary.
2. The time complexity of the 'get' operation is O(log n), where n is the number of timestamps associated with the queried key. This is due to the binary search performed to find the appropriate value.

Space Complexity:
The space complexity is O(n), where n is the number of keys. We need to store values and timestamps for each key in the dictionary.
"""

class TimeMap: 
    def __init__(self):
        self.store = {} # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None: 
        if key not in self.store: 
            self.store[key] = []
        self.store[key].append([value, timestamp])
    
    def get(self, key: str, timestamp: int) -> str: 
        res = ""
        values = self.store.get(key, [])

        # binary search 
        l, r = 0, len(values) - 1 
        while l <= r:
            m = (l + r) // 2 
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1 
            else: 
                r = m - 1