## Author: Arda Aktürk

import matplotlib.pyplot as plt
import numpy as np

def draw_segments(segments, title="Shape", lw=5):
    """
    segments: Each sagment should be defined as [x_start, x_end, function]
    Example: [1, 2, lambda x: 1 + 2*(x - 1)]
    """
    plt.figure(figsize=(6, 6))

    for seg in segments:
        x_start, x_end, func = seg
        x_vals = np.linspace(x_start, x_end, 100)
        y_vals = func(x_vals)
        plt.plot(x_vals, y_vals, linewidth=lw)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.title(title)
    plt.show()


############## LETTER A ###################
segments_a = [
    [1, 2, lambda x: 1 + 2 * (x-1)],
    [1.5, 2.5, lambda x: 2 + x*0],
    [2, 3, lambda x: 1 - 2 * (x-3)]
]
draw_segments(segments_a, title="Letter A")


############## LETTER R ###################
segments_r = [
    [2, 3, lambda x: 4.0 + 0.167*(x-2) + 0*(x-2)**2 + -0.417*(x-2)**3],
    [3, 3.5, lambda x: 3.75 + -1.083*(x-3) + -1.25*(x-3)**2 + 0.833*(x-3)**3],
    [2, 3, lambda x: 2.0 + -0.167*(x-2) + 0*(x-2)**2 + 0.417*(x-2)**3],
    [3, 3.5, lambda x: 2.25 + 1.083*(x-3) + 1.25*(x-3)**2 + -0.833*(x-3)**3],
    [2, 3.5, lambda x: 2 - 2/1.5 * (x-2)],
    [2, 2.01, lambda x: 4 / 0.01 * (x-2)]
]
draw_segments(segments_r, title="Letter R")


############## LETTER D ###################
segments_d = [
    [1, 2.414, lambda x: 5.0 + 0.292*(x-1) + 0*(x-1)**2 + -0.353*(x-1)**3],
    [2.414, 3, lambda x: 4.414 + -1.827*(x-2.414) + -1.499*(x-2.414)**2 + 0.853*(x-2.414)**3],
    [1, 2.414, lambda x: 1.0 + -0.292*(x-1) + 0*(x-1)**2 + 0.353*(x-1)**3],
    [2.414, 3, lambda x: 1.586 + 1.827*(x-2.414) + 1.499*(x-2.414)**2 + -0.853*(x-2.414)**3],
    [1, 1.01, lambda x: 1 + 4 / 0.01 * (x-1)]
]
draw_segments(segments_d, title="Letter D")


############## LETTER K ###################
segments_k = [
    [1, 1.01, lambda x: 1 + 2 / 0.01 * (x - 1)],
    [1, 2, lambda x: 2 + (x - 1)],
    [1, 2, lambda x: 2 - (x - 1)]
]
draw_segments(segments_k, title="Letter K")


############## LETTER U ###################
segments_u = [
    [1, 1.7, lambda x: 4.0 + -5.521*(x-1) + 0*(x-1)**2 + 2.813*(x-1)**3],
    [1.7, 2, lambda x: 1.1 + -1.386*(x-1.7) + 5.907*(x-1.7)**2 + -7.994*(x-1.7)**3],
    [2, 2.3, lambda x: 1.0 + 0*(x-2) + -1.287*(x-2)**2 + 7.994*(x-2)**3],
    [2.3, 3, lambda x: 1.1 + 1.386*(x-2.3) + 5.907*(x-2.3)**2 + -2.813*(x-2.3)**3]
]
draw_segments(segments_u, title="Letter U")


############## SMILE WITH BLUSH ###############
upper_face = [
    [1, 3 - np.sqrt(3), lambda x: 3.0 + 4.113*(x-1) + 0*(x-1)**2 + -5.302*(x-1)**3],
    [3 - np.sqrt(3), 2, lambda x: 4.0 + 2.971*(x-1.267) + -4.262*(x-1.267)**2 + 2.144*(x-1.267)**3],
    [2, 3, lambda x: 4.732 + 0.178*(x-2) + 0.447*(x-2)**2 + -0.358*(x-2)**3],
    [3, 4, lambda x: 5.0 + 0*(x-3) + -0.626*(x-3)**2 + 0.358*(x-3)**3],
    [4, 3+np.sqrt(3), lambda x: 4.732 + -0.178*(x-4) + 0.447*(x-4)**2 + -2.144*(x-4)**3],
    [3+np.sqrt(3), 5, lambda x: 4.0 + -2.971*(x-4.732) + -4.262*(x-4.732)**2 + 5.302*(x-4.732)**3]
]

lower_face = [
    [1, 3 - np.sqrt(3), lambda x: 3.0 + -4.113*(x-1) + 0*(x-1)**2 + 5.302*(x-1)**3],
    [3 - np.sqrt(3), 2, lambda x: 2.0 + -2.971*(x-1.267) + 4.262*(x-1.267)**2 + -2.144*(x-1.267)**3],
    [2, 3, lambda x: 1.268 + -0.178*(x-2) + -0.447*(x-2)**2 + 0.358*(x-2)**3],
    [3, 4, lambda x: 1.0 + 0*(x-3) + 0.626*(x-3)**2 + -0.358*(x-3)**3],
    [4, 3+np.sqrt(3), lambda x: 1.268 + 0.178*(x-4) + -0.447*(x-4)**2 + 2.144*(x-4)**3],
    [3+np.sqrt(3), 5, lambda x: 2.0 + 2.971*(x-4.732) + 4.262*(x-4.732)**2 + -5.302*(x-4.732)**3]
]

right_eye = [
    [3.6, 3.8, lambda x: 3.8 + 1.5*(x-3.6) + 0*(x-3.6)**2 + -12.5*(x-3.6)**3],
    [3.8, 4, lambda x: 4.0 + 0*(x-3.8) + -7.5*(x-3.8)**2 + 12.5*(x-3.8)**3],
]

left_eye = [
    [2, 2.2, lambda x: 3.8 + 1.5*(x-2) + 0*(x-2)**2 + -12.5*(x-2)**3],
    [2.2, 2.4, lambda x: 4.0 + 0*(x-2.2) + -7.5*(x-2.2)**2 + 12.5*(x-2.2)**3],
]

right_blush = [
    [4.2, 4.3, lambda x: 3.3 + 1.5*(x-4.2) + 0*(x-4.2)**2 + -50.0*(x-4.2)**3],
    [4.3, 4.4, lambda x: 3.4 + 0*(x-4.3) + -15.0*(x-4.3)**2 + 50.0*(x-4.3)**3]
]

left_blush = [
    [1.6, 1.7, lambda x: 3.3 + 1.5*(x-1.6) + 0*(x-1.6)**2 + -50.0*(x-1.6)**3],
    [1.7, 1.8, lambda x: 3.4 + 0*(x-1.7) + -15.0*(x-1.7)**2 + 50.0*(x-1.7)**3]
]

mouth = [
    [2.4, 3, lambda x: 2.6 + -2.0*(x-2.4) + 0*(x-2.4)**2 + 1.852*(x-2.4)**3],
    [3, 3.6, lambda x: 1.8 + 0*(x-3) + 3.333*(x-3)**2 + -1.852*(x-3)**3]
]

face_outline = [*upper_face, *lower_face]
eyes = [*left_eye, *right_eye]
blushes = [*left_blush, *right_blush]

segments_swb = [
    *face_outline,
    *eyes,
    *blushes,
    *mouth
]

draw_segments(segments_swb, title="Smile with Blush")


############## SMILE WITH HALO ###############
halo = [
    [2, 3, lambda x: 5.0 + 0.3*(x-2) + 0*(x-2)**2 + -0.1*(x-2)**3],
    [3, 4, lambda x: 5.2 + 0*(x-3) + -0.3*(x-3)**2 + 0.1*(x-3)**3],
    [2, 3, lambda x: 5.0 + -0.3*(x-2) + 0*(x-2)**2 + 0.1*(x-2)**3],
    [3, 4, lambda x: 4.8 + 0*(x-3) + 0.3*(x-3)**2 + -0.1*(x-3)**3],
]

segments_swh = [
    *face_outline,
    *eyes,
    *mouth,
    *halo
]

draw_segments(segments_swh, title="Smile with Halo")


############## ANGRY FACE ###############
sad_mouth = [
    [2.4, 3, lambda x: 1.7 + 2.0*(x-2.4) + 0*(x-2.4)**2 + -1.852*(x-2.4)**3],
    [3, 3.6, lambda x: 2.5 + 0*(x-3) + -3.333*(x-3)**2 + 1.852*(x-3)**3],
]

angry_eyes = [
    [3.6, 4, lambda x: 3.6 + 1.0*(x-3.6) + 0*(x-3.6)**2 + 0*(x-3.6)**3],
    [2.4, 2, lambda x: 4.0 + -1.0*(x-2) + 0*(x-2)**2 + 0*(x-2)**3]
]

segments_angryface = [
    *face_outline,
    *sad_mouth,
    *angry_eyes
]

draw_segments(segments_angryface, title="Angry Face")


############################# END ######################################














