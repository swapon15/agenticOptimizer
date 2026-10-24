
import numpy as np


# Target geometric proportions.
# Vertical positions are measured relative to the top of the face.
TARGETS = {
    "eye_y_ratio": 0.38,
    "nose_length_ratio": 0.18,
    "nose_width_ratio": 0.08,
    "mouth_y_ratio": 0.72,
    "mouth_width_ratio": 0.28,
}

WEIGHTS = {
    "symmetry": 0.25,
    "eyes": 0.25,
    "nose": 0.25,
    "mouth": 0.25,
}


def face_fitness(x):
    """
    Calculate a scalar geometric fitness score.
    Lower score is better.

    Chromosome:
    [face_width, face_height, eye_spacing, eye_y,
     eye_size, brow_y, nose_length, nose_width,
     mouth_width, mouth_y]
    """

    x = np.asarray(x, dtype=float)

    if x.shape != (10,) or not np.all(np.isfinite(x)):
        return 1e6

    (
        face_width,
        face_height,
        eye_spacing,
        eye_y,
        eye_size,
        brow_y,
        nose_length,
        nose_width,
        mouth_width,
        mouth_y,
    ) = x

    if face_width <= 0 or face_height <= 0:
        return 1e6

    # The face ellipse is centered at y = 0.5.
    face_top = 0.5 - face_height / 2

    # Normalize vertical positions relative to the face top.
    eye_y_ratio = (eye_y - face_top) / face_height
    mouth_y_ratio = (mouth_y - face_top) / face_height

    # Normalize dimensions by the corresponding face dimension.
    nose_length_ratio = nose_length / face_height
    nose_width_ratio = nose_width / face_width
    mouth_width_ratio = mouth_width / face_width

    # The current renderer creates symmetric facial features.
    symmetry_score = 0.0

    # Eye placement.
    eye_score = abs(
        eye_y_ratio - TARGETS["eye_y_ratio"]
    )

    # Nose proportions.
    nose_score = (
        abs(nose_length_ratio - TARGETS["nose_length_ratio"])
        + abs(nose_width_ratio - TARGETS["nose_width_ratio"])
    )

    # Mouth proportions.
    mouth_score = (
        abs(mouth_y_ratio - TARGETS["mouth_y_ratio"])
        + abs(mouth_width_ratio - TARGETS["mouth_width_ratio"])
    )

    # Geometric validity penalties.
    validity_penalty = 0.0

    if eye_spacing / 2 + eye_size / 2 >= face_width / 2:
        validity_penalty += 10.0

    if mouth_width >= face_width:
        validity_penalty += 10.0

    if mouth_y <= eye_y:
        validity_penalty += 10.0

    if nose_length <= 0 or nose_width <= 0:
        validity_penalty += 10.0

    score = (
        WEIGHTS["symmetry"] * symmetry_score
        + WEIGHTS["eyes"] * eye_score
        + WEIGHTS["nose"] * nose_score
        + WEIGHTS["mouth"] * mouth_score
        + validity_penalty
    )

    return float(score)
