class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        adjlist = defaultdict(list)
        for i in edges: 
            adjlist[i[0]].append(i[1])
            adjlist[i[1]].append(i[0])
        visited = [0] * n
        print(adjlist)
        def dfs(adjlist, curr, parent):
            if visited[curr] == 1:
                return False
            visited[curr] = 1
            for i in adjlist[curr]:
                if i == parent:
                    continue
                if not dfs(adjlist,i, curr):
                    return False

            return True
        # print(visited.count(1), n)
        return dfs(adjlist,0,-1) and visited.count(1) == n
        
            

        