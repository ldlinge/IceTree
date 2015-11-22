from itertools import chain, imap, ifilter


class Tree(object):
    def __init__(self, value):
        self.value = value
        self.children = []  # Will return empty list if node has no children
        self.parent = None  # Will None if node is root of the tree

    def __iter__(self):
        for node in chain(*imap(iter, self.children)):
            yield node
        yield self

    def preorder_iter(self):
        yield self
        for node in chain(*imap(iter, self.children)):
            yield node

    def ancestors_iter(self):
        c = self
        while c.parent:
            yield c
            c = c.parent
        yield c

    # We generally don't use setters and getters in python because of overhead and making code unclean
    #def getChildren(self):
    #    return self.children

    # We generally don't use setters and getters in python because of overhead and making code unclean
    #def getParent(self):
    #        return self.parent

    def add_child(self, obj):
        self.children.append(obj)
        obj.parent = self

    def isInTree(self, node):
        for n in self:
            if (isinstance(node, Tree) and node == n) or node == n.value:
                return True
        return False



root = Tree('Root')
for i in range(4):
    root.add_child(Tree('Level_1-'+str(i+1)))
    root.add_child(Tree(i+1))
    root.children[i].add_child(Tree('Level_2-'+str(i+5)))

str_decendants = []
for node in root:
    if type(node.value) is str:
        str_decendants.append(node.value)
print '\nDescendants that are of type "str":'
print str_decendants

print '\nAlternative filter iterator to apply condition on the iterator to grab node with value type "str"'
print 'This allows us to define the condition for the iteration'
def is_str(x):
    return isinstance(x.value, str)

str_decendants2 = ''
for i in ifilter(is_str, root):
    str_decendants2 += i.value
print str_decendants2

str_ancestors = ''
for node in root.children[0].children[0].ancestors_iter():
    str_ancestors += str(node.value)
print '\nAncestors "toString":'
print str_ancestors

int_decendants = []
for node in root:
    if type(node.value) is int:
        int_decendants.append(node.value)
print '\nDecendants of type "int":'
print int_decendants

root2 = Tree('Root 2')
print '\nRoot 2 children:'
print root2.children