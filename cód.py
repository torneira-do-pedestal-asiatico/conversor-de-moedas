def get_exchange_rate(base_currency, target_currency):
    """
    Retorna a taxa de câmbio fixa entre duas moedas.
    """
    exchange_rates = {
        "USD": {"BRL": 5.30, "EUR": 0.90, "GBP": 0.78},
        "BRL": {"USD": 0.19, "EUR": 0.17, "GBP": 0.15},
        "EUR": {"USD": 1.11, "BRL": 5.87, "GBP": 0.86},
        "GBP": {"USD": 1.28, "BRL": 6.80, "EUR": 1.16},
    }

    if base_currency in exchange_rates and target_currency in exchange_rates[base_currency]:
        return exchange_rates[base_currency][target_currency]
    else:
        return None

def convert_currency(amount, rate):
    """
    Converte o valor usando a taxa de câmbio.
    """
    return amount * rate

def main():
    print("=== Conversor de Moedas ===")
    print("Moedas disponíveis: USD, BRL, EUR, GBP")
    print("Digite 'sair' a qualquer momento para encerrar o programa.")

    while True:
        # Solicita a moeda base
        base_currency = input("Digite a moeda de origem (exemplo: USD, BRL): ").upper()
        if base_currency == "SAIR":
            print("Encerrando o programa...")
            break

        # Solicita a moeda de destino
        target_currency = input("Digite a moeda de destino (exemplo: USD, EUR): ").upper()
        if target_currency == "SAIR":
            print("Encerrando o programa...")
            break

        # Solicita o valor a ser convertido
        try:
            amount = float(input(f"Digite o valor em {base_currency} que deseja converter: "))
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
            continue

        # Obtém a taxa de câmbio
        rate = get_exchange_rate(base_currency, target_currency)
        if rate is None:
            print("Erro: Conversão entre as moedas selecionadas não está disponível.")
            continue

        # Realiza a conversão
        converted_amount = convert_currency(amount, rate)
        print(f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")

        # Pergunta ao usuário se deseja realizar outra conversão
        again = input("Deseja realizar outra conversão? (s/n): ").lower()
        if again != 's':
            print("Obrigado por usar o conversor de moedas!")
            break

if __name__ == "__main__":
    main()
