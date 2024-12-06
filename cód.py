import tkinter as tk
from tkinter import messagebox

# Taxas de câmbio fixas
EXCHANGE_RATES = {
    "USD": {"BRL": 5.30, "EUR": 0.90, "GBP": 0.78},
    "BRL": {"USD": 0.19, "EUR": 0.17, "GBP": 0.15},
    "EUR": {"USD": 1.11, "BRL": 5.87, "GBP": 0.86},
    "GBP": {"USD": 1.28, "BRL": 6.80, "EUR": 1.16},
}

def convert_currency():
    """
    Converte o valor entre as moedas selecionadas.
    """
    try:
        amount = float(amount_entry.get())
        base_currency = from_currency_var.get()
        target_currency = to_currency_var.get()

        if base_currency == target_currency:
            messagebox.showerror("Erro", "Selecione moedas diferentes para a conversão.")
            return

        rate = EXCHANGE_RATES.get(base_currency, {}).get(target_currency)
        if rate is None:
            messagebox.showerror("Erro", "Conversão entre as moedas selecionadas não está disponível.")
            return

        converted_amount = amount * rate
        result_label.config(text=f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")

# Configuração da janela principal
root = tk.Tk()
root.title("Conversor de Moedas")

# Título
title_label = tk.Label(root, text="Conversor de Moedas", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Entrada do valor
amount_label = tk.Label(root, text="Valor:")
amount_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
amount_entry = tk.Entry(root, width=20)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

# Seleção de moeda de origem
from_currency_label = tk.Label(root, text="De:")
from_currency_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
from_currency_var = tk.StringVar(root)
from_currency_var.set("USD")  # Valor padrão
from_currency_menu = tk.OptionMenu(root, from_currency_var, *EXCHANGE_RATES.keys())
from_currency_menu.grid(row=2, column=1, padx=10, pady=5)

# Seleção de moeda de destino
to_currency_label = tk.Label(root, text="Para:")
to_currency_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
to_currency_var = tk.StringVar(root)
to_currency_var.set("BRL")  # Valor padrão
to_currency_menu = tk.OptionMenu(root, to_currency_var, *EXCHANGE_RATES.keys())
to_currency_menu.grid(row=3, column=1, padx=10, pady=5)

# Botão de conversão
convert_button = tk.Button(root, text="Converter", command=convert_currency, bg="#4CAF50", fg="white")
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Resultado
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Inicia o loop da interface gráfica
root.mainloop()
