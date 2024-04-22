    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        def isCompleteComponent(component):
            for i in component:
                for j in component:
                    if i != j and j not in graph[i]:
                        return False
            return True

        components = []
        visited = set()
        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)
                components.append(component)
                visited |= component

        res = 0
        for component in components:
            if isCompleteComponent(component):
                res += 1

        return res