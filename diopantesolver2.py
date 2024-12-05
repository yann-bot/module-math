import tkinter as tk
from tkinter import messagebox
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from math import gcd

def extended_euclidean(a, b):
    """Retourne (gcd, x, y) tels que ax + by = gcd(a, b)"""
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

def solve_diophantine(a, b, c):
    """Résout l'équation ax + by = c et retourne les solutions entières"""
    g, x0, y0 = extended_euclidean(a, b)
    if c % g != 0:
        return None, None, None  # Pas de solution
    
    # Solution particulière
    x0 *= c // g
    y0 *= c // g
    
    # Forme générale des solutions
    k_x = b // g  # Coefficient pour k dans x
    k_y = -a // g  # Coefficient pour k dans y
    
    return (x0, y0), (k_x, k_y), g

def plot_diophantine(a, b, c, x0, y0, k_x, k_y):
    """Trace les solutions entières uniquement"""
    # Calcul des solutions discrètes
    k_values = range(-10, 11)  # Limiter k pour un affichage clair
    solutions = [(x0 + k * k_x, y0 + k * k_y) for k in k_values]

    # Tracer les solutions entières
    plt.figure(figsize=(8, 8))
    for x, y in solutions:
        plt.scatter(x, y, color='red', label='Solutions entières' if solutions.index((x, y)) == 0 else "")

    # Marquer la solution particulière
    plt.scatter(x0, y0, color='blue', label='Solution particulière')

    # Étiquettes
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.title(f"Solutions entières de l'équation {a}x + {b}y = {c}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xticks(range(min(x for x, y in solutions) - 1, max(x for x, y in solutions) + 2))
    plt.yticks(range(min(y for x, y in solutions) - 1, max(y for x, y in solutions) + 2))
    plt.show()

def solve_and_plot():
    """Gestionnaire d'événements pour résoudre et tracer les solutions entières"""
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres entiers pour a, b et c.")
        return

    solution_particuliere, solution_generale, g = solve_diophantine(a, b, c)
    if solution_particuliere is None:
        messagebox.showerror("Erreur", f"L'équation {a}x + {b}y = {c} n'a pas de solution entière.")
        return

    x0, y0 = solution_particuliere
    k_x, k_y = solution_generale

    # Afficher la solution
    messagebox.showinfo("Solution", 
                        f"Solution particulière : x = {x0}, y = {y0}\n"
                        f"Solutions générales : x = {x0} + k*{k_x}, y = {y0} + k*{k_y}, k ∈ Z")

    # Tracer les solutions entières
    plot_diophantine(a, b, c, x0, y0, k_x, k_y)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Équation diophantienne ax + by = c")

# Interface utilisateur
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Entrez les coefficients de l'équation ax + by = c :").grid(row=0, columnspan=2, pady=5)

tk.Label(frame, text="a :").grid(row=1, column=0)
entry_a = tk.Entry(frame)
entry_a.grid(row=1, column=1)

tk.Label(frame, text="b :").grid(row=2, column=0)
entry_b = tk.Entry(frame)
entry_b.grid(row=2, column=1)

tk.Label(frame, text="c :").grid(row=3, column=0)
entry_c = tk.Entry(frame)
entry_c.grid(row=3, column=1)

solve_button = tk.Button(frame, text="Résoudre et tracer", command=solve_and_plot)
solve_button.grid(row=4, columnspan=2, pady=10)

# Lancement de l'application
root.mainloop()
