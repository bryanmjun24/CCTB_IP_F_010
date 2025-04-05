# party_planner.py
import sys

party_items = [
    ("Cake", 20),
    ("Balloons", 21),
    ("Music System", 10),
    ("Lights", 5),
    ("Catering Service", 8),
    ("DJ", 3),
    ("Photo Booth", 15),
    ("Tables", 7),
    ("Chairs", 12),
    ("Drinks", 6),
    ("Party Hats", 9),
    ("Streamers", 18),
    ("Invitation Cards", 4),
    ("Party Games", 2),
    ("Cleaning Service", 11),
]

def calculate_base_code(selected_indices):
    if not selected_indices:
        return 0, []
    values = [party_items[i][1] for i in selected_indices]
    base_code = values[0]
    breakdown = [str(values[0])]
    for val in values[1:]:
        breakdown.append(f"& {val}")
        base_code &= val
    return base_code, breakdown

def modify_code(base_code):
    if base_code == 0:
        return base_code + 5, "Epic Party Incoming!"
    elif base_code > 5:
        return base_code - 2, "Let's keep it classy!"
    else:
        return base_code, "Chill vibes only!"

def main():
    # For web: expect comma-separated indices passed as an argument
    input_str = sys.argv[1] if len(sys.argv) > 1 else input("Enter item indices separated by commas (e.g., 0, 2): ")
    selected_indices = [int(i.strip()) for i in input_str.split(",") if i.strip().isdigit()]
    selected_items = [party_items[i][0] for i in selected_indices]

    base_code, breakdown = calculate_base_code(selected_indices)
    adjusted_code, message = modify_code(base_code)

    print("Content-type: text/html\n")
    print("<html><body>")
    print("<h2>Selected Items:</h2>")
    print("<ul>")
    for item in selected_items:
        print(f"<li>{item}</li>")
    print("</ul>")
    print(f"<p>Base Party Code: {' '.join(breakdown)} = {base_code}</p>")
    if base_code == 0:
        print(f"<p>Adjusted Party Code: {base_code} + 5 = {adjusted_code}</p>")
    elif base_code > 5:
        print(f"<p>Adjusted Party Code: {base_code} - 2 = {adjusted_code}</p>")
    print(f"<p><strong>Final Party Code: {adjusted_code}</strong></p>")
    print(f"<p><strong>Message:</strong> {message}</p>")
    print("</body></html>")

if __name__ == "__main__":
    main()
