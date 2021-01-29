from TreeNode import TreeNode


class AVL_Tree():

    def __init__(self):
        self._list = []

    def Insert(self, root, TC, customer):
        if not root:
            return TreeNode(TC, customer)
        elif TC < root.TC:
            root.left = self.Insert(root.left, TC, customer)
        else:
            root.right = self.Insert(root.right, TC, customer)

        balance = self.GetBalance(root)

        if balance > 1 and TC < root.left.TC:
            return self.LL_Rotate(root)

        if balance > 1 and TC > root.left.TC:
            return self.LR_Rotate(root)

        if balance < -1 and TC > root.right.TC:
            return self.RR_Rotate(root)

        if balance < -1 and TC < root.right.TC:
            return self.RL_Rotate(root)

        return root

    def LL_Rotate(self, x):
        y = x.left
        z = y.right

        y.right = x
        x.left = z
        return y

    def RR_Rotate(self, x):
        y = x.right
        z = y.left

        y.left = x
        x.right = z
        return y

    def LR_Rotate(self, x):
        x.left = self.RR_Rotate(x.left)
        return self.LL_Rotate(x)

    def RL_Rotate(self, x):
        x.right = self.LL_Rotate(x.right)
        return self.RR_Rotate(x)

    def Height(self, root):
        if root:
            left = self.Height(root.left)
            right = self.Height(root.right)
            return 1+max(right, left)
        else:
            return -1

    def GetBalance(self, root):
        if root:
            return self.Height(root.left) - self.Height(root.right)
        else:
            return -1

    def Search(self, TC, root):
        if not root:
            return None
        elif TC < root.TC:
            return self.Search(TC, root.left)
        elif TC > root.TC:
            return self.Search(TC, root.right)
        elif TC == root.TC:
            return root
        else:
            return -1

    def ReadCustomer(self, root):

        if root:
            self._list.append(root)
            self.ReadCustomer(root.left)
            self.ReadCustomer(root.right)
        return self._list

    def Read(self, root):
        self._list = []
        return self.ReadCustomer(root)

    def GetMinValue(self, root):
        if root is None or root.left is None:
            return root
        return root.left

    def delete(self, root, TC):
        if not root:
            return root
        elif TC < root.TC:
            root.left = self.delete(root.left, TC)
        elif TC > root.TC:
            root.right = self.delete(root.right, TC)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.GetMinValue(root.right)
            root.TC = temp.TC
            root.Customer = temp.Customer
            root.Right = self.delete(root.right, temp.TC)

        if root is None:
            return root

        balance = self.GetBalance(root)

        if balance > 1 and TC < root.left.TC:
            return self.LL_Rotate(root)

        if balance > 1 and TC > root.left.TC:
            return self.LR_Rotate(root)

        if balance < -1 and TC > root.right.TC:
            return self.RR_Rotate(root)

        if balance < -1 and TC < root.right.TC:
            return self.RL_Rotate(root)

        return root
