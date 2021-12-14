# SDEV140-FinalProject
    SDEV 140: (Tues & Thurs.)
    FINAL Project: Python_GUI_Application Program Name: Tax Deduction Calculator
    Document Title: Tax Deduction GUI app User Manual Author: Cheryl Borst
    Date of last revision: 12/13/2021

Welcome User!

This Python GUI application is designed to let the user enter a series of dollar amounts (for cash and in-kind donations) the user personally contributed to approved charities throughout the tax year. Once the user has completed their entries, the application will total the donations, and display the result in dollars and cents. This total can then be compared with the IRS requirements on the Form 1040 to determine whether or not the user will benefit from itemizing their taxes

Note: In-Kind Donations are the estimated current resale value of donated goods, such as clothing, vehicles, household goods, and other items given to an IRS approved charity.

# INSTRUCTIONS for use
1. Users should make sure to have the latest version of Python installed on their computer. Python is a free source programming language that may be obtained via download at the following site: https://www.python.org/
2. This Python GUI application imports tkinter a package interface that is included in the standard Python GUI toolkit, so the user should have all the needed tools to run this program after downloading it from GitHub once the program is installed on their computer.
3. This program is available at GitHub.
https://github.com/CAborst/SDEV140-FinalProject/blob/main/FP.TaxDeductionCalculator.py
4. If the user has a GitHub account, they can clone the repository. Then run the code in a Python shell.
5. If the user does NOT have a GitHub account, then the user can copy the code by highlighting it, then paste it into the IDLE shell (included with the Python download and installation process). The user then saves the file in a new file, and then selects Run Module to use the calculator.
6. User will enter a numeric value of dollars and cents into the entry box.
7. User can continue to submit values, as long as desired, then select the Compute Total Value to see the Total Donations Value displayed.

## USER INPUT (Buttons)
User selects one of 3 GUI buttons: Submit Value(to enter a dollar value), Compute Total Value(to add the entries in a running total and display the total), or Quit(to exit the program and close the window).

## USER INPUT (Entry box) 
User enters the dollar amount of cash, check or charge donated OR the estimated value of the goods donated (float)
  
# VARIABLES
* running_total(float)
* ntrcash(float)
* submit_value(float)
* total_value(float) 
* donation_total(float)

# OUTPUT 
* donation_total: calculated combined total of donations(float), presented in dollars and cents.

# Validation Testing
Consisted of entering a variety of numerical combinations with and without decimal points. Values exceeding limits, and alphabet letters, etc. Integers, decimals, and no decimals all worked fine. Alphabet letters caused the IDLE window to report errors, however, the alphabet letters were deletable, and the code could continue where it left off.
