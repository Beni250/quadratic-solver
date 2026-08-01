import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Page Header
# -----------------------------
st.set_page_config(page_title="Quadratic Equation Solver", page_icon="🧮")

st.title("🧮 Quadratic Equation Solver")
st.subheader("Created by Bernard")

st.caption("Solve and visualize quadratic equations.")

st.latex(r"ax^2 + bx + c = 0")

st.write(
    "Enter the coefficients **a**, **b**, and **c** below, then click **Solve** to calculate the roots and display the graph."
)

# -----------------------------
# Inputs
# -----------------------------
a = st.number_input("Enter coefficient a", value=1.00)
b = st.number_input("Enter coefficient b", value=0.00)
c = st.number_input("Enter coefficient c", value=0.00)

# -----------------------------
# Solve Button
# -----------------------------
if st.button("Solve",type="primary"):

    if a == 0:
        st.error("Coefficient 'a' must not be different from 0; otherwise, the equation would not be quadratic.")

    else:

        delta = b**2 - 4*a*c

        st.markdown("### Equation")
        st.latex(fr"{a}x^2 + ({b})x + ({c}) = 0")

        st.markdown("### Discriminant")
        st.write(f"Δ = {delta:.4f}")

        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)

            st.success(f"Two real roots found:\n\nx₁ = {x1:.4f}\n\nx₂ = {x2:.4f}")

            left = min(x1, x2) - 5
            right = max(x1, x2) + 5

        elif delta == 0:
            x1 = -b / (2 * a)

            st.success(f"One repeated root:\n\nx = {x1:.4f}")

            left = x1 - 5
            right = x1 + 5

        else:
            st.warning("The equation has no real roots.")

            vertex = -b / (2 * a)
            left = vertex - 10
            right = vertex + 10

        # -----------------------------
        # Plot
        # -----------------------------
        x = np.linspace(left, right, 500)
        y = a * x**2 + b * x + c

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.plot(x, y, color="blue", linewidth=2)

        ax.axhline(0, color="black")
        ax.axvline(0, color="black")

        # Mark roots
        if delta > 0:
            ax.scatter([x1, x2], [0, 0], color="red", s=80, label="Roots")

        elif delta == 0:
            ax.scatter([x1], [0], color="red", s=80, label="Root")

        # Vertex
        vertex_x = -b / (2 * a)
        vertex_y = a * vertex_x**2 + b * vertex_x + c

        ax.scatter(vertex_x, vertex_y,
                   color="green",
                   s=80,
                   label="Vertex")

        ax.set_title(f"y = {a}x² + {b}x + {c}")
        ax.set_xlabel("X-Axis")
        ax.set_ylabel("Y-Axis")

        ax.grid(True)
        ax.legend()

        st.pyplot(fig)

        # -----------------------------
        # Extra Information
        # -----------------------------
        st.markdown("### Vertex")

        st.write(f"({vertex_x:.4f}, {vertex_y:.4f})")

        st.markdown("### Axis of Symmetry")

        st.latex(fr"x={vertex_x:.4f}")

st.divider()

st.caption("© 2026 Bernard | Linear Equation Solver")
