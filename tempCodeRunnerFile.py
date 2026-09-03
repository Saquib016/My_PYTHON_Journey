import pandas as pd


def decode_secret_message(url):
    tables = pd.read_html(url)

    df = tables[0]

    # Normalize column names
    df.columns = [str(col).strip().lower() for col in df.columns]

    # Find columns
    char_col = next(col for col in df.columns if "char" in col)
    x_col = next(col for col in df.columns if "x" in col and "coordinate" in col)
    y_col = next(col for col in df.columns if "y" in col and "coordinate" in col)

    # Convert coordinates to integers
    df[x_col] = df[x_col].astype(int)
    df[y_col] = df[y_col].astype(int)

    # Find grid size
    max_x = df[x_col].max()
    max_y = df[y_col].max()

    # Create grid filled with spaces
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place characters
    for _, row in df.iterrows():
        x = row[x_col]
        y = row[y_col]
        char = str(row[char_col])

        grid[y][x] = char

    # Print from top to bottom
    for row in reversed(grid):
        print("".join(row).rstrip())


decode_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)
