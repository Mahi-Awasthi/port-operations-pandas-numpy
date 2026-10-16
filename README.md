# Port Operations: Pandas and NumPy

A small training exercise demonstrating how to detect and handle missing values
in port-operation data with Pandas and NumPy.

## What this exercise covers

- Selecting relevant DataFrame columns without changing the original data
- Creating example missing values with `numpy.nan`
- Counting missing values with `DataFrame.isna().sum()`
- Filling numeric missing values with each column's median

## Project files

- `missing_values_demo.py` — runnable demonstration script
- `sample_ports.csv` — small synthetic dataset for practice
- `requirements.txt` — Python package requirements

The sample CSV is synthetic and is included for demonstration only; it does not
represent real port operations.

## Run the exercise

Use Python 3.9 or newer. From this folder, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the demonstration with the included sample data:

```bash
python missing_values_demo.py
```

To use your own CSV, pass its path:

```bash
python missing_values_demo.py path/to/your_ports.csv
```

Your CSV must include these columns:

- `Port_Name`
- `Avg_Vessel_Wait_Time_Hours`
- `Labor_Availability_Percent`

The script introduces missing values in a copy of the selected columns, prints
the missing-value counts before and after median imputation, and leaves the
input file unchanged.

## Publish to GitHub

This project is prepared for the public repository
[Mahi-Awasthi/port-operations-pandas-numpy](https://github.com/Mahi-Awasthi/port-operations-pandas-numpy).
After authenticating Git with GitHub, publish the committed project from this
folder with:

```bash
git push -u origin main
```

If Git prompts for authentication, sign in through Git Credential Manager or
GitHub Desktop. Never put a password or access token in the remote URL or in a
project file.
