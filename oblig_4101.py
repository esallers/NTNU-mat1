
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

R = 1e3 
C = 1e-6
V0 = 0 
t_span = (0, 0.01)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

def rc_circuit(t, v):
    return (1 / (R * C)) * (9 - v)

solution = solve_ivp(rc_circuit, t_span, [V0], t_eval=t_eval)

plt.figure(figsize=(8, 5))
plt.plot(solution.t, solution.y[0], label="$v(t)$", color="blue")
plt.axhline(y=9, color='red', linestyle='--', label="Kildespenning (9V)")
plt.xlabel("Tid (s)")
plt.ylabel("Spenning $v(t)$ (V)")
plt.grid(True)
plt.legend()
plt.show()