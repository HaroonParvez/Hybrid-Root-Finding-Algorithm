# Hybrid Root-Finding Algorithm

🔍 This project implements a **hybrid root-finding algorithm** combining:
- Newton-Raphson Method  
- Regula-Falsi Method  
- Bisection Method  

The algorithm adapts between methods based on the quality of input and convergence behaviour. It's designed to find a root of a real-valued function reliably and efficiently.

---

## ⚙️ Function Definition

```python
Hybrid_Function(f, bounds=None, fp=None, x0=None, iterations=100, tol=1.0e-8)
```

### Parameters:
- `f`: The function whose root is being found  
- `bounds`: Tuple `(lower, upper)` — used for Regula-Falsi or Bisection  
- `fp`: Derivative of the function `f`, used for Newton-Raphson  
- `x0`: Initial guess for Newton-Raphson  
- `iterations`: Maximum number of iterations (default = 100)  
- `tol`: Tolerance for convergence (default = 1.0e-8)  

### Returns:
- Approximate root (or `None` if not found)  
- Number of iterations performed  

---

## 📁 Project Contents

- `Hybrid_Root_Finding_Algorithm.ipynb` — Full notebook containing:
  - Function implementation  
  - Mathematical explanation  
  - Test cases and results  

---

## 🧰 Tools & Methods Used

- Python  
- Jupyter Notebook (via CoCalc)  
- Numerical differentiation (fallback if `fp` not provided)  

---

## 🧪 Example Use

```python
f = lambda x: x**2 - 2
fp = lambda x: 2*x
root, iters = Hybrid_Function(f, bounds=(0, 2), fp=fp, x0=1.5)
print(f"Root: {root}, Iterations: {iters}")
```

### Output:
```
Root: 1.4142135623746899, Iterations: 4
```

---

## 🎯 Features

- Starts with **Newton-Raphson** if `x0` and `fp` are provided  
- Falls back to **Regula-Falsi** with `bounds` if Newton fails or isn’t applicable  
- Switches to **Bisection** as a final fallback  
- Uses **numerical derivative** if `fp` not provided  
- Automatically switches between methods based on convergence performance  

---

## 📌 Author

**Haroon Parvez**  
BSc Physics and Data Science – Queen Mary University of London
