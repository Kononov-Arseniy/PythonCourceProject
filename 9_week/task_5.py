'''
https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/?envType=problem-list-v2&envId=binary-tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph=collections.defaultdict(list)
        visit=set()
        def dfs(node):
            if node: 
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        q=collections.deque([start])
        res=-1
        while q:
            for i in range(len(q)):
                val=q.popleft()
                visit.add(val)
                for n in graph[val]:
                    if n not in visit:
                        q.append(n)
            res+=1
        return res