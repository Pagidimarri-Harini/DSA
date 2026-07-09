class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfaction = sum([customers[i] for i in range(len(customers)) if grumpy[i] == 0  ])
        print(satisfaction)
        for i in range(minutes):
            if grumpy[i] == 1:
                satisfaction += customers[i]
        maxsatis = satisfaction
        for i in range(minutes, len(grumpy)):
            
            if grumpy[i] == 1:
                satisfaction += customers[i]
            if grumpy[i-minutes] == 1:
                satisfaction -= customers[i-minutes]
            maxsatis = max(maxsatis, satisfaction)
        # print(grumpy)
        # print(endind, maxsum, endind-minutes)
        
        return maxsatis

            
            
        