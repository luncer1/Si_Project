# SI_Project

![Project Logo](https://via.placeholder.com/150) <!-- Replace with actual logo if available -->

> **A Python implementation of a Simple Genetic Algorithm (SGA) for optimization problems, specifically maximizing a quadratic objective function.**

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## :ledger: Index

- [About](#beginner-about)
- [Usage](#zap-usage)
  - [Installation](#electric_plug-installation)
  - [Commands](#package-commands)
  - [Pre-Requisites](#notebook-pre-requisites)
  - [Development Environment](#nut_and_bolt-development-environment)
  - [File Structure](#file_folder-file-structure)
  - [Build](#hammer-build)
- [Community](#cherry_blossom-community)
  - [Contribution](#fire-contribution)
  - [Branches](#cactus-branches)
  - [Guideline](#exclamation-guideline)
- [FAQ](#question-faq)
- [Credit/Acknowledgment](#star2-creditacknowledgment)
- [License](#lock-license)

---

## :beginner: About

This project implements a **Simple Genetic Algorithm (SGA)** in Python to solve optimization problems. The algorithm evolves a population of individuals (represented as binary-encoded integers from 0 to 255) over generations to maximize a quadratic objective function:

$$ f(x) = 11x^2 + x + 6 $$

### Key Features
- 🔄 **Population Management**: Initialization, evaluation, selection, mutation, and crossover.
- ⚖️ **Fitness Handling**: Automatic adjustment for negative fitness values.
- 📊 **Statistical Analysis**: Multiple trials to identify the best individual.
- 📝 **Debug Logging**: Comprehensive logging for troubleshooting.
- 🎓 **Educational Focus**: Designed for learning evolutionary computation, extensible for other tasks.

---

## :zap: Usage

Run the main script to execute the genetic algorithm and generate results in `results.txt`.

### :electric_plug: Installation

1. **Prerequisites**: Ensure you have **Python 3.10 or higher** installed.
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/luncer1/Si_Project.git
   ```
3. **Navigate to Directory**:
   ```bash
   cd Si_Project
   ```
4. **Dependencies**: No additional packages needed – uses Python standard library only.

### :package: Commands

- **Run the Algorithm**:
  ```bash
  python main.py
  ```
  - Performs **40 statistical trials**.
  - Each trial: 5 generations with population size 30.
  - Outputs best individuals to `results.txt`.

---

### :notebook: Pre-Requisites
- 🐍 Python 3.10+
- 📚 Git

### :nut_and_bolt: Development Environment
1. Clone as above.
2. *(Optional)* Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Open in your IDE (e.g., VS Code with Python extension).
4. Modify code; test locally.

### :file_folder: File Structure

```
.
├── .gitignore
├── main.py          # 🚀 Entry point: Runs SGA algorithm
├── README.md        # 📖 This documentation
├── results.txt      # 📄 Output: Best individuals per trial
├── SGA.py           # 🧬 SGA class: Core algorithm logic
├── __pycache__/     # 🗂️ Python cache (ignored)
└── .idea/           # ⚙️ IDE config (ignored)
    ├── .gitignore
    ├── misc.xml
    ├── modules.xml
    ├── SI_Project.iml
    ├── vcs.xml
    └── inspectionProfiles/
        └── profiles_settings.xml
```

| # | File Name | Details |
|---|-----------|---------|
| 1 | `main.py` | Entry point; orchestrates trials and logging. |
| 2 | `SGA.py` | Core SGA class with evolutionary methods. |
| 3 | `results.txt` | Stores fitness values and best individuals. |

### :hammer: Build
No build required – pure Python. Run directly:
```bash
python main.py
```

---

## :cherry_blossom: Community

### :fire: Contribution

We ❤️ contributions! Here's how:

1. **🐛 Report a Bug**  
   Found an issue? Report [here](https://github.com/luncer1/Si_Project/issues).

2. **💡 Request a Feature**  
   Suggest ideas [here](https://github.com/luncer1/Si_Project/issues).

3. **🔀 Create a Pull Request**  
   Pick issues [here](https://github.com/luncer1/Si_Project/issues) and submit a PR.

   > New to open-source? Learn more [here](https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source) and about PRs [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github).

### :cactus: Branches

- **`main`**: Production branch with stable code.

**Feature Branch Workflow:**
1. Create branch: `git checkout -b feat-<feature-name>`
2. Develop and commit.
3. PR to `main`.

**Pull Request Steps:**
1. Submit PR to `main`.
2. Pass checks and reviews.

### :exclamation: Guideline
- 📏 Follow **PEP 8** style.
- 🏷️ Use descriptive, English names.
- 💬 Comment complex logic.
- 🧪 Test changes before submitting.

---

## :question: FAQ

- **What is the objective function?**  
  \( f(x) = 11x^2 + x + 6 \), maximized for \( x \in [0, 255] \).

- **How to tweak parameters?**  
  Edit variables in `main.py` (e.g., `population_size`, `crossover_rate`).

- **Why `results.txt`?**  
  Each line: `<fitness> <best_individual>` from a trial.

---

## :star2: Credit/Acknowledgment

- **Developer**: [luncer1](https://github.com/luncer1)
- **Inspiration**: Genetic algorithm concepts in evolutionary computation.

---

## :lock: License

Licensed under [MIT](LICENSE). <!-- Add LICENSE file if missing -->
:exclamation: Guideline
Follow PEP 8 for Python code style.
Use descriptive variable and function names (preferably in English).
Add comments for complex logic.
Test changes locally before submitting.
:question: FAQ
What is the objective function? It's ( f(x) = 11x^2 + x + 6 ), maximized for x in [0, 255].
How to change parameters? Edit variables in main.py like population_size, crossover_rate, etc.
Why are results in results.txt? Each line contains the fitness value and the best individual from a trial.
:star2: Credit/Acknowledgment
Developed by luncer1.
Inspired by genetic algorithm concepts in evolutionary computation.
:lock: License
This project is licensed under the MIT License. See LICENSE for details. <!-- Add a LICENSE file if not present -->