'''
https://leetcode.com/problems/recover-binary-search-tree/?envType=problem-list-v2&envId=binary-tree
'''

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first, second, prev = None, None, None
        def verify():
            nonlocal root, first, second, prev
            if not prev or prev.val < root.val: 
                prev = root
                return
            if not first:
                first = prev
                second = root
            else: 
                second = root
        def morris():
            nonlocal root
            while root: 
                if root.left:
                    pre = root.left
                    while pre.right and pre.right is not root: pre = pre.right
                    if pre.right:
                        verify()
                        pre.right = None
                        root = root.right
                    else: 
                        pre.right = root
                        root = root.left
                else:
                    verify()
                    root = root.right
        morris()
        first.val, second.val = second.val, first.val