def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[v].append(u)

    answer = [[] for _ in range(n)]

    def dfs(nodes, curr):
        for node in graph[curr]:
            if node not in answer[nodes]:
                answer[nodes].append(node)
                dfs(nodes, node)

    for i in range(n):
        dfs(i, i)

    for i in answer:
        i.sort()

    return answer