class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = 0
        count = 0
        window = 0
        for i in range(len(arr)):
            # print(window, sum)
            
            sum += arr[i]
            window += 1
            if window == k:
                if sum//k >= threshold:
                    count += 1
                window -= 1
                sum -= arr[i-k+1]
        return count