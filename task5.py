import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("USD Currency Converter")
        self.root.geometry("400x300")

        # Hardcoded exchange rates (as of a specific date)
        self.exchange_rates = {
            'EUR': 0.85,  # 1 USD = 0.85 EUR
            'GBP': 0.75,  # 1 USD = 0.75 GBP
            'INR': 75.0,  # 1 USD = 75.0 INR
            'AUD': 1.40,  # 1 USD = 1.40 AUD
            'CAD': 1.25   # 1 USD = 1.25 CAD
        }

        # Label and entry for USD amount
        self.usd_label = ttk.Label(root, text="Amount in USD:")
        self.usd_label.pack(pady=10)
        self.usd_entry = ttk.Entry(root, width=20)
        self.usd_entry.pack(pady=10)

        # Dropdown menu for selecting target currency
        self.currency_label = ttk.Label(root, text="Select target currency:")
        self.currency_label.pack(pady=10)
        self.currency_var = tk.StringVar(value=list(self.exchange_rates.keys())[0])
        self.currency_dropdown = ttk.Combobox(root, textvariable=self.currency_var, values=list(self.exchange_rates.keys()))
        self.currency_dropdown.pack(pady=10)

        # Button for conversion
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.pack(pady=10)

        # Label to display the result
        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def convert_currency(self):
        try:
            usd_amount = float(self.usd_entry.get())
            target_currency = self.currency_var.get()
            converted_amount = usd_amount * self.exchange_rates[target_currency]
            self.result_label.config(text=f"{usd_amount} USD = {converted_amount:.2f} {target_currency}")
        except ValueError:
            self.result_label.config(text="Please enter a valid amount.")
        except KeyError:
            self.result_label.config(text="Invalid target currency.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
