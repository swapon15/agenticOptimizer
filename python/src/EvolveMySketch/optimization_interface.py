
import numpy as np

from EvolveMySketch.face_model import FaceParameters
from EvolveMySketch.fitness import face_fitness


def evaluate_candidate(x):
    """
    MATLAB GA objective-function entry point.

    Accepts a 10-dimensional chromosome from MATLAB
    and returns a scalar fitness score.
    """

    x = np.asarray(x, dtype=float).reshape(-1)

    if x.size != 10:
        raise ValueError(
            f"Expected 10 parameters, received {x.size}"
        )

    if not np.all(np.isfinite(x)):
        return 1e6

    candidate = FaceParameters.from_chromosome(x)
    candidate.validate()

    return face_fitness(candidate.to_chromosome())
