
"""
*** Roads Building ***
----------------------
Once upon a time, in a kingdom far, far away, there lived a King Byteasar II. There was nothing special about him or his kingdom. As a mediocre ruler, he preferred hunting and feasting over doing anything about his kingdom's prosperity.

Luckily, his adviser, the wise magician Bitlin, worked for the kingdom's welfare day and night. However, since there was no one to advise him, he completely forgot about one important thing: the roads! Over the years most of the two-way roads built by Byteasar's predecessors were forgotten and no longer traversable. Only a few roads can still be used.

Bitlin wanted each pair of cities to be connected, but couldn't find a way to figure out which roads are missing. Desperate, he turned to his magic crystal ball for help. The crystal showed him a programmer from the distant future: you! Now you're the only one who can save the kingdom. Given the existing roads and the number of cities in the kingdom, you should use the most modern technologies and find out which roads should be built again to connect each pair of cities. Since the crystal ball is quite old and meticulous, it will only transfer the information if it is sorted properly.

The roads to be built should be returned in an array sorted lexicographically, with each road stored as [cityi, cityj], where cityi < cityj.

Example

For cities = 4 and roads = [[0, 1], [1, 2], [2, 0]],
the output should be
roadsBuilding(cities, roads) = [[0, 3], [1, 3], [2, 3]].

See the image below: the existing roads are colored black, and the ones to be built are colored red.


Input/Output

[execution time limit] 4 seconds (py3)

[input] integer cities

The number of cities in the kingdom.

Guaranteed constraints:
1 ≤ cities ≤ 100.

[input] array.array.integer roads

Array of roads in the kingdom. Each road is given as a pair [cityi, cityj], where 0 ≤ cityi, cityj < cities and cityi ≠ cityj. It is guaranteed that no road is given twice.

Guaranteed constraints:
0 ≤ roads.length ≤ 5000,
roads[i].length = 2,
0 ≤ roads[i][j] < cities.

[output] array.array.integer

A unique array of roads that should be built sorted as described above. There's no need to build looping roads, i.e. roads that lead back from a city to itself.
"""

cities = 4
roads = [
    [0, 1],
    [1, 2],
    [2, 0]
]

# cities = 9
# roads = [
#     [5, 8],
#     [6, 0],
#     [0, 5],
#     [4, 1],
#     [0, 1],
#     [7, 0],
#     [6, 8],
#     [7, 3],
#     [2, 6],
#     [0, 2],
#     [0, 3],
#     [8, 7],
#     [5, 4],
#     [8, 4],
#     [8, 2],
#     [7, 1],
#     [4, 6],
#     [5, 6],
#     [4, 2],
#     [4, 7],
#     [2, 7],
#     [3, 6],
#     [8, 0],
#     [1, 6],
#     [3, 2],
#     [3, 4],
#     [4, 0],
#     [6, 7],
#     [5, 7]]

# my solution (no google)
import pprint


def roadsBuilding(cities, roads):
    road_dict = {}
    result = []
    for i in range(cities):
        road_dict[i] = set()
    for road in roads:
        road_dict[road[0]].add(road[1])
        road_dict[road[1]].add(road[0])

    for key in road_dict:
        if road_dict[key] == set():
            continue
        for city in road_dict:
            road = []
            if city not in road_dict[key] and city != key:
                road_dict[key].add(city)
                road.append(key)
                road.append(city)
                if road and sorted(road) not in result:
                    result.append(road)

    return result


# solutions with highest votes
def roadsBuilding(cities, roads):
    roads = set([tuple(road) for road in roads])
    print(roads)
    toBuild = []
    for i in range(0, cities - 1):
        for j in range(i + 1, cities):
            if (i, j) not in roads and (j, i) not in roads:
                toBuild.append([i, j])
    return toBuild


# print(roadsBuilding(cities, roads))
