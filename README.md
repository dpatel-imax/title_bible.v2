# IMAX Revenue Estimator

This project provides a simple command-line tool that loads a movie dataset from a CSV file and estimates the total IMAX revenue for a user-supplied year. It assumes IMAX receives 20% of a movie's earnings.

## Usage
1. Place your movie dataset CSV file in this directory and name it `movies_dataset.csv`.
2. Ensure the CSV contains a column that includes "year" (e.g., `year`, `release_year`, or `release_date`) and a column for revenue such as `revenue`, `gross`, or `box_office`. The script will try to detect these automatically.
3. Run the program:
   ```bash
   python3 main.py
   ```
4. When prompted, enter the year you would like to estimate IMAX revenue for.

The script will print the estimated revenue based on the sum of all movie revenues for the chosen year multiplied by 20%.
