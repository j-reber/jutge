import time
from yogi import tokens


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


def count_rotations(s, t):
    if len(s) != len(t):
        return 0

    n = len(s)
    s2 = s + s
    pattern = t + "#" + s2
    lps = kmp(pattern)
    count = 0
    for i in range(n + 1, len(lps)):
        if lps[i] == n:
            count += 1

    if s == t:
        return count - 1

    return count


def main():
    s, t = [], []
    s.append('abc'*10000)
    t.append('bca'*10000)
    #
    # s.append("zqzzqzzqz")
    # t.append("zqzzqzzqz")
    for i, x in enumerate(tokens(str)):
        if i % 2 == 0:
            s.append(x)
        else:
            t.append(x)

    for i in range(len(s)):
        # start = time.time()
        rots = count_rotations(s[i], t[i])
        # end = time.time()
        # print(end-start)
        print(rots)


if __name__ == '__main__':
    main()
