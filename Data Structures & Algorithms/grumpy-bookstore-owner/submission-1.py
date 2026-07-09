class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfaction = [customers[i] if grumpy[i] == 0 else 0 for i in range(len(customers)) ]
        prevsum = sum(satisfaction)
        maxsum = 0

        for i in range(len(grumpy)):
            
            maxsum = max(maxsum, prevsum - sum(satisfaction[i:i+minutes]) + sum(customers[i:i+minutes]))
        # print(grumpy)
        # print(endind, maxsum, endind-minutes)
        
        return maxsum

            
            
        