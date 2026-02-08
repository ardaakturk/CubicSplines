# CENG216 - Numerical Computation | Homework 2

**Izmir Institute of Technology (IZTECH) — Spring 2025**

This project demonstrates the use of **linear and cubic spline interpolation** to draw letters and facial expressions on a coordinate system, along with **least squares approximation** and **QR factorization** solutions.

## Exercise 1: Spline Interpolation

### Objective

Using linear and natural cubic spline equations, plot five distinct letters from my name and three facial expressions using only `matplotlib`. No built-in spline functions are used — all spline coefficients are derived mathematically from scratch.

### Letters: A, R, D, K, U

Letters are selected from **Arda Akturk** (5 unique letters). Each letter is constructed by defining piecewise polynomial segments over specified intervals.

| Letter | Spline Type | Description |
|--------|-------------|-------------|
| **A** | Linear | Three straight-line segments forming the shape |
| **R** | Cubic + Linear | Upper and lower curves via cubic splines, vertical stroke via linear |
| **D** | Cubic + Linear | Symmetric upper/lower cubic curves with a vertical stroke |
| **K** | Linear | Vertical stroke and two diagonal lines |
| **U** | Cubic | Smooth U-curve through 5 interpolation points |

### Facial Expressions

Three expressions are drawn using cubic spline curves for the face outline, eyes, mouth, and additional features:

| Expression | Components |
|------------|------------|
| **Smile with Blush** | Circular face outline, curved eyes, smile, blush marks |
| **Smile with Halo** | Circular face outline, curved eyes, smile, halo above |
| **Angry Face** | Circular face outline, angled eyebrows, frown |

The circular face outline is constructed from **12 cubic spline segments** (6 upper + 6 lower) passing through points on a circle centered at (3, 3) with radius 2.

### How It Works

1. **`cubic_spline_equations.py`** — Computes natural cubic spline coefficients for a given set of data points:
   - Builds the tridiagonal system from the natural spline boundary conditions (S''(x₀) = S''(xₙ) = 0)
   - Solves for the coefficients (a, b, c, d) of each piecewise cubic polynomial:
     ```
     Sᵢ(x) = aᵢ + bᵢ(x - xᵢ) + cᵢ(x - xᵢ)² + dᵢ(x - xᵢ)³
     ```
   - Outputs formatted equations ready to use as lambda functions

2. **`main.py`** — Defines all spline segments as `[x_start, x_end, lambda]` triples and renders each shape using `matplotlib`.

## Exercise 2: Least Squares and QR Factorization

Handwritten solutions (submitted separately as PDF) covering:

- **2a.** Solving normal equations (A^T A x = A^T b) for the least squares solution and computing the 2-norm error ||r||₂
- **2b.** Classical Gram-Schmidt orthogonalization to obtain the full QR factorization
- **2c.** Using QR factorization to solve a least squares problem and computing its 2-norm error

## Usage

```bash
# Install dependencies
pip install numpy matplotlib

# Run the main script (displays all letter and face plots)
python main.py

# Compute cubic spline coefficients for custom data points
python cubic_spline_equations.py
```

## Project Structure

```
.
├── main.py                      # Spline segment definitions and plotting
├── cubic_spline_equations.py    # Natural cubic spline coefficient calculator
├── CENG216_Homework2.pdf        # Assignment description
├── CENG216_HW2_320201111.pdf    # Submitted solutions (Exercise 2)
└── README.md
```

## Technologies

- **Python 3**
- **NumPy** — Linear algebra operations for solving the tridiagonal spline system
- **Matplotlib** — Plotting the spline curves
