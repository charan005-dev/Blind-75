#TC: O(n) #SC:O(n)  - serialize
#TC: O(n) #SC: O(n) - deserialize


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """  

        #level order traversal with conversion to strings , size parameter not needed as we aren't operating through levels
        if not root:
            return ""
        result = []
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))
            else:
                result.append("null")


        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        i = 0
        q = deque()
        root = TreeNode(int(data[0]))
        q.append(root)
        i+=1
        while q:
            node = q.popleft()
            #left
            if data[i] != "null": # if (!data[i].equals("null"))
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i+=1

            #right
            if data[i] != "null": # if (!data[i].equals("null"))
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
            i+=1

        return root