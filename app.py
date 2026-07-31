import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.title("Quadratic Equation Solver")

a = st.number_input("Enter a", value=1.0)
b = st.number_input("Enter b", value=0.0)
c = st.number_input("Enter c", value=0.0)

if st.button("Solve"):
    delta = b**2 - 4*a*c

    if a == 0:
        st.error("a must not be 0")

    else:
        if delta > 0:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            st.success(f"x₁ = {x1:.4f}, x₂ = {x2:.4f}")

            left = min(x1, x2) - 5
            right = max(x1, x2) + 5

        elif delta == 0:
            x1 = -b/(2*a)
            st.success(f"x₁ = x₂ = {x1:.4f}")

            left = x1 - 5
            right = x1 + 5

        else:
            st.warning("No real roots.")

            vertex = -b/(2*a)
            left = vertex - 10
            right = vertex + 10

        x = np.linspace(left, right, 500)
        y = a*x**2 + b*x + c

        fig, ax = plt.subplots(figsize=(8,5))
        ax.plot(x, y)
        ax.axhline(0, color="black")
        ax.axvline(0, color="black")
        ax.grid(True)
        ax.set_title(f"y = {a}x² + {b}x + {c}")

        st.pyplot(fig)
