from EvolveMySketch.face_model import FaceParameters
from EvolveMySketch.face_renderer import render_face
from EvolveMySketch.fitness import face_fitness

x = [
    0.80, 1.00, 0.30, 0.40, 0.06,
    0.32, 0.18, 0.07, 0.22, 0.75
]

face = FaceParameters.from_chromosome(x)
face.validate()

score = face_fitness(x)

print("Initial chromosome:", x)
print("Fitness score:", score)

render_face(face, "evaluated_face.png")
