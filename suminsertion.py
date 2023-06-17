import random
from yogi import scan, tokens


class Node:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(0, 2 ** 31)
        self.count = 1
        self.sum = key
        self.left = None
        self.right = None


def size(t):
    return t.count if t else 0


def update(t):
    t.count = 1 + size(t.left) + size(t.right)
    return t


def sum(t):
    return t.sum if t else 0


def updateSum(t):
    t.sum = t.key + sum(t.left) + sum(t.right)
    return t


def split(x, t):
    if t is None:
        return None, None
    elif x < t.key:
        l, t.left = split(x, t.left)
        r = updateSum(t)
        return l, r
    elif x > t.key:
        t.right, r = split(x, t.right)
        l = updateSum(t)
        return l, r
    else:
        l = t.left
        r = t.right
        del t
        return l, r


def merge(l, r):
    if l is None:
        return r
    if r is None:
        return l
    if l.priority > r.priority:
        l.right = merge(l.right, r)
        return updateSum(l)
    else:
        r.left = merge(l, r.left)
        return updateSum(r)


def insert(x, t):
    l, r = split(x, t)
    new_node = Node(x)
    return merge(merge(l, new_node), r)


def erase(x, t):
    l, r = split(x, t)
    return merge(l, r)


def find_ith(i, t):
    s = size(t.left)
    if i < s:
        return find_ith(i, t.left)
    elif i > s:
        return find_ith(i - s - 1, t.right)
    else:
        return t.key


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


def print_tree(t, sp):
    if t:
        print_tree(t.right, sp + 2)
        print(' ' * sp + str(t.key), t.priority, t.count)
        print_tree(t.left, sp + 2)


def contains(x, t):
    if t is None:
        return False
    if x < t.key:
        return contains(x, t.left)
    if x > t.key:
        return contains(x, t.right)
    return True


if __name__ == "__main__":
    # output = ""
    # iterator = enumerate(tokens(int))
    # for n in iterator:
    #     # try:
    #     if n is None:
    #         continue
    #     if n == 0:
    #         break
    #
    #     t = None
    #     t = insert(0, t)
    #     for _ in range(n):
    #         # y = scan(int)
    #         # i = scan(int)
    #         # j = scan(int)
    #         y = next(iterator)
    #         i = next(iterator)
    #         j = next(iterator)
    #         print(n, y, i, j)
    #
    #         l, m, r = None, None, None
    #         ith = find_ith(i - 1, t)
    #         jth = find_ith(j - 1, t)
    #         l, m = split(ith, t)
    #         m, r = split(jth, m)
    #         csum = ((ith if ith == jth else ith + jth) + y + sum(m)) % 1000000000
    #         t = merge(l, merge(m, r))
    #         t = insert(ith, t)
    #         if ith != jth:
    #             t = insert(jth, t)
    #         if contains(csum, t):
    #             output += "R " + str(csum) + "\n"
    #         else:
    #             t = insert(csum, t)
    #             output += "I " + str(csum) + "\n"
    #     output += "-" * 10 + "\n"
    # # except ValueError:
    # #     continue
    # # x = scan(str)
    # # print(type(x))
    # print(output[:-1])

    n_s = []
    aux_3 = []
    aux_n = []
    tot = []
    iterator = enumerate(tokens(int))
    for _, n in iterator:
        if n is None:
            continue
        if n == 0:
            break
        n_s.append(n)
        for _ in range(n):
            _, y_in = next(iterator)
            _, i_in = next(iterator)
            _, j_in = next(iterator)
            aux_3 = [y_in, i_in, j_in]
            aux_n.append(aux_3)
            aux_3 = []
        tot.append(aux_n)
        aux_n = []

    output = ""
    for block in tot:
        t = None
        t = insert(0, t)
        for line in block:
            y, i, j = line[0], line[1], line[2]
            l, m, r = None, None, None
            ith = find_ith(i - 1, t)
            jth = find_ith(j - 1, t)
            l, m = split(ith, t)
            m, r = split(jth, m)
            csum = ((ith if ith == jth else ith + jth) + y + sum(m)) % 1000000000
            t = merge(l, merge(m, r))
            t = insert(ith, t)
            if ith != jth:
                t = insert(jth, t)
            if contains(csum, t):
                output += "R " + str(csum) + "\n"
            else:
                t = insert(csum, t)
                output += "I " + str(csum) + "\n"
        output += "-" * 10 + "\n"
    print(output[:-1])

