# 🧮 Interactive CLI Mini Calculator

A lightweight, robust Command Line Interface (CLI) Calculator built with Python. Designed with a modular dictionary-dispatch architecture, robust input validation, and in-memory calculation history tracking.

---

## 🚀 Features

* **Basic Arithmetic Operations:** Addition, Subtraction, Multiplication, and Division.
* **Dual Input Support:** Accepts both standard operators (`+`, `-`, `*`, `/`) and numeric choices (`1`, `2`, `3`, `4`).
* **Calculation History:** Keeps track of previous calculations and allows viewing the last 5 operations with the `history` command.
* **Error Handling & Validation:**
  * Prevents division by zero using `ZeroDivisionError` handling.
  * Catches non-numeric inputs using `ValueError` handling to prevent crashes.
* **Modular Function Mapping:** Implemented using first-class functions mapped to dictionary keys instead of lengthy `if/elif` chains.

---

## 🛠️ Tech Stack

* **Language:** Python 3.14+
* **Environment:** Command Line / Terminal

---

## 📂 Project Structure

```text
Mini Calculator/
│
├── main.py          # Core calculator logic, execution loop & history handling
└── README.md        # Project documentation
