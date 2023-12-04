from argparse import ArgumentParser

import numpy as np


def estimate_pi_mc(n_points: int, seed: int | None = None) -> float:
    """Estimates PI using Monte-Carlo method.

    Calculates fraction of points inside circle. The points are sampled
    uniformly in square.

    :param n_points: number of points to use for estimation
    :param seed: random seed for reproducibility

    :returns: PI estimate
    """

    random = np.random.default_rng(seed)
    x, y = random.uniform(low=-1, high=1, size=(2, n_points))
    inside = x**2 + y**2 < 1
    pi = 4 * inside.mean()
    return pi


def calc_circle_area(radius: float, pi: float = np.pi) -> float:
    """Calculates circle area using its radius.

    :param radius: circle radius
    :param pi: value to use for PI
    :returns: circle area with iven radius.
    """

    return pi * radius**2


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--n-points",
        type=int,
        default=10_000_000,
        help="Number of points to use for PI estimation",
    )
    parser.add_argument("--seed",
        type=int,
        default=None,
        help="Random seed for PI estimation",
    )
    parser.add_argument(
        "--radius",
        type=float,
        required=True,
        help="circle raduis",
    )
    args = parser.parse_args()

    pi_estim = estimate_pi_mc(args.n_points, args.seed)
    area = calc_circle_area(args.radius, pi_estim)
    print(area)
