class Bintree:
    def __init__(self):
        self.root = None

    def put(self,  newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue)

    def __contains__(self, value):
        # True om value finns i trädet, False annars
        return finns(self.root, value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


def putta(current, newvalue):                      # sorterar och lägger in en nod
    if current is None:
        current = Node(newvalue)
    else:
        if newvalue < current.value:
            if current.left:                        # pekar roten på en nod till vänster?
                putta(current.left, newvalue)       # rekursivt
            else:
                current.left = Node(newvalue)
        elif newvalue > current.value:
            if current.right:
                putta(current.right, newvalue)
            else:
                current.right = Node(newvalue)
    return current


def finns(current, value):                        # finns värdet i trädet?
    if current is None:
        return False
    if value == current.value:
        return True
    if value < current.value:
        return finns(current.left, value)
    if value > current.value:
        return finns(current.right, value)


def skriv(current):              # skriver ut trädet inorder
    if current is not None:
        skriv(current.left)
        print(current.value)
        skriv(current.right)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



