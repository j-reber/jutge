import random
from yogi import scan


class Node:
    def __init__(self, key, s):
        self.key = key
        self.priority = random.randint(0, 2 ** 31)
        self.count = 1
        self.string_count = len(s)
        self.string = s
        self.left = None
        self.right = None


def size(t):
    return t.count if t else 0


def string_size(t):
    return t.string_count if t else 0


def update(t):
    t.count = 1 + size(t.left) + size(t.right)
    return t


def update_string(t):
    t.string_count = len(t.string) + string_size(t.left) + string_size(t.right)
    return t


def split(x, t):
    if t is None:
        return None, None, None
    elif x < t.key:
        l, r, f = split(x, t.left)
        t.left = r
        return l, update_string(update(t)), f
    elif x > t.key:
        l, r, f = split(x, t.right)
        t.right = l
        return update_string(update(t)), r, f
    else:
        return t.left, t.right, t


def merge(l, r):
    if l is None:
        return r
    if r is None:
        return l
    if l.priority > r.priority:
        l.right = merge(l.right, r)
        return update_string(update(l))
    else:
        r.left = merge(l, r.left)
        return update_string(update(r))


def increase(t):
    if t:
        t.key += 1
        increase(t.left)
        increase(t.right)


def insert(x, t, s):
    l, r, f = split(x, t)
    if f:
        r = merge(f, r)
    increase(r)
    new_node = Node(x, s)
    return merge(merge(l, new_node), r)


def find_ith(i, t):
    s = size(t.left)
    if i < s:
        return find_ith(i, t.left)
    elif i > s:
        return find_ith(i - s - 1, t.right)
    else:
        return t


def find_string_ith(i, t):
    if t is None:
        return ''
    s = string_size(t.left)
    if i < s:
        return find_string_ith(i, t.left)
    elif i < s + len(t.string):
        return t.string[i - s]
    else:
        return find_string_ith(i - s - len(t.string), t.right)


def compute_rank(x, t):
    if t is None:
        return 0
    s = size(t.left)
    if x < t.key:
        return compute_rank(x, t.left)
    elif x > t.key:
        return s + 1 + compute_rank(x, t.right)
    else:
        return s


def main():
    t = None
    x = scan(str)
    output = ""
    while True:
        try:
            if x == "E":
                print(output)
                break
            elif x == "I":
                s = scan(str)
                i = scan(int)
                t = insert(i, t, s)
            elif x == "C":
                i = scan(int)
                result = find_string_ith(i, t)
                output += result
            x = scan(str)
        except EOFError:
            break


if __name__ == "__main__":
    main()
