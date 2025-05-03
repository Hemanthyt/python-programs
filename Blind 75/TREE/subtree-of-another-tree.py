class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def sameTree(self,root,subroot):
        if not root and not subroot:
            return True
        if root and subroot and root.val==subroot.val:
            return self.sameTree(root.left,subroot.left) and self.sameTree(root.right,subroot.right)
        else:
            return False
