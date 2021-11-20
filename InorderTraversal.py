https://leetcode.com/problems/binary-tree-inorder-traversal/
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# left root right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        nodes = []
        
        def traverse(root):
            if root:
                print(traverse(root.left))
                nodes.append(root.val)
                print(nodes)
                print(traverse(root.right))
                
        traverse(root)
        
        return nodes
    
