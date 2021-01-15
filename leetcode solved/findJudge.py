"""
997. Find the Town Judge
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.



Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
"""

N = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]


def findJudge(N, trust):
    # initialize dict to hold trust relationships
    trusted = {}
    # create an empty trusted array for each person (N) in the trusted dict
    for i in range(1, N + 1):
        trusted[i] = []
    # add the relationships to the dict
    for groups in range(len(trust)):
        if trust[groups][0] not in trusted:
            trusted[trust[groups][0]] = []
        trusted[trust[groups][0]].append(trust[groups][1])
    # initialize the judge to not exist
    judge = -1
    # iterate the trusted relationships
    for person in trusted:
        # if someone trusts nobody
        if trusted[person] == []:
            # set the judge to that person
            judge = person
            # check to see if everyone else trusts that pers
    for person in trusted:
        # if anyone does not trust the judge return -1 there is no judge
        if judge not in trusted[person] and person != judge:
            return -1
    # if we reach the end the judge is valid
    return judge

# print(findJudge(N, trust))
