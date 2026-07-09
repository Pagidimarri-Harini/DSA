class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        timearr = [((target-position[i])/speed[i], position[i]) for i in range(len(position))]
        timearr.sort(key=lambda timearr: timearr[1], reverse = True)
        print(timearr)
        count = 0
        maxtime = 0
        for i in range(len(timearr)):
            if timearr[i][0] > maxtime:
                maxtime = timearr[i][0]
                count += 1
        return count
            


        