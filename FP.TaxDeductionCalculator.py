# FINAL Project: Python_GUI_Application
# Program name: Tax Deduction Calculator
# Author: Cheryl Borst
# Date of last revision: 12/13/2021 
# Summary: This GUI lets the user enter a series of dollar amounts for cash and in-kind
#          donations.  The program totals the dollar values, so the user can compare to see
#          if it is worth using itemized deductions onthe IRS Form 1040.
#   Note: In-Kind Donations are the estimated current resale vale of donated goods, such as clothing,
#                           vehicles, household goods, and other items given to a approved charity.
# 
#  USER INPUT: User selects one of 3 GUI buttons: Submit Value(to enter a dollar value), Compute Total
#              Value(to add the entries in a running total and display the total), or Quit(to exit
#              the program and close the window).
#  USER INPUT: ntrcash: value of cash, check or charge donated or the estimated value of the goods donated
#              (float)
#
#  VARIABLES: running_total(float), ntrcash(float), submit_value(float), total_value(float),
#             donation_total(float) 
#
#  OUTPUT:
#   donation_total: calculated combined total of donations(float)

import tkinter

class TDCalcGUI:
    def __init__(self):
        self.running_total = 0 """This is a running total of entries."""
        
        # Create main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Tax Deduction Calculator")

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create input widgets for top frame
        self.ntrcash_label = tkinter.Label(self.top_frame, \
                                           text = "Enter a Cash or In-kind value: ")
        self.ntrcash_entry = tkinter.Entry(self.top_frame, width = 15)

        # Pack the top frame widgets
        self.ntrcash_label.pack(side="left")
        self.ntrcash_entry.pack(side="left")

        # Create the middle frame label
        self.results_label = tkinter.Label(self.mid_frame, \
                                           text = "Computed Donation Total: $ ")
        
        # Create a computed total widget
        self.donation_total = tkinter.StringVar() """The total of donation entries for the widget."""
        self.donation_total_label = tkinter.Label(self.mid_frame, \
                                                  textvariable = self.donation_total)
        
        # Pack the middle frame widgets
        self.results_label.pack(side="left")
        self.donation_total_label.pack(side="left")
        
        # Create the buttons in the bottom frame
        self.SbmtVal_button = tkinter.Button(self.bottom_frame, \
                                             text = "Submit Value", \
                                             command = self.submit_value)
        self.NxtVal_button = tkinter.Button(self.bottom_frame, \
                                            text = "Compute Total Value", \
                                            command = self.total_value)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text = "Quit", \
                                          command = self.main_window.destroy)

        # Pack the bottom frame widgets
        self.SbmtVal_button.pack(side="left")
        self.NxtVal_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
    
        #Enter the inter main loop()
        tkinter.mainloop()
 
    # Define Calculation functions
    def submit_value(self):
        self.entry_amount = float(self.ntrcash_entry.get())
        self.running_total += self.entry_amount
        self.ntrcash_entry.delete(0, 'end')
        
    def total_value(self):
        self.donation_total.set(format(self.running_total, '.2f'))
        
# Create an instance of the class
donation_total = TDCalcGUI()
