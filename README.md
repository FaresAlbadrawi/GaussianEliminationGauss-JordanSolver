# Gaussian Elimination Solver

This project is an advanced Python-based solver for systems of linear equations using **Gaussian Elimination**. It is designed with **modular programming** principles, ensuring code reusability, clarity, and efficiency. The implementation leverages **matrix manipulation, numerical methods, and structured programming** to efficiently determine solutions.

## 🚀 Key Features

- **Dynamic Matrix Handling**: Takes user input for matrix dimensions and values.
- **Algorithmic Optimization**: Implements Gaussian elimination with row operations.
- **Edge Case Detection**: Identifies no-solution and infinite-solution cases.
- **Modular Design**: Divides logic into independent, reusable Python functions.
- **Error Handling**: Detects invalid inputs and provides modification options.
- **Efficient Data Processing**: Uses optimized loops and in-place transformations for performance.

## 🛠️ Technical Skills Demonstrated

- **Python Programming**: Extensive use of Python’s data structures (lists, loops, conditionals).
- **Algorithm Development**: Implements a mathematical approach to solving linear systems.
- **Modular Coding**: Organized as reusable functions across multiple scripts.
- **Numerical Computation**: Matrix transformations using basic numerical methods.
- **File Handling & Input Validation**: Ensures user input is properly validated before execution.
- **Debugging & Error Handling**: Checks for inconsistencies in user-provided equations.

## 🔍 How It Works

1. **User Input**: The program prompts for the number of equations and variables.
2. **Matrix Construction**: Takes in user-provided coefficients and constants.
3. **Gaussian Elimination Steps**:
   - Identifies zero rows and missing data.
   - Finds pivot elements and rearranges rows if necessary.
   - Performs row reduction to get a row-echelon form.
   - Back-substitutes values for solution extraction.
4. **Solution Classification**:
   - **Unique Solution**: Outputs the solved values.
   - **No Solution**: Detects inconsistencies and terminates.
   - **Infinite Solutions**: Identifies dependent equations.
5. **Output Results**: Displays the solution set clearly.

## 🚀 Running the Program

Execute the script using:

```bash
python _main_file.py
