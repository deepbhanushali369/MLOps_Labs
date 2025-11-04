# MLOps_Labs – Lab04_Github_Lab

## Overview
Lab 04 focuses on implementing a simple Python project integrated with automated testing using **GitHub Actions (CI/CD)**.  
The objective was to understand how continuous integration pipelines help ensure code reliability, testing consistency, and workflow automation.

---

## Objectives
- Create and activate a virtual environment.
- Develop Python functions inside a modular folder structure.
- Write test cases using **Pytest** and **Unittest** frameworks.
- Configure **GitHub Actions** using YAML files to automate testing.
- Verify that all tests pass locally and on GitHub.

---

## Project Structure
MLOps_Labs/
│
├── .github/
│ └── workflows/
│ ├── github_lab1_pytest_action.yml
│ └── github_lab2_unittest_action.yml
│
├── Lab04_Github_Lab/
│ └── Lab1/
│ ├── src/lab1/calculator.py
│ ├── test/test_pytest.py
│ └── test/test_unittest.py
│
├── requirements.txt
└── .gitignore

## Step-by-Step Implementation

### Step 1: Virtual Environment

To isolate dependencies, a virtual environment named **`github_env`** was created and activated:
```bash
python -m venv github_env
github_env\Scripts\activate
pip install pytest

```

### Step 2: Folder Structure

A clean, modular folder layout was created:
src/ – source code for the project.
test/ – test files for validation.
.github/workflows/ – CI/CD pipeline definitions.

### Step 3: Python Module

calculator.py contains four basic arithmetic functions:

def fun1(x, y): return x + y
def fun2(x, y): return x - y
def fun3(x, y): return x * y
def fun4(x, y): return fun1(x, y) + fun2(x, y) + fun3(x, y)

### Step 4: Testing Locally

Two test scripts were created:
test_pytest.py – uses pytest.
test_unittest.py – uses unittest.
Run tests locally from the repo root:

python -m pytest Lab04_Github_Lab\Lab1\test\test_pytest.py -q
python -m unittest Lab04_Github_Lab.Lab1.test.test_unittest -q

### Step 5: GitHub Actions Workflows

Two YAML files were created under .github/workflows/:
github_lab1_pytest_action.yml – runs pytest automatically.
github_lab2_unittest_action.yml – runs unittest automatically.

Each workflow:
Triggers on every push or pull request to main.
Sets up Python 3.11 on an Ubuntu runner.
Installs dependencies from requirements.txt.
Executes the respective test suite.
Uploads results as artifacts.