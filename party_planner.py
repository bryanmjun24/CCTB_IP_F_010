#!/usr/bin/env python3
import cgi
import sys
import json

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
    ("Cleaning Service", 11)
]

def main():
    if len(sys.argv) < 2:
        print("Content-Type: text/html\n")
        print("<h3>Error: No input provided.</h3>")
        return

    indices_input = sys.argv[1]
    try:
        indices = list(map(int, indices_input.split(",")))
    except ValueError:
        print("Content-Type: text/html\n")
        print("<h3>Error: Invalid input. Please enter valid indices.</h3>")
        return

    selected_items = [party_items[i] for i in indices if 0 <= i < len(party_items)]
    if not selected_items:
        print("Content-Type: text/html\n")
        print("<h3>Error: No valid items selected.</h3>")
        return

    values = [item[1] for item in selected_items]
    base_code = values[0]
    for v in values[1:]:
        base_code &= v

    if base_code == 0:
        final_code = base_code + 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        final_code = base_code - 2
        message = "Let's keep it classy!"
    else:
        final_code = base_code
        message = "Chill vibes only!"

    # HTML output
    print("<h2>Party Plan Results</h2>")
    print("<p><strong>Selected Items:</strong> " + ", ".join([item[0] for item in selected_items]) + "</p>")
    print(f"<p><strong>Base Party Code:</strong> {base_code}</p>")
    print(f"<p><strong>Final Party Code:</strong> {final_code}</p>")
    print(f"<p><strong>Message:</strong> {message}</p>")

if __name__ == "__main__":
    main()
