from a_star import a_star_search
from bfs import bfs
from puzzle import *
from  dfs import *

x = start(16)
y = start(8)

print("8x8 board:\n")
bfs(y, 8)
dfs_depth_limited(y, 1000,8)
a_star_search(y, 8)
print("\n===========\n15x15 board:\n")
a_star_search(x,16)
