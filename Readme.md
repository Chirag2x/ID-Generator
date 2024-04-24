
# ID Card Generator

## Overview
This project generates a PDF file containing custom ID cards for employees. Each ID card includes the employee's photo, name, and title, overlayed on a pre-defined ID template.

## Prerequisites
- Python 3
- Pillow (PIL Fork)
- ReportLab

To install the required Python packages, run:
```
pip install pillow reportlab
```

## Inputs
1. `ute_id_template.png`: A pre-defined ID template image (PNG format).
2. `Book - Copy - Copy(Sheet1).csv`: A CSV file containing employee details with the columns: `Name`, `Title`, `Location`, and `ID`.
3. `Images`: A file containing all employee ID photos referenced in the CSV file.

## Usage
1. Place the `ute_id_template.png`, `Book - Copy - Copy(Sheet1).csv`, and `Images` in the same directory as the script.
2. Run the script with:
```
python idGenerator.py
```
3. The script will generate a PDF named `employee_id_cards.pdf` in the current directory with the ID cards for all employees listed in the CSV file.

## Customization
- You can modify the font size and path by changing the `font_size` and `font_path` variables in the script.
- The positions for photo and text placement can also be adjusted to fit the ID template.

## Output
- The output PDF will have the size of a standard credit card, with each page containing one ID card.
![Input Files](Outputs.png)