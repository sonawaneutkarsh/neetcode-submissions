# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        if not root:
            return 0
        
        depthLeft= self.diameterOfBinaryTree(root.left)
        depthRight= self.diameterOfBinaryTree(root.right)
        diameter= depthLeft+depthRight #should i add +2 so that it counts current node

        return diameter
        '''
        self.res=0 #why is self needed
        def dfs(curr):
            if not curr:
                return 0

            left=dfs(curr.left)
            right=dfs(curr.right)

            self.res=max(self.res, left+right)
            return max(left,right)+1
        dfs(root)
        return self.res
            
