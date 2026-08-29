# Python Fundamentals, Data Analysis and Git
This project contains the solutions for Task 0. It covers basic Python programming, functions, lists, NumPy, Pandas, data analysis and data visualization using Matplotlib.

## Contents

q1.py -Basic list operations using loops, including finding the largest and smallest values, calculating the sum, counting even and odd numbers, and reversing the list.

q2.py -A function called process_list(numbers) which works on a copy of the original list, removes negative values, adds 0, and sorts the result.

q3.py -Checks for prime numbers up to a given value of N.

q4.py -Introduces NumPy arrays and basic operations such as mean, maximum, minimum, standard deviation, addition of values and boolean indexing.

q5.py -Loads the student performance dataset and performs some basic analysis.

q6.py -Uses the processed student data to create a few different visualizations: Student vs Final Score, Hours Studied vs Final Score, Distribution of Final Scores, Attendance vs Final Score

## Prerequisites
Before running this project, ensure you have the following installed:
* *Python 3.8 or higher*
* *Pip* (Python package installer)

## Installation & Setup
1. *Clone or download this repository* to your local machine.
2. *Navigate into the project directory*
    cd Task_0
3. *Install the required Python libraries*:
    pip install numpy pandas matplotlib

## How to Run the Project

The first four questions can be run independently:
python q1.py
python q2.py
python q3.py
python q4.py

For Q5 and Q6, run them in order:
python q5.py
Q5 reads student_performance.csv, performs the required analysis, and creates the processed CSV file.
Then run:
python q6.py
Q6 uses the processed dataset and generates four graphs inside the plots/ folder.

## Output

The project produces:
A processed student performance CSV file
A bar chart of student final scores
A scatter plot of hours studied vs final score
A histogram showing the distribution of final scores
A scatter plot of attendance vs final score

## Dependencies

The project uses:
NumPy — numerical and array operations
Pandas — CSV and tabular data analysis
Matplotlib — data visualization
