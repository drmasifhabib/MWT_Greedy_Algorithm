import time
from mwt_greedy import directional_greedy_mwt
from mwt_dp import mwt_dp
from utils import generate_random_convex_polygon

def run_experiment(n_values=[4,10,20,30,40,50]):
    for n in n_values:
        P = generate_random_convex_polygon(n)
        # Greedy
        start = time.time()
        greedy_weight, _ = directional_greedy_mwt(P)
        greedy_time = time.time() - start
        # DP (for small n)
        if n <= 50:  # DP is slow for large n
            start = time.time()
            dp_weight = mwt_dp(P)
            dp_time = time.time() - start
            print(f"n={n}: Greedy Weight={greedy_weight:.2f}, Time={greedy_time:.3f}s | DP Weight={dp_weight:.2f}, Time={dp_time:.3f}s")

if __name__ == "__main__":
    run_experiment()
