from DataStructures.BinarySearchTree import BinarySearchTree
from DataStructures.Graph import Graph
from DataStructures.Stack import Stack
from DataStructures.Trie import Trie


def example1():
    t = BinarySearchTree()
    print("---[ Binary Search Tree Insert ]---")
    t.insert(8)
    t.insert(3)
    t.insert(10)
    t.insert(1)
    t.insert(6)
    t.insert(14)
    t.insert(4)
    t.insert(7)
    t.insert(13)
    print("---[ Binary Search Tree Contains ]---")
    if t.contains(7):
        print("t contains 7")
    else:
        print("t does not contain 7")
    print("---[ Binary Search Tree Pre Order Traversal ]---")
    t.pre_order_traversal()
    print("---[ Binary Search Tree In Order Traversal ]---")
    t.in_order_traversal()
    print("---[ Binary Search Tree Post Order Traversal ]---")
    t.post_order_traversal()


def example2():
    g = Graph()
    g.edges = {
        "A": ["B"],
        "B": ["C"],
        "C": ["B", "D", "F"],
        "D": ["C", "E"],
        "E": ["F"],
        "F": [],
    }
    print("---[ Graph BFS ]---")
    path1 = g.bfs("A", "D")
    path2 = g.bfs("E", "D")
    print("BFS A -> D", path1)
    print("BFS E -> D", path2)
    print("---[ Graph DFS ]---")
    path3 = g.dfs("A", "D")
    path4 = g.dfs("E", "D")
    print("DFS A -> D", path3)
    print("DFS E -> D", path4)


def example3():
    s = Stack()
    print("---[ Stack Push ]---")
    for _ in range(1, 7):
        print(_)
        s.push(_)
    print("---[ Stack Pop ]---")
    for _ in range(1, 7):
        n = s.pop()
        print(n)


def example4():
    t = Trie()
    strings = ["A", "to", "tea", "ted", "ten", "i", "in", "inn"]
    print("---[ Trie Insert ]---")
    for string in strings:
        t.insert(string)
    print("---[ Trie Contains ]---")
    for string in strings:
        r = t.contains(string)
        print(r)


def main():
    example1()
    example2()
    example3()
    example4()


if __name__ == "__main__":
    main()
