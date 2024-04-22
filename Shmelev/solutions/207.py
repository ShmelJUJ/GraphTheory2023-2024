class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for v, u in prerequisites:
            graph[v].append(u)

        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True

            visited[course] = -1
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited[course] = 1
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True