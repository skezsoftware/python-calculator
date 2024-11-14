# Calculator application using tkinter for GUI
import tkinter as tk

class Calculator:
    def __init__(self, root):
        # Initialize the main window with title and size
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("300x400")  # Set window dimensions
        self.root.resizable(False, False)  # Prevent window resizing
        self.root.configure(bg='#333333')  # Set dark background color
        
        # Initialize variables for calculation and display
        self.current_expression = ""  # Stores the current mathematical expression
        self.display_var = tk.StringVar()  # Special tkinter variable for dynamic text display
        self.display_var.set('0')  # Set initial display value
        
        # Create the calculator display (Entry widget)
        self.display = tk.Entry(
            root, 
            textvariable=self.display_var,  # Link to StringVar for automatic updates
            justify="right",  # Right-align the text
            font=('Arial', 24),  # Set font and size
            bd=10,  # Set border width
            relief='sunken',  # Add 3D sunken effect
            bg='#000066',  # Dark blue background for display
            fg='white'  # White text color
        )
        # Position the display at the top, spanning all columns
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Define common style properties for all buttons
        self.button_style = {
            'font': ('Arial', 16, 'bold'),
            'relief': 'raised',  # 3D raised effect
            'bd': 1,  # Border width
            'bg': '#ffffff',  # White background
            'fg': '#000000',  # Black text
            'activebackground': '#e0e0e0',  # Color when button is pressed
            'activeforeground': '#000000',  # Text color when pressed
            'cursor': 'hand2',  # Hand pointer cursor on hover
            'width': 4,
            'height': 2
        }
        
        # Create and place all buttons
        self.create_buttons()
        
        # Configure grid weights for responsive layout
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        # Define button layout: (text, row, column, [columnspan])
        button_layout = [
            ('C', 1, 0),    # Clear button
            ('⌫', 1, 1),    # Backspace button
            ('%', 1, 2),    # Percentage button
            ('/', 1, 3),    # Division button
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),  # Numbers and multiply
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),  # Numbers and subtract
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),  # Numbers and add
            ('0', 5, 0, 2),  # Zero button spans 2 columns
            ('.', 5, 2),    # Decimal point
            ('=', 5, 3)     # Equals button
        ]

        # Create each button based on the layout
        for button in button_layout:
            if len(button) == 4:  # Special case for '0' button that spans 2 columns
                btn = tk.Button(
                    self.root,
                    text=button[0],
                    command=lambda x=button[0]: self.button_click(x),  # Bind click event
                    **self.button_style  # Apply common button styles
                )
                btn.grid(row=button[1], column=button[2], columnspan=button[3],
                        padx=1, pady=1, sticky="nsew")
            else:  # Normal buttons
                btn = tk.Button(
                    self.root,
                    text=button[0],
                    command=lambda x=button[0]: self.button_click(x),  # Bind click event
                    **self.button_style  # Apply common button styles
                )
                btn.grid(row=button[1], column=button[2], padx=1, pady=1, sticky="nsew")

            # Bind hover events for visual feedback
            btn.bind('<Enter>', lambda e, btn=btn: self.on_enter(btn))
            btn.bind('<Leave>', lambda e, btn=btn: self.on_leave(btn))

    def on_enter(self, btn):
        """Handle mouse enter event - change button color on hover"""
        btn.config(bg='#e0e0e0')  # Light gray background

    def on_leave(self, btn):
        """Handle mouse leave event - restore original button color"""
        btn.config(bg='#ffffff')  # White background

    def button_click(self, value):
        """Handle button clicks and update display accordingly"""
        if value == 'C':  # Clear button
            self.current_expression = ""
            self.display_var.set('0')
        
        elif value == '⌫':  # Backspace button
            self.current_expression = self.current_expression[:-1]
            if not self.current_expression:
                self.display_var.set('0')
            else:
                self.display_var.set(self.current_expression)
        
        elif value == '=':  # Equals button - calculate result
            try:
                result = eval(self.current_expression)  # Evaluate the mathematical expression
                self.display_var.set(result)
                self.current_expression = str(result)
            except:
                self.display_var.set('Error')
                self.current_expression = ""
        
        elif value == '%':  # Percentage button
            try:
                result = eval(self.current_expression) / 100
                self.display_var.set(result)
                self.current_expression = str(result)
            except:
                self.display_var.set('Error')
                self.current_expression = ""
        
        else:  # Numbers and operators
            if self.current_expression == "0":
                self.current_expression = value
            else:
                self.current_expression += value
            self.display_var.set(self.current_expression)

# Create and run the calculator application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    calculator = Calculator(root)  # Create calculator instance
    root.mainloop()  # Start the event loop