# Hybrid_Root_Finding_Algorithm

🔍 This project implements a **hybrid root-finding algorithm** combining:
- Bisection Method
- Regula-Falsi Method
- Newton-Raphson Method

The method chooses the most efficient algorithm based on function behavior and convergence, ensuring both speed and reliability.

---

## 📁 Project Contents

- `hybrid_root_finder_report.ipynb` — Full notebook containing code, explanations, and results  
*(or whatever your file is called — change this to match)*

---

## 🧰 Tools & Methods Used

- Python (NumPy, custom function implementations)
- Numerical Methods:
  - Bisection
  - Regula-Falsi
  - Newton-Raphson
- CoCalc (for development and testing)

---

## 🧪 Example Use

```python
f = lambda x: x**2 - 2
root = hybrid_root_finder(f, a=0, b=2)
print(root)  # Output: 1.4142 (approx)

