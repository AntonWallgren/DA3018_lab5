class Node:
    def __init__(self, key, val):
        self.__key = key
        self.__val = val
        self.__left = None
        self.__right = None
        self.__parent = None

    def set_children(self, l, r):
        self.__left = l
        self.__right = r

    def set_parent(self, p):
        self.__parent = p

    def data(self):
        return self.__key, self.__val

    def left_child(self):
        return self.__left

    def right_child(self):
        return self.__right

    def parent(self):
        return self.__parent

    def set_val(self, value): # ??
        self.__val = value

    def __str__(self):
        return str(self.__key+' '+str(self.__val))


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        '''
        Public interface method to insert a key and value to the search tree.
        '''
        self.root = self.__insert(self.root, key, val)

    def __insert(self, v, key, val):
        '''
        Internal method to recursively decide where to insert a new node.
        '''
        if v:
            v_key, x = v.data() # x is ignored
            left = v.left_child()
            right = v.right_child()
            if key < v_key:
                left = self.__insert(left, key, val)
            elif key == v_key:
                v._Node__val = val
            else:
                right = self.__insert(right, key, val)
            v.set_children(left, right)
            if left:
                v.left_child()._Node__parent = v
            if right:
                v.right_child()._Node__parent = v
            return v
        else:
            return Node(key, val)

    def find(self, key):
        return self.__find(self.root, key) # Return only the value?

    def __find(self, v, key):
        if v:
            v_key, x = v.data() # x is ignored
            if key == v_key:
                return v # Return the node
            elif key < v_key:
                return self.__find(v.left_child(), key)
            else:
                return self.__find(v.right_child(), key)
        else:
            raise KeyError

    def __replace(self, u, v):
        if u.parent():
            if u == u.parent().left_child():
                l = v
                r = u.parent().right_child()
                u.parent().set_children(l, r)
            else:
                l = u.parent().left_child()
                r = v
                u.parent().set_children(l, r)
        else:
            self.root = v
        if v:
            v.set_parent(u.parent())

    def remove(self, key):
        v = self.__find(self.root, key)
        if v.left_child() and v.right_child():
            x = self.__min(v.right_child())
            if x.parent() != v:
                self.__replace(x, x.right_child())
                l = x.left_child()
                r = v.right_child()
                x.set_children(l, r)
                x.right_child().set_parent(x)
            self.__replace(v, x)
            l = v.left_child()
            r = x.right_child()
            x.set_children(l, r)
            x.left_child().set_parent(x)
        else:
            if v.left_child():
                self.__replace(v, v.left_child())
            else:
                self.__replace(v, v.right_child())

    def size(self):
        return self.__size(self.root)

    def __size(self, v):
        if v:
            return 1 + self.__size(v.left_child()) + self.__size(v.right_child())
        else:
            return 0

    def min(self):
        return self.__min(self.root)

    def __min(self, v):
        if v.left_child():
            return self.__min(v.left_child())
        return v

    def max(self):
        return self.__max(self.root)

    def __max(self, v):
        if v.right_child():
            return self.__max(v.right_child())
        return v

    def __in_order_walk(self, v):
        if v:
            yield from self.__in_order_walk(v.left_child())
            yield v.data()
            yield from self.__in_order_walk(v.right_child())

    def __str__(self):
        return str(self.root)

    def __iter__(self):
        return self.__in_order_walk(self.root)

    def __getitem__(self, key):
        return self.find(key)

    def __setitem__(self, key, value):
        v = self.find(key)
        v.set_val(value)

def main():
    credits = BinarySearchTree()
    credits.insert('DA3018', 7.5)
    credits.insert('DA3018', 10)
    credits.insert('DA2004', 7.5)
    credits.insert('DA2006', 7.5)
    credits.insert('DA2005', 7.5)
    credits.insert('DA2003', 6)
    credits.insert('DA4003', 7.5)
    # print(credits)
    n = credits.size()          # n = 6
    hp = credits.find('DA2005') # set hp to 7.5
    # credits.remove('DA2004')
    m = credits.size()          # m = 5
    # print(credits._BinarySearchTree__find(credits.root, 'DA2005')._Node__parent)
    # print(n, m)
    # print(credits.min())
    # print(credits.max())
    for course, hp in credits:
         print(course)
    # for i in credits:
    #     print(i)
    print(credits['DA2004'])
    credits['DA2004'] = 15
    print(credits['DA2004'])
    print(hp)

if __name__ == '__main__':
    main()
