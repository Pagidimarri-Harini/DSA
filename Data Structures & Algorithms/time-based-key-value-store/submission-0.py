class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        
    def BinarySearch(self,arr, key):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left+right)//2
            if arr[mid][1] > key:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def get(self, key: str, timestamp: int) -> str:
        ans = self.BinarySearch(self.store[key], timestamp)
        if ans == -1:
            return ""
        return self.store[key][ans][0]
        
