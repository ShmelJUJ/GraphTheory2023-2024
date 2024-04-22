    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        d = {i: [1, 0] for i in range(n)}

        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    d[node][0] += d[child][0]
                    d[node][1] += (d[child][0] + d[child][1])
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    d[child][1] = d[node][1] - d[child][0] + (n - d[child][0])
                    dfs2(child, node)

        dfs(0, -1)
        dfs2(0, -1)
        res = []

        for key in d:
            res.append(d[key][1])
        return res