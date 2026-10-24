
from dataclasses import dataclass
import numpy as np


@dataclass
class FaceParameters:
    face_width: float
    face_height: float
    eye_spacing: float
    eye_y: float
    eye_size: float
    brow_y: float
    nose_length: float
    nose_width: float
    mouth_width: float
    mouth_y: float

    @classmethod
    def from_chromosome(cls, x):
        if len(x) != 10:
            raise ValueError("Expected exactly 10 parameters")

        return cls(*map(float, x))

    def to_chromosome(self):
        return np.array([
            self.face_width,
            self.face_height,
            self.eye_spacing,
            self.eye_y,
            self.eye_size,
            self.brow_y,
            self.nose_length,
            self.nose_width,
            self.mouth_width,
            self.mouth_y,
        ])

    def validate(self):
        values = self.to_chromosome()

        if not np.all(np.isfinite(values)):
            raise ValueError("Parameters must be finite")
