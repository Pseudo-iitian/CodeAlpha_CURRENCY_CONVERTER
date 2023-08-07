import tkinter as tk
from tkinter import Scrollbar, Text
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x250")

        self.currency_rates = CurrencyRates()

        self.create_widgets()

    def create_widgets(self):
        self.lbl_from_currency = tk.Label(self.root, text="From Currency:")
        self.lbl_from_currency.pack()

        self.from_currency_var = tk.StringVar()
        self.from_currency_var.set("USD")  # Default "From" currency (USD)

        self.from_currency_dropdown = tk.OptionMenu(self.root, self.from_currency_var, *self.get_currency_codes())
        self.from_currency_dropdown.pack()

        self.lbl_to_currency = tk.Label(self.root, text="To Currency:")
        self.lbl_to_currency.pack()

        self.to_currency_var = tk.StringVar()
        self.to_currency_var.set("INR")  # Default "To" currency (INR)

        self.to_currency_dropdown = tk.OptionMenu(self.root, self.to_currency_var, *self.get_currency_codes())
        self.to_currency_dropdown.pack()

        self.lbl_amount = tk.Label(self.root, text="Amount:")
        self.lbl_amount.pack()

        self.amount_entry = tk.Entry(self.root, width=15)
        self.amount_entry.pack()

        self.btn_convert = tk.Button(self.root, text="Convert", command=self.convert_currency)
        self.btn_convert.pack()

    def get_currency_codes(self):
        # You can add more currency codes as needed.
        return ["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF", "CNY"]

    def convert_currency(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = self.amount_entry.get()

        if not amount:
            self.show_result("Please enter an amount to convert.")
            return

        try:
            amount = float(amount)
        except ValueError:
            self.show_result("Invalid amount.")
            return

        if from_currency == to_currency:
            self.show_result("Cannot convert to the same currency.")
            return

        exchange_rate = self.currency_rates.get_rate(from_currency, to_currency)
        converted_amount = round(amount * exchange_rate, 2)

        result_text = f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"
        self.show_result(result_text)

    def show_result(self, result_text):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Conversion Result")
        popup_window.geometry("400x250")

        scrollbar = Scrollbar(popup_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        result_text_box = Text(popup_window, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        result_text_box.pack()

        result_text_box.insert(tk.END, result_text)

        scrollbar.config(command=result_text_box.yview)


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
