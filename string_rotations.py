import time


def kmp(strg):
    p = [0 for _ in strg]
    j = -1
    for i in range(len(strg)):
        while j >= 0 and strg[j] != strg[i]:
            if j:
                j = p[j - 1]
            else:
                j = -1
        j += 1
        p[i] = j
    return p


def count_rotations_simple(s, t):
    if len(s) != len(t):
        return 0

    count = 0
    n = len(s)

    for i in range(n):
        rotated = s[i:] + s[:i]
        if rotated == t:
            count += 1
    return count


def count_rotations(s, t):
    if len(s) != len(t):
        return []
    if s == t:
        return len(s)

    n = len(s)
    s2 = s + s
    pattern = t + "#" + s2
    lps = kmp(pattern)

    rotations = []
    for i in range(n + 1, len(lps)):
        if lps[i] == n:
            rotation_start = i - 2 * n
            rotation = s2[rotation_start:rotation_start + n]
            rotations.append(rotation)

    return len(rotations)


def main():
    s, t = [], []
    # s.append('z' * 50000 + 'a' * 300 + 'iib' * 300)
    # t.append('iib' * 300 + 'z' * 50000 + 'a'*300)
    while True:
        line = input()
        if line == "":
            break
        s1, t1 = line.split(" ")
        s.append(s1)
        t.append(t1)
    for i in range(len(s)):
        # start = time.time()
        rots = count_rotations(s[i], t[i])
        print(rots)
        # end_kmp = time.time()
        # print(end_kmp-start)
        # rots_simp = count_rotations_simple(s[i], t[i])
        # print(rots_simp)
        # end = time.time()
        # print(end-end_kmp)


if __name__ == '__main__':
    main()
