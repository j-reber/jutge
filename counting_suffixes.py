from yogi import tokens
import re


class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.mid = None
        self.right = None
        self.value = None


class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.search(key):  # Strings can only be inserted once
            self.root = self._insert_node(self.root, key, 0)

    def _insert_node(self, node, key, index):
        if node is None:
            node = TSTNode(key[index])

        if key[index] < node.char:
            node.left = self._insert_node(node.left, key, index)
        elif key[index] > node.char:
            node.right = self._insert_node(node.right, key, index)
        else:
            if index == len(key) - 1:
                if node.value is None:
                    node.value = key
            else:
                node.mid = self._insert_node(node.mid, key, index + 1)

        return node

    def erase(self, key):
        if self.search(key):
            self.root = self._erase_node(self.root, key, 0)

    def _erase_node(self, node, key, index):
        if node is None:
            return None

        if key[index] < node.char:
            node.left = self._erase_node(node.left, key, index)
        elif key[index] > node.char:
            node.right = self._erase_node(node.right, key, index)
        else:
            if index == len(key) - 1:
                if node.value:
                    node.value = None
            else:
                node.mid = self._erase_node(node.mid, key, index + 1)

        if not node.value and not node.left and not node.mid and not node.right:
            return None

        return node

    def suffixes(self, node):
        if node is not None:
            if node.left is None and node.right is None and node.mid is None:
                yield node.char

            if node.left:
                for s in self.suffixes(node.left):
                    yield s
            if node.right:
                for s in self.suffixes(node.right):
                    yield s
            if node.mid:
                for s in self.suffixes(node.mid):
                    yield node.char + s

    def autocompletes(self, node, string):
        if node is None or len(string) == 0:
            return []

        head = string[0]
        tail = string[1:]
        if head < node.char:
            return self.autocompletes(node.left, string)
        elif head > node.char:
            return self.autocompletes(node.right, string)
        else:
            if len(tail) == 0:
                # found the node containing the prefix string,
                # so get all the possible suffixes underneath
                return self.suffixes(node.mid)
            return self.autocompletes(node.mid, string[1:])

    def autocomplete(self, string):
        return map(lambda l: string + l, self.autocompletes(self.root, string))

    def count_prefix(self, string):
        if self.search(string):
            return len(list(self.autocomplete(string))) + 1
        else:
            return len(list(self.autocomplete(string)))

    def reset(self):
        self.root = None

    def search(self, key):
        node = self._search_node(self.root, key, 0)
        return node.value if node else None

    def _search_node(self, node, key, index):
        if node is None or index >= len(key):
            return None

        if key[index] < node.char:
            return self._search_node(node.left, key, index)
        elif key[index] > node.char:
            return self._search_node(node.right, key, index)
        else:
            if index == len(key) - 1:
                return node if node.value else None
            return self._search_node(node.mid, key, index + 1)

    def visualize(self):
        lines = self._generate_visualization(self.root, [], "", "")
        for line in lines:
            print(line)

    def _generate_visualization(self, node, lines, prefix, child_prefix):
        if node is None:
            return lines

        lines.append(f"{prefix}{node.char}")

        if node.value:
            lines.append(f"{child_prefix}└── {node.value}")

        if node.left or node.mid or node.right:
            if node.left:
                lines = self._generate_visualization(node.left, lines, f"{child_prefix}├── ", f"{child_prefix}|   ")
            if node.mid:
                lines = self._generate_visualization(node.mid, lines, f"{child_prefix}├── ", f"{child_prefix}|   ")
            if node.right:
                lines = self._generate_visualization(node.right, lines, f"{child_prefix}└── ", f"{child_prefix}    ")

        return lines


# Example usage:
if __name__ == '__main__':
    cmds, args = [], []
    for i, x in enumerate(tokens(str)):
        if x.isupper():
            if x == "R":
                args.append("")
            cmds.append(x)
        else:
            args.append(x[::-1])  # Invert strings so they become suffixes become prefixes

    tst = TernarySearchTree()
    for i, cmd in enumerate(cmds):
        if cmd == 'I':
            tst.insert(args[i])
        elif cmd == 'E':
            tst.erase(args[i])
        elif cmd == 'C':
            cnt = tst.count_prefix(args[i])
            print(cnt)
        elif cmd == 'R':
            tst.reset()
            print('---')
            # print('Reseted')
        else:
            continue
    # # tst.visualize()

    # tst.erase("a")
    # tst.insert("abba")
    # print(tst.count_prefix("a"))
    # # print(list(tst.autocomplete("a")))
    # tst.insert("abc")
    # print(tst.count_prefix("abc"))
    # # print(list(tst.autocomplete("abc")))
    # print(tst.count_prefix("abba"))
    # # print(list(tst.autocomplete("abba")))
    # print(tst.count_prefix("a"))
    # # print(list(tst.autocomplete("a")))
    # print(tst.count_prefix("ab"))
    # # print(list(tst.autocomplete("ab")))
    # tst.insert("abba")
    # print(tst.count_prefix("ab"))
    # # print(list(tst.autocomplete("ab")))
    # tst.erase("abc")
    # print(tst.count_prefix("abc"))
    # # print(list(tst.autocomplete("abc")))
    # print(tst.count_prefix("ab"))
    # # print(list(tst.autocomplete("ab")))
    #
    # tst.erase("ab")
    # print(tst.count_prefix("ab"))
    # # print(list(tst.autocomplete("ab")))

    # tst.reset()
    # print("___")
    # print(tst.count_prefix("ab"))
    # # print(list(tst.autocomplete("ab")))
    #
    # tst.insert("sgge")
    # tst.insert("sggezz")
    # print(tst.count_prefix("sgge"))
    # # print(list(tst.autocomplete("sgge")))
    # tst.erase("sgge")
    # print(tst.count_prefix("sgge"))
    # print(list(tst.autocomplete("sgge")))

    # tst.insert("asdf")
    # tst.insert("abba")
    # tst.insert("adf")
    # tst.insert('hqhqhq')
    # # tst.erase()
    # print(list(tst.autocomplete("asdf")))
    # # tst.visualize()
    # # tst.erase("abba")
    # # tst.visualize()
