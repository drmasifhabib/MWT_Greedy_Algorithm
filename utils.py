import math
import random
import numpy as np

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def rotate_list(lst, idx):
    return lst[idx:] + lst[:idx]

def generate_random_convex_polygon(n, radius=10):
    angles = sorted([random.uniform(0, 2*math.pi) for _ in range(n)])
    return [(radius * math.cos(a), radius * math.sin(a)) for a in angles]
