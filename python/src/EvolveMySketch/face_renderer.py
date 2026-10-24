
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Arc


def render_face(params, save_path=None):
    fig, ax = plt.subplots(figsize=(5, 5))

    # Face outline
    face = Ellipse(
        (0.5, 0.5),
        params.face_width,
        params.face_height,
        facecolor="#F4C7A1",
        edgecolor="black",
        linewidth=2
    )
    ax.add_patch(face)

    left_eye_x = 0.5 - params.eye_spacing / 2
    right_eye_x = 0.5 + params.eye_spacing / 2

    # Eyes
    for x in (left_eye_x, right_eye_x):
        ax.add_patch(
            Ellipse(
                (x, params.eye_y),
                params.eye_size,
                params.eye_size * 1.4,
                facecolor="white",
                edgecolor="black"
            )
        )
        ax.add_patch(
            Ellipse(
                (x, params.eye_y),
                params.eye_size * 0.4,
                params.eye_size * 0.6,
                facecolor="black"
            )
        )

    # Eyebrows
    for x in (left_eye_x, right_eye_x):
        ax.plot(
            [x - params.eye_size, x + params.eye_size],
            [params.brow_y, params.brow_y],
            color="black",
            linewidth=3
        )

    # Nose
    nose = Polygon(
        [
            (0.5, params.eye_y + 0.04),
            (0.5 - params.nose_width / 2,
             params.eye_y + params.nose_length),
            (0.5 + params.nose_width / 2,
             params.eye_y + params.nose_length)
        ],
        closed=False,
        fill=False,
        edgecolor="black",
        linewidth=2
    )
    ax.add_patch(nose)

    # Mouth
    mouth = Arc(
        (0.5, params.mouth_y),
        params.mouth_width,
        0.06,
        theta1=200,
        theta2=340,
        color="black",
        linewidth=2
    )
    ax.add_patch(mouth)

    ax.set_xlim(0, 1)
    ax.set_ylim(1, 0)
    ax.set_aspect("equal")
    ax.axis("off")

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")

    return fig, ax
