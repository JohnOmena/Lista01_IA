import copy

from dfs import valid, move
from puzzle import hashing, compare, make_frontier, heuristic
from heapq import heappop, heappush



def a_star_search(board, p):
    l = {}
    q = []
    heappush(q, (0, board))
    comparisons = 0
    while q:
        v = heappop(q)
        current_price = v[0]
        u = v[1]
        x = hashing(u)
        if l.get(x, -1) != -1:
            continue
        l[x] = 1
        if len(q) > 65:
            q = q[:65]

        if compare(u, p) == 0:
            print("Found with: ",comparisons)
            return u
        else:
            frontier = make_frontier(u)
            for i in frontier:
                border = move(copy.deepcopy(u), i[0], i[1])
                heappush(q,(current_price+heuristic(border,p),border))
            comparisons += 1

    return None