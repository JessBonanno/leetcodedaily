"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.


Example 1:


Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
Time from [1,1] to [3,4] = 3 seconds
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
Example 2:

Input: points = [[3,2],[-2,2]]
Output: 5
"""

points = [[3, 2], [-2, 2]]


# points = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]
# Output
# 43394

# TODO complete this solution, its not working properly with negative
#  differences
def minTimeToVisitAllPoints(points):
    # if idx1 and idx2 increment equally its diagonal move ( 1 sec ) per
    # increase
    # if idx1 only +1 its vertical move (1 sec)
    # if idx2 only +1 its horizontal move (1 sec)

    # get idx increments and idx 2 increments
    # move diagonally for times they are equal
    # move vertically for times idx 1 is greater
    # move horizontally for times idx 2 is greater

    total_moves = 0
    for i in range(len(points) - 1):
        idx_1_moves = points[i + 1][0] - points[i][0]
        idx_2_moves = points[i + 1][1] - points[i][1]
        diagonal = abs(min(idx_1_moves, idx_2_moves))
        vertical = 0
        horizontal = 0

        if idx_1_moves > idx_2_moves > 0:
            vertical = abs(idx_1_moves - idx_2_moves)
        elif idx_2_moves > idx_1_moves > 0:
            horizontal = abs(idx_2_moves - idx_1_moves)

        total_moves += diagonal + vertical + horizontal
        print('idx1 moves:', idx_1_moves, 'idx2 moves:', idx_2_moves)
        print('diagonal:', diagonal)
        print('vertical:', vertical)
        print('horizontal:', horizontal)

    return total_moves


# print(
#     f'minTimeToVisitAllPoints([[3,2],[-2,2]])'
#     f':{minTimeToVisitAllPoints(points)}')



