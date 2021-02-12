import heapq
import math

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        graph = {}
        minDistances = [None] * n
        fromVertex = [None] * n
        for e, p in zip(edges, succProb):
            w = (e[0], e[1], 888888.0) if p == 0 else (e[0], e[1], -1 * math.log(p, 2))
            if e[0] not in graph:
                graph[e[0]] = [w]
            else:
                graph[e[0]].append(w)
            t = (e[1], e[0], 888888.0) if p == 0 else (e[1], e[0], -1 * math.log(p, 2))
            if e[1] not in graph:
                graph[e[1]] = [t]
            else:
                graph[e[1]].append(t)

        if start not in graph:
            return 0

        cost, arrivedVertex, fromV = 0, start, None
        CostFromSource = [(cost, arrivedVertex, fromV)]
        heapq.heapify(CostFromSource)

        while len(CostFromSource) > 0:
            cost, arrivedVertex, fromV = heapq.heappop(CostFromSource)
            if minDistances[arrivedVertex] == None:
                minDistances[arrivedVertex] = cost
                fromVertex[arrivedVertex] = fromV
                for e in graph[arrivedVertex]:
                    heapq.heappush(CostFromSource, (e[2] + cost, e[1], arrivedVertex))
        return 0.0 if minDistances[end]==None else 2 ** (-1 * minDistances[end])


sln = Solution()
assert 0.25000 == sln.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2)
assert 0.30000 == sln.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2)
assert 0.00000 == sln.maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2)
assert 0 == sln.maxProbability(500,[[193,229],[133,212],[224,465]],[0.91,0.78,0.64],4,364)
