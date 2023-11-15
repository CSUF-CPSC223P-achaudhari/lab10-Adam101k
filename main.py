# Just using for personal testing

from bots import bot_clerk

def main():
    # Mock inventory (as would be read from 'inventory.dat')
    inventory = {
        "101": ["Notebook Paper", 2],
        "102": ["Pencils", 2],
        "103": ["Pens", 6],
        "104": ["Graph Paper", 1],
        "105": ["Paper Clips", 1],
        "106": ["Staples", 4],
        "107": ["Stapler", 7],
        "108": ["3 Ring Binder", 1],
        "109": ["Printer Paper", 1],
        "110": ["Notepad", 1]
    }

    # Test scenarios
    scenarios = [
        [],
        ['104'],
        ['106', '109', '102'],
        ['103', '108', '102', '110', '106'],
        ['106', '102', '108', '109', '103', '101', '110', '104', '107', '105']
    ]

    for items in scenarios:
        print(f"INPUT  : {items}")
        cart = bot_clerk(items, inventory)
        print(f"OUTPUT : {cart}\n")

if __name__ == "__main__":
    main()
