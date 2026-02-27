# Practice 5 — Receipt Parser

## Description

A Python script that reads a raw supermarket receipt from a text file (`raw.txt`), extracts all items with their prices, and displays a formatted summary including subtotal, tax, and total.

## Files

| File | Description |
|------|-------------|
| `receipt_parser.py` | Main script that parses and displays the receipt |
| `raw.txt` | Sample raw receipt text file |

## How to Run

Make sure both files are in the same directory, then run:

```bash
python receipt_parser.py
```

## Example Output

```
========================================
             PARSED RECEIPT
========================================

Item                          Price
------------------------------------
Milk 2L                     1200.00
Bread                        450.00
...
------------------------------------
Subtotal                    7650.00
Tax                          918.00
TOTAL                       8568.00
========================================
```

## Concepts Used

- File I/O (`open`, `readlines`)
- Regular expressions (`re` module)
- String formatting
- Functions and dictionaries
