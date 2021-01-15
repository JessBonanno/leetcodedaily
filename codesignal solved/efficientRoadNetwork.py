"""
*** Efficient Road Network ***
------------------------------
Once upon a time, in a kingdom far, far away, there lived a King Byteasar III. As a smart and educated ruler, he did everything in his (unlimited) power to make every single system within his kingdom efficient. The king went down in history as a great road builder: during his reign a great number of roads were built, and the road system he created was the most efficient during those dark times.

When you started learning about Byteasar's III deeds in your history classes, a creeping doubt crawled into the back of your mind: what if the famous king wasn't so great after all? According to the most recent studies, there were n cities in Byteasar's kingdom, connected by two-way roads. You managed to get information about these roads from the university library, so now you can write a function that will determine whether the road system in Byteasar's kingdom was efficient or not.

A road system is considered efficient if it is possible to travel from any city to any other city by traversing at most 2 roads.

Example

For n = 6 and

roads = [[3, 0], [0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
the output should be
efficientRoadNetwork(n, roads) = true.

Here's how the road system can be represented:


For n = 6 and

roads = [[0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
the output should be
efficientRoadNetwork(n, roads) = false.

Here's how the road system can be represented:


As you can see, it's only possible to travel from city 3 to city 4 by traversing at least 3 roads.

Input/Output

[execution time limit] 7 seconds (py3)

[input] integer n

The number of cities in the kingdom.

Guaranteed constraints:
1 ≤ n ≤ 250.

[input] array.array.integer roads

Array of roads in the kingdom. Each road is given as a pair [cityi, cityj], where 0 ≤ cityi, cityj < n and cityi ≠ cityj. It is guaranteed that no road is given twice.

Guaranteed constraints:
0 ≤ roads.length ≤ 35000,
roads[i].length = 2,
0 ≤ roads[i][j] < n.

[output] boolean

true if the road system is efficient, false otherwise.
"""

n = 6
roads = [[3, 0], [0, 4], [5, 0], [2, 1],
         [1, 4], [2, 3], [5, 2]]

tester = [
    [0, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
]


# roads = [[0, 4], [5, 0], [2, 1],
#          [1, 4], [2, 3], [5, 2]]
#
# roads = [[0, 1],
#          [0, 2],
#          [3, 4]]

# my first passing solution with help but still not passing 100% of tests
# def efficientRoadNetwork(n, roads):
#     if not roads:
#         return True
#     if n == 0:
#         return True
#     graph = {}
#     for i in range(n):
#         graph[str(i)] = set()
#     for road in roads:
#         graph[str(road[0])].add(str(road[1]))
#         graph[str(road[1])].add(str(road[0]))
#
#
#     def bfs(graph, S, D):
#         queue = [(S, [S])]
#         while queue:
#             (vertex, path) = queue.pop(0)
#             for next in graph[vertex] - set(path):
#                 if next == D:
#                     yield path + [next]
#                 else:
#                     queue.append((next, path + [next]))
#
#     def shortest(graph, S, D):
#         try:
#             return next(bfs(graph, S, D))
#         except StopIteration:
#             return None
#
#     for i in range(len(graph)):
#         for j in range(1, len(graph)):
#             if i != j:
#                 result = (shortest(graph, str(i), str(j)))
#                 if result is None:
#                     return False
#                 if len(result) > n + 1:
#                     return False
#     return True


# solution from google
# def efficientRoadNetwork(n, roads):
#     graph = [[1] * n for x in range(n)]
#     print(graph)
#     for i in range(n):
#         graph[i][i] = 0
#     for i, j in roads:
#         graph[i][j] = 1
#         graph[j][i] = 1
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if graph[i][j] > graph[i][k] + graph[k][j]:
#                     graph[i][j] = graphy[i][k] + graph[k][j]
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] >= 3:
#                 return False
#     return True

# solution with most votes
def efficientRoadNetwork(n, roads):
    adj = [[] for i in range(n)]
    for rd in roads:
        adj[rd[0]].append(rd[1])
        adj[rd[1]].append(rd[0])
    print(adj)
    for city in range(n - 1):
        oneHop = {c for c in adj[city]}
        print(oneHop)
        twoHops = {c for c1 in oneHop for c in adj[c1]}
        print(twoHops)
        if len({city} | oneHop | twoHops) < n:
            return False
    return True


# print(efficientRoadNetwork(n, roads))


