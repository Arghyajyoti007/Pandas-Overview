# Pandas Operations Notebook

This repository contains a Jupyter Notebook (`.ipynb`) demonstrating various fundamental operations and concepts in the Pandas library for data manipulation and analysis in Python.

## Table of Contents

1.  [Getting Started](#getting-started)
2.  [Notebook Sections](#notebook-sections)
    *   [DataFrame and Series Creation](#dataframe-and-series-creation)
    *   [Exploring DataFrames](#exploring-dataframes)
    *   [Indexing and Selection (`.loc` and `.iloc`)](#indexing-and-selection-loc-and-iloc)
    *   [Conditional Selection](#conditional-selection)
    *   [Data Manipulation](#data-manipulation)
    *   [Null Value Management](#null-value-management)

## Getting Started

To run this notebook, you will need to have Python and Jupyter installed. We recommend using Anaconda or Miniconda for environment management.

### Prerequisites

*   Python 3.x
*   Jupyter Notebook
*   Pandas library
*   NumPy library

### Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```
2.  **Install the necessary libraries:**
    ```bash
    pip install pandas numpy jupyter
    ```
3.  **Open the Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
    Then navigate to and open the notebook file (e.g., `pandas_operations.ipynb`).

## Notebook Sections

### DataFrame and Series Creation
This section covers the basics of creating Pandas DataFrames and Series from dictionaries and lists, including specifying custom indices.

### Exploring DataFrames
Learn how to get a quick overview of your DataFrame using functions like:
*   `.head()`: View the first few rows.
*   `.tail()`: View the last few rows.
*   `.info()`: Get a summary of the DataFrame, including data types and non-null values.
*   `.describe()`: Generate descriptive statistics.
*   `.dtypes`: Check data types of columns.
*   `.shape`: Get the dimensions of the DataFrame.
*   `.columns`: List column names.
*   `.unique()`: Find unique values in a Series.
*   `.nunique()`: Count unique values in a Series.
*   `.value_counts()`: Count occurrences of unique values.

### Indexing and Selection (`.loc` and `.iloc`)
Understand how to select data based on labels (`.loc`) and integer positions (`.iloc`).
*   **`.loc`**: Label-based indexing for rows and columns.
*   **`.iloc`**: Integer-location based indexing for rows and columns.

### Conditional Selection
Demonstrates various methods for filtering DataFrames based on conditions:
*   Boolean indexing using comparison operators (`>`, `<`, `==`, etc.).
*   Combining conditions with `&` (AND) and `|` (OR).
*   Using `.query()` for string-based conditional selection.
*   Using `~` (NOT) for inverting conditions.
*   Filtering with `.isin()` to check for membership in a list of values.

### Data Manipulation
This section showcases common data manipulation techniques:
*   **Adding new columns**.
*   **Renaming columns**.
*   **Changing data types** (`.astype()`).
*   **Replacing values** (`.replace()`).
*   **Removing columns** (`.drop()`).

### Null Value Management
Learn how to identify, remove, and fill missing values (NaNs):
*   `.isnull()` and `.notnull()`: Identify missing values.
*   `.isnull().sum()`: Count missing values per column.
*   `.dropna()`: Remove rows or columns with missing values.
*   `.fillna()`: Fill missing values with a specified value, or using methods like forward-fill (`ffill`) or back-fill (`bfill`).
*   Filling with aggregate statistics (mean, median, mode).

Feel free to explore the notebook, run the cells, and experiment with your own data!
