import csv
import os

DATASET = 'movies_dataset.csv'


def load_movies(file_path=DATASET):
    """Load movies from CSV and return list of (year, revenue) tuples."""
    movies = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset '{file_path}' not found.")
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            year = None
            revenue = None
            # attempt to find a year field
            for key in row:
                lower = key.lower()
                value = row[key]
                if year is None:
                    if lower in {'year', 'release_year', 'startyear'}:
                        year = value
                    elif lower == 'release_date' and value:
                        year = value.split('-', 1)[0]
                if revenue is None and lower in {'revenue', 'worldwide_gross', 'gross', 'box_office'}:
                    revenue = value
            try:
                year = int(str(year).strip())
                revenue = float(str(revenue).replace('$', '').replace(',', '').strip())
                movies.append((year, revenue))
            except (TypeError, ValueError):
                continue
    return movies


def estimate_imax_revenue(movies, target_year):
    """Return IMAX revenue (20%) for all movies released in target_year."""
    total = sum(rev for year, rev in movies if year == target_year)
    return total * 0.20


def main():
    try:
        movies = load_movies()
    except FileNotFoundError as e:
        print(e)
        return

    try:
        year_input = input("Enter a year to estimate IMAX revenue: ")
        target_year = int(year_input)
    except ValueError:
        print("Invalid year. Please enter a numeric year.")
        return

    imax_revenue = estimate_imax_revenue(movies, target_year)
    formatted = f"${imax_revenue:,.2f}"
    print(f"Estimated IMAX revenue for {target_year}: {formatted}")


if __name__ == '__main__':
    main()
