# AI Assignment – Overview

## What this repository contains

- **`TASK 1 AND 2/TASK 1/pyprogram1.ipynb`** – Notebook for Task 1.  It implements the required search‑strategy algorithm and visualises the results.
- **`TASK 1 AND 2/TASK 2/task2program.ipynb`** – Notebook for Task 2.  It loads the Australian map images, performs colour‑mapping, and analyses the data.
- Supporting files such as the PDF answer sheet (`CAT/CAT_May2026_Answers.pdf`) and helper scripts (`CAT/A*SearchStrategy.py`).

## How to run the Jupyter notebooks

1. **Install the dependencies** (if you have not done so already):
   ```bash
   cd "$(pwd)"
   python -m venv .venv   # create a virtual environment
   source .venv/bin/activate
   pip install -r requirements.txt   # create a requirements.txt if needed, otherwise install pandas, matplotlib, notebook, etc.
   ```
2. **Start Jupyter** (you can use either `notebook` or `lab`):
   ```bash
   jupyter notebook   # opens the classic UI
   # or
   jupyter lab       # opens the modern UI
   ```
3. In the Jupyter UI navigate to the notebook you want to run:
   - `TASK 1 AND 2/TASK 1/pyprogram1.ipynb` for Task 1
   - `TASK 1 AND 2/TASK 2/task2program.ipynb` for Task 2
4. **Run the cells sequentially** (use `Shift+Enter` or the Run All button).  The notebooks are fully linear – later cells depend on the output of earlier ones.
5. **Verify the output** – the final cells display the results and visualisations required for the assignment.

## Quick one‑liner for the impatient

```bash
source .venv/bin/activate && jupyter lab "TASK 1 AND 2/TASK 1/pyprogram1.ipynb"
```

Feel free to open the PDF in `CAT/` for reference answers or the helper script `A*SearchStrategy.py` for the implementation details.

---

