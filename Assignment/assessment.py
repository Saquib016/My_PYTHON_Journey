import urllib.request
from html.parser import HTMLParser

class DocTableParser(HTMLParser):
    """
    A custom HTML parser to extract table data from the Google Doc.
    It ignores irrelevant tags and captures text inside table cells.
    """
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_tr = False
        self.in_td = False
        self.current_cell = []
        self.current_row = []
        self.tables = []
        self.current_table = []

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.in_table = True
            self.current_table = []
        elif tag == 'tr' and self.in_table:
            self.in_tr = True
            self.current_row = []
        elif tag in ('td', 'th') and self.in_tr:
            self.in_td = True
            self.current_cell = []

    def handle_endtag(self, tag):
        if tag == 'table':
            self.in_table = False
            if self.current_table:
                self.tables.append(self.current_table)
        elif tag == 'tr' and self.in_table:
            self.in_tr = False
            if self.current_row:
                self.current_table.append(self.current_row)
        elif tag in ('td', 'th') and self.in_tr:
            self.in_td = False
            # Concatenate and strip to clean up cell contents cleanly
            self.current_row.append(''.join(self.current_cell).strip())

    def handle_data(self, data):
        if self.in_td:
            self.current_cell.append(data)


def print_secret_message(url: str) -> None:
    """
    Fetches the Google Doc from the given URL, parses the data grid, 
    and prints the deciphered message.
    """
    # 1. Fetch the HTML content
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return
        
    # 2. Parse the HTML to extract table values
    parser = DocTableParser()
    parser.feed(html)
    
    # 3. Locate the correct table that holds the coordinate data
    target_table = None
    for tbl in parser.tables:
        if not tbl:
            continue
        headers = [h.lower() for h in tbl[0]]
        # Look for typical keywords in the table headers to verify we found the correct table
        if any('x' in h for h in headers) and any('y' in h for h in headers):
            target_table = tbl
            break
            
    # Fallback to the first table if no explicit header was found
    if not target_table and parser.tables:
        target_table = parser.tables[0]
        
    if not target_table:
        print("No valid table found in the document.")
        return
        
    # 4. Determine column indices dynamically
    headers = [h.lower() for h in target_table[0]]
    x_idx, char_idx, y_idx = 0, 1, 2  # default indices
    is_header = False
    
    if any('x' in h for h in headers):
        is_header = True
        for i, h in enumerate(headers):
            if 'x' in h: x_idx = i
            elif 'y' in h: y_idx = i
            elif 'char' in h: char_idx = i
            
    # Read row data
    data_rows = target_table[1:] if is_header else target_table
    
    # 5. Extract coordinate data & determine grid dimensions
    max_x = 0
    max_y = 0
    parsed_data = []
    
    for row in data_rows:
        if len(row) <= max(x_idx, y_idx, char_idx):
            continue
            
        x_str = row[x_idx]
        y_str = row[y_idx]
        char = row[char_idx]
        
        # Verify it's a valid coordinate record
        if not x_str.isdigit() or not y_str.isdigit():
            continue
            
        x = int(x_str)
        y = int(y_str)
        
        # In a published Doc, intentionally empty grid positions read as empty strings post-strip. 
        # But we default the background to spaces anyway.
        if char == '':
            char = ' '
            
        parsed_data.append((x, y, char))
        if x > max_x: max_x = x
        if y > max_y: max_y = y
        
    if not parsed_data:
        print("No valid coordinate data found.")
        return
        
    # 6. Initialize grid with empty spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # 7. Populate grid
    for x, y, char in parsed_data:
        grid[y][x] = char
        
    # 8. Print the grid top-to-bottom
    # (0, 0) corresponds to the bottom-left point on a Cartesian plane, requiring us to map backwards starting from max_y
    for y in range(max_y, -1, -1):
        print(''.join(grid[y]))

# Example usage:
print_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")