from typing import List
from collections import defaultdict


def update(node_index, l, r, e, d, new_height, new_slope,
           height, slope, lazy, points_map):
    if l == e and r == d:
        height[node_index] += new_height
        slope[node_index] += new_slope
        lazy[node_index] = True
        return

    mid = (l + r) // 2
    node_index_l = 2 * node_index
    node_index_r = node_index_l + 1

    if lazy[node_index]:
        height[node_index_l] += height[node_index]
        height[node_index_r] += height[node_index] + slope[node_index] * (points_map[mid + 1] - points_map[l])
        slope[node_index_l] += slope[node_index]
        slope[node_index_r] += slope[node_index]
        lazy[node_index_l] = lazy[node_index_r] = True
        height[node_index] = slope[node_index] = 0
        lazy[node_index] = False

    if e <= mid:
        update(node_index_l, l, mid, e, min(mid, d), new_height, new_slope,
               height, slope, lazy, points_map)
    new_e = max(mid + 1, e)
    k = new_height + (new_slope * (points_map[new_e] - points_map[e]))
    if d > mid:
        update(node_index_r, mid + 1, r, new_e, d, k, new_slope,
               height, slope, lazy, points_map)


def query(node_index, l, r, x, height, slope, lazy,
          points_map):
    res = 0.0
    if lazy[node_index]:
        res = height[node_index] + slope[node_index] * (points_map[x] - points_map[l])

    if l == r:
        return res

    m = (l + r) // 2
    pl = 2 * node_index
    pr = pl + 1
    if x <= m:
        res += query(pl, l, m, x, height, slope, lazy, points_map)
    else:
        res += query(pr, m + 1, r, x, height, slope, lazy, points_map)
    return res


def main():

    while True:
        try:
            n = int(input())
            if n == 0:
                break

            height = [0.0] * (15 * n)
            slope = [0.0] * (15 * n)
            lazy = [False] * (15 * n)
            sl, sr, syl, syr = [0.0] * n, [0.0] * n, [0.0] * n, [0.0] * n
            to_query = [0.0] * (4 * n)
            for i in range(n):
                c, *values = input().split()
                if c == 'A':
                    l, r, yl, yr = map(float, values)
                    sl[i] = l
                    sr[i] = r
                    syl[i] = yl
                    syr[i] = yr
                else:
                    x = float(values[0])
                    to_query[i] = x
            _ = input()

            points_map = sl + sr + to_query
            points_map = sorted(set(points_map))
            points_map_reversed = defaultdict(int)
            for i, point in enumerate(points_map):
                points_map_reversed[point] = i

            for i in range(n):
                if to_query[i]:
                    print("{:.3f}".format(query(1, 0, len(points_map) - 1, points_map_reversed[to_query[i]], height, slope, lazy, points_map)))
                else:
                    update(1, 0, len(points_map) - 1, points_map_reversed[sl[i]], points_map_reversed[sr[i]], syl[i], (syr[i] - syl[i]) / (sr[i] - sl[i]),
                           height, slope, lazy, points_map)
        except ValueError:
            break


if __name__ == "__main__":
    main()