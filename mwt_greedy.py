import math
from utils import euclidean_distance, rotate_list, generate_random_convex_polygon

def greedy_mwt(P, direction='clockwise'):
    if direction == 'anticlockwise':
        P = P[::-1]  # Reverse for anticlockwise
    n = len(P)
    if n <= 3:
        return 0, []  # Base case

    # Find shortest external edge
    min_edge = float('inf')
    start_idx = 0
    for i in range(n):
        dist = euclidean_distance(P[i], P[(i + 1) % n])
        if dist < min_edge:
            min_edge = dist
            start_idx = i

    # Rotate to start from shortest edge
    P = rotate_list(P, start_idx)

    diagonals = []
    total_weight = 0
    while n > 3:
        for i in range(n):
            v1, v2, v3, v4 = P[i], P[(i+1)%n], P[(i+2)%n], P[(i+3)%n]
            d1 = euclidean_distance(v1, v3)
            d2 = euclidean_distance(v2, v4)

            if d1 < d2:
                diagonals.append((v1, v3))
                total_weight += d1
                P = P[:i+1] + P[i+2:]
            else:
                diagonals.append((v2, v4))
                total_weight += d2
                P = P[:i+2] + P[i+3:]
            n -= 1
            break  # Restart after removal
    return total_weight, diagonals

def directional_greedy_mwt(P):
    cw_weight, cw_diagonals = greedy_mwt(P, 'clockwise')
    acw_weight, acw_diagonals = greedy_mwt(P, 'anticlockwise')
    if cw_weight < acw_weight:
        return cw_weight, cw_diagonals
    else:
        return acw_weight, acw_diagonals
