## Author: Arda Aktürk


# Derivation steps are implemented to obtain the corresponding
# cubic spline function between the given points.
# Coordinates are estimated using a squared paper and the drawing of the shape.

# natural_cubic_cpline coefficients function implements the mathematical
# functions and returns the coefficients of the cubic functions.
# Then print_cubic_spline_function prints the function in the format that I
# use in the main file.

# For example, given the coordinates:
# x_vals = [2.4, 3, 3.6]
# y_vals = [1.7, 2.5, 1.7]

# natural_cubic_spline_coefficients will return the coefficients of the
# functions between those points. Such as:
# [(1.7, 2.0, 0, -1.852), (2.5, 0, -3.333, 1.852)]

# Then print_cubic_spline_function formats them like this:
# S(1) = 1.7 + 2.0*(x-2.4) + 0*(x-2.4)**2 + -1.852*(x-2.4)**3
# S(2) = 2.5 + 0*(x-3) + -3.333*(x-3)**2 + 1.852*(x-3)**3

# And these functions are used in the main file as lambda functions.

import numpy as np

def fix_and_round(val, tol=1e-12, digits=3):
    return 0 if abs(val) < tol else round(float(val), digits)

def natural_cubic_spline_coefficients(x: list[float], y: list[float]):
    n = len(x)  # number of points

    # Step 1: compute delta_lowercase and delta_uppercase
    delta_lc = np.diff(x)
    delta_uc = np.diff(y)

    # Step 2: build the system for c (second derivatives)
    A = np.zeros((n, n))
    rhs = np.zeros(n)

    A[0, 0] = 1  # natural spline condition
    A[-1, -1] = 1  # natural spline condition

    for i in range(1, n-1):
        A[i, i - 1] = delta_lc[i - 1]
        A[i, i] = 2 * (delta_lc[i - 1] + delta_lc[i])
        A[i, i + 1] = delta_lc[i]
        rhs[i] = 3 * ((delta_uc[i] / delta_lc[i]) -
                    (delta_uc[i-1] / delta_lc[i-1]))

    # Step 3: solve for c
    c = np.linalg.solve(A, rhs)

    # Step 4: compute a, b, c, d for each spline
    coeffs = []
    for i in range(n-1):
        a = y[i]
        b = (delta_uc[i] / delta_lc[i]) - (delta_lc[i] / 3) * (2*c[i] + c[i+1])
        d = (c[i+1] - c[i]) / (3 * delta_lc[i])
        tuple_out = (fix_and_round(a),fix_and_round(b), fix_and_round(c[i]),fix_and_round(d))
        coeffs.append(tuple_out)

    return coeffs

def print_cubic_spline_function(coeffs: list[tuple], x_values):
    for i in range(len(coeffs)):
        ai = coeffs[i][0]
        bi = coeffs[i][1]
        ci = coeffs[i][2]
        di = coeffs[i][3]
        xi = x_values[i]
        function = f"{ai} + {bi}*(x-{xi}) + {ci}*(x-{xi})**2 + {di}*(x-{xi})**3"
        print(f"S({i+1}) = {function}")



############## CHANGE ONLY THIS PART ###############

# ## UPPER PART OF R CURVE
# x_vals = [2, 3, 3.25]
# y_vals = [4, 3.75, 3]
#
# ## LOWER PART OF R CURVE
# x_vals = [2, 3, 3.25]
# y_vals = [2, 2.25, 3]

# Upper D
# x_vals = [1, 2.414, 3]
# y_vals = [5, 4.414, 3]

# Left U
# x_vals = [1, 1.7, 2, 2.3, 3]
# y_vals = [4, 1.1, 1, 1.1, 4]

# UPPER FACE
# x_vals = [1, 3 - np.sqrt(3), 2, 3, 4, 3+np.sqrt(3), 5]
# y_vals = [3, 4, 3+np.sqrt(3), 5, 3+np.sqrt(3), 4, 3]
# LOWER FACE
# x_vals = [1, 3 - np.sqrt(3), 2, 3, 4, 3+np.sqrt(3), 5]
# y_vals = [3, 2, 3-np.sqrt(3), 1, 3-np.sqrt(3), 2, 3]

# RIGHT EYE
# x_vals = [3.6, 3.8, 4]
# y_vals = [3.8, 4, 3.8]

# RIGHT BLUSH
# x_vals = [4.2, 4.3, 4.4]
# y_vals = [3.3, 3.4, 3.3]

# LEFT BLUSH
# x_vals = [1.6, 1.7, 1.8]
# y_vals = [3.3, 3.4, 3.3]

# MOUTH
# x_vals = [2.4, 3, 3.6]
# y_vals = [2.6, 1.8, 2.6]

# UPPER HALO
# x_vals = [2, 3, 4]
# y_vals = [5, 5.2, 5]

# LOWER HALO
# x_vals = [2, 3, 4]
# y_vals = [5, 4.8, 5]

# SAD MOUTH
x_vals = [2.4, 3, 3.6]
y_vals = [1.7, 2.5, 1.7]

# ANGRY EYES
# x_vals = [2, 2.4]
# y_vals = [4, 3.6]


###################################################
coeffs = natural_cubic_spline_coefficients(x_vals, y_vals)
print(coeffs)
print_cubic_spline_function(coeffs, x_vals)



