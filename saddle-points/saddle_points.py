def saddle_points(m):
    if not m:
        return set()
    if any(len(r) != len(m[0]) for r in m):
        raise ValueError('irregular matrix')
    mx = [max(r) for r in m]
    mn = [min(c) for c in zip(*m)]
    points = [(i, j) for i in range(len(m))
              for j in range(len(m[0])) if mx[i] == mn[j]]

    return set(points)
