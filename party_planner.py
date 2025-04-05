
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

def display_items():
    print("Available Party Items:")
    for index, (item, _) in enumerate(party_items):
        print(f"{index}: {item}")

def get_user_selection():
    indices = input("Enter the indices of items you want (comma-separated): ")
    try:
        selected_indices = [int(i.strip()) for i in indices.split(",")]
        return selected_indices
    except ValueError:
        print("Invalid input. Please enter comma-separated numbers.")
        return get_user_selection()

def calculate_base_code(selected_indices):
    if not selected_indices:
        return 0
    values = [party_items[i][1] for i in selected_indices]
    base_code = values[0]
    for val in values[1:]:
        base_code &= val
    return base_code

def modify_code(base_code):
    message = ""
    if base_code == 0:
        base_code += 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        base_code -= 2
        message = "Let's keep it classy!"
    else:
        message = "Chill vibes only!"
    return base_code, message

def generate_html(selected_indices, final_code, message):
    selected_items = [party_items[i][0] for i in selected_indices]
    html = f"""
    <html>
    <head><title>Party Planner Result</title></head>
    <body>
        <h1>Selected Party Items</h1>
        <ul>
            {''.join(f"<li>{item}</li>" for item in selected_items)}
        </ul>
        <h2>Final Party Code: {final_code}</h2>
        <p>{message}</p>
    </body>
    </html>
    """
    return html

def main():
    display_items()
    selected_indices = get_user_selection()
    base_code = calculate_base_code(selected_indices)
    final_code, message = modify_code(base_code)
    html_output = generate_html(selected_indices, final_code, message)
    print("\nHTML Output:\n")
    print(html_output)

if __name__ == "__main__":
    main()
