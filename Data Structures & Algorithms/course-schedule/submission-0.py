class Solution:
    def detectCycle(self, pathvisited, visited, curr, adjlist):
        # print(curr, pathvisited[curr])
        visited[curr] = 1
        pathvisited[curr] = 1
        for i in adjlist[curr]: 
            if not visited[i] and not self.detectCycle(pathvisited, visited, i, adjlist):
                return False
            elif pathvisited[i] == 1:
                return False
        pathvisited[curr] = 0
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for i in prerequisites:
            adjlist[i[0]].append(i[1])
        pathvisited = [0] * numCourses
        visited = [0] * numCourses
        # print(adjlist)
        for i in range(numCourses):
            if visited[i] == 0:
                if not self.detectCycle(pathvisited, visited, i, adjlist):
                    return False
                # print(visited)
        return True
        