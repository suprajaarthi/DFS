https://leetcode.com/problems/balanced-binary-tree/
  
class Solution(object):
    def isBalanced(self, root):
        def calculate(node):
            print(node)
            if not node: return 0
            myself = 1
            left = calculate(node.left)
            print(left)
            right = calculate(node.right)
            print(right)
            if left < 0 or right < 0: return -1
            if abs(left - right) > 1: return -1
            print(myself+max(left,right))
            return 1 + max(left, right)
                                
        return False if calculate(root) < 0 else True
      
      
# Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:

#       3
#       |
#     9   20
#         | 
#       15   7
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:
#       1
#       |
#     2   2
#     |
#   3  3
#   |
# 4  4 


# Input: root = []
# Output: true
