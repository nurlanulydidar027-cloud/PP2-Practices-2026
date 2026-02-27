"""
receipt_parser.py
Parses a raw text receipt and extracts items, prices, and totals.
"""

import re
import os
# import json


def parse_receipt(filepath: str) -> dict:
    """Read and parse a receipt from a text file."""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    items = []
    subtotal = None
    tax = None
    total = None

    # Regex: match lines like "Item name   1234" (name + whitespace + number)
    item_pattern = re.compile(r"^(.+?)\s{2,}(\d+(?:\.\d{1,2})?)$")
    subtotal_pattern = re.compile(r"subtotal[:\s]+(\d+(?:\.\d{1,2})?)", re.IGNORECASE)
    tax_pattern = re.compile(r"tax[^:]*:\s*(\d+(?:\.\d{1,2})?)", re.IGNORECASE)
    total_pattern = re.compile(r"^total[:\s]+(\d+(?:\.\d{1,2})?)", re.IGNORECASE)

    in_items_section = False

    for line in lines:
        line = line.strip()

        if line.lower() == "items:":
            in_items_section = True
            continue

        # Stop items section at separator or summary lines
        if in_items_section and line.startswith("="):
            in_items_section = False

        if in_items_section:
            match = item_pattern.match(line)
            if match:
                name = match.group(1).strip()
                price = float(match.group(2))
                items.append({"name": name, "price": price})

        # Parse summary lines
        if subtotal_pattern.search(line):
            subtotal = float(subtotal_pattern.search(line).group(1))
        elif tax_pattern.search(line):
            tax = float(tax_pattern.search(line).group(1))
        elif total_pattern.search(line):
            total = float(total_pattern.search(line).group(1))

    return {
        "items": items,
        "subtotal": subtotal,
        "tax": tax,
        "total": total,
    }


def display_receipt(data: dict) -> None:
    """Print parsed receipt data in a readable format."""
    print("=" * 40)
    print(f"{'PARSED RECEIPT':^40}")
    print("=" * 40)
    print(f"\n{'Item':<25} {'Price':>10}")
    print("-" * 36)

    for item in data["items"]:
        print(f"{item['name']:<25} {item['price']:>10.2f}")

    print("-" * 36)
    if data["subtotal"] is not None:
        print(f"{'Subtotal':<25} {data['subtotal']:>10.2f}")
    if data["tax"] is not None:
        print(f"{'Tax':<25} {data['tax']:>10.2f}")
    if data["total"] is not None:
        print(f"{'TOTAL':<25} {data['total']:>10.2f}")
    print("=" * 40)

    # Verify totals
    calculated = sum(item["price"] for item in data["items"])
    print(f"\nCalculated sum of items: {calculated:.2f}")
    if data["subtotal"] and abs(calculated - data["subtotal"]) < 0.01:
        print("✓ Subtotal matches!")
    else:
        print(f"  (Note: subtotal in receipt is {data['subtotal']})")


def main():
    filepath = os.path.join(os.path.dirname(__file__), "raw.txt")
    print(f"Parsing receipt from: {filepath}\n")
    data = parse_receipt(filepath)
    display_receipt(data)

    # print("\n---JSON OUTPUT---")
    # print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
