-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Product Information Automation with Python

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Notes](#notes)
6. [License](#license)

## Introduction

This project automates the process of filling product information into a website using Python and the `pyautogui` library. The goal is to simplify data entry tasks by automatically populating fields on a specific web page.

## Installation

Ensure Python is installed on your system. Install the required packages:

```bash
pip install pyautogui pandas openpyxl numpy
```

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/markx98/PythonAutomation.git
   cd PythonAutomation
   ```

2. **Prepare Your Data:**

   Ensure your product data is organized in a format supported by `pandas` (e.g., CSV, Excel).

3. **Configuration:**

   Adjust the parameters according to the specific fields and layout of your website.

4. **Watch Automation in Action:**

   Observe as the script fills product information on the website.

## Project Structure

```
PythonAutomation/
├── Auto/
│   ├── code.py         # Automation
│   └── products.csv    # Example product data
├── Screen-coordinates/
│   └── ScreenMark.py   # Screen coordinates marking
├── README.md           # Project README
└── License.txt         # Project LICENSE
```

## Notes

- Uses `pyautogui` for GUI automation, simulating mouse and keyboard actions. Adjust timing and coordinates as needed for your specific environment.
- Ensure all data inputs are validated and handled securely to prevent unintended actions on the website.

## License

This project is licensed under the MIT License. See the `License.txt` file for more details.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Always updating the project! markx98!
