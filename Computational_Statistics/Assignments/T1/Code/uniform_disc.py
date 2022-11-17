"""Script to draw samples of a uniform distribution on a disc."""

import numpy as np


def uniform_disc_dist(size, radius, seed=1):
    """Uniform distribution on a disc (inversion method)."""
    np.random.seed(seed)

    uniform_rv = np.random.uniform(0, 1, size)
    r_rv = np.sqrt(uniform_rv) * radius
    theta_rv = np.random.uniform(0, 2 * np.pi, size)
    disc_rv_x = r_rv * np.cos(theta_rv)
    disc_rv_y = r_rv * np.sin(theta_rv)
    points = np.array([disc_rv_x, disc_rv_y]).T

    return points


def mc_mean_distance(p: np.ndarray, q: np.ndarray) -> np.float64:
    """Monte carlo estimate of the mean distance between two points."""
    return np.mean(np.linalg.norm(p - q, axis=1))


def true_expected_distance(radius):
    """Expected distance between two points in a disc of radius R."""
    return (128 / (45 * np.pi)) * radius
