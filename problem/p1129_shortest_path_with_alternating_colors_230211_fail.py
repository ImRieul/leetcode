# 1129. Shortest Path with Alternating Colors
# Difficulty: Medium, 30m
# https://leetcode.com/problems/shortest-path-with-alternating-colors/solutions/

# 제한 시간 안에 풀지 못함.
# 원인
#  1. 문제를 잘 이해하지 못했다. 노드, 에지의 개념을 이해하지 못했다.
#  2. 접근 방법도 잘못 되었다. 그저 색이 번갈아가면서 다음 노드로 이어져야 하는 것 같았다.
#  3. wrong_answer를 보니 검색 알고리즘에 대한 문제 같다.




from typing import List

from objectdict import ObjectDict


# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1.
# Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
#
# You are given two arrays redEdges and blueEdges where:
#
# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph,
# and blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x
# such that the edge colors alternate along the path, or -1 if such a path does not exist.

# Example 1:
# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]

# Example 2:
# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        output = [0]
        edges = []

        for i in range(n):
            if i < len(red_edges):
                edges.append(red_edges[i])
            else:
                edges.append([])

            if i < len(blue_edges):
                edges.append(blue_edges[i])
            else:
                edges.append([])

        edges = edges[:n]

        for i in range(n-1):
            if len(edges[i]) == 0:
                output.append(-1)
            elif edges[i][0] == i and edges[i][1] == i+1:
                output.append(i+1)
            else:
                output.append(-1)

        return output



# 공식 풀이
# https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1376/
# BFS(Breadth-First Search) 알고리즘을 사용. 너비 우선 탐색이라고 한다.
# 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 사용.
# 자료 구조는 큐(Queue)를 사용한다.
# 큐는 선입선출(FIFO) 방식으로 데이터를 저장한다.

# java 코드를 변환하려 했으나, 모르는 개념이 많아 부분적으로 더 공부를 해야겠다.
# https://leetcode.com/problems/shortest-path-with-alternating-colors/solutions/3049265/shortest-path-with-alternating-colors/

class Solution1:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        adj: ObjectDict[int, List[int]] = ObjectDict()
        for i in range(len(red_edges)):
            adj.red_edges = [red_edges[0], [red_edges[1], 0]]

        for i in range(len(blue_edges)):
            adj.blue_edges = [blue_edges[0], [blue_edges[1], 1]]

        answer: int = [0] * n
        visit: ObjectDict[bool, bool] = ObjectDict()
        queue: List[int] = []

        print(adj, answer)

if __name__ == '__main__':
    s = Solution1()
    print(s.shortestAlternatingPaths(3, [[0,1],[1,2]], []))