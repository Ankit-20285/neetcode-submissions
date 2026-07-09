import bisect
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        pairs = self.store[key]
        idx = bisect.bisect_right(pairs, [timestamp, chr(127)])
        if idx == 0:
            return ""
        return pairs[idx - 1][1]
