def optimize(force, allowable=200):
    best = None
    min_weight = 1e9

    for w in range(10, 100):
        for t in range(5, 50):
            s = force / (w * t)
            if s <= allowable:
                weight = w * t
                if weight < min_weight:
                    min_weight = weight
                    best = (w, t)

    return best
