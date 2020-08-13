'''
现在的第一个程序是这样：
输入：中意者的qq号码的列表的列表。（每个人都有自己的列表）
输出：所能形成三元组的列表。
'''

# I是输入
I = {
    1:[2,3,5,6],     # 1号成员希望与2,3,5,6组队
    2:[1,3,4],
    3:[1,2,4],
    4:[1,2,3,5,6],
    5:[1,4,6],
    6:[1,4,5],
}

K = I.keys()  # 所有参加的人

G=[(x,y) for x in I.keys() for y in I[x] ]   # 图的本质是关系，关系的本质是序对的集合

from itertools import combinations   # 用来生成全部可能的3组合

print(
    # 对每个可能的3元组进行考察，如果符合条件就列出来
    [set([a,b,c]) for (a,b,c) in combinations(K, 3)
             if  (a,b) in G
             and (b,a) in G
             and (a,c) in G 
             and (c,a) in G
             and (b,c) in G 
             and (c,b) in G
    ]
)