import csv
import os

DATASET = "movies_dataset.csv"


def _detect_fields(fieldnames):
    """Heuristically choose columns for year and revenue."""
    year_field = None
    revenue_field = None
    for name in fieldnames:
        lower = name.lower()
        if year_field is None and ("year" in lower or "release_date" in lower):
            year_field = name
        if revenue_field is None and any(token in lower for token in ["revenue", "gross", "box_office", "earning"]):
            revenue_field = name
    return year_field, revenue_field


def load_movies(file_path=DATASET):
    """Load movies from CSV and return list of (year, revenue) tuples."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset '{file_path}' not found.")

    movies = []
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        year_field, revenue_field = _detect_fields(reader.fieldnames)
        if not year_field or not revenue_field:
            raise ValueError("Could not detect year or revenue columns in dataset.")
        for row in reader:
            year_raw = row.get(year_field)
            revenue_raw = row.get(revenue_field)
            if year_raw is None or revenue_raw is None:
                continue
            # Parse the year (handle formats like YYYY-MM-DD)
            year_str = str(year_raw).split("-", 1)[0].strip()
            revenue_str = str(revenue_raw).replace("$", "").replace(",", "").strip()
            try:
                year = int(year_str)
                revenue = float(revenue_str)
                movies.append((year, revenue))
            except ValueError:
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
