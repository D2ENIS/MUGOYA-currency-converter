import requests
import time

# Terminal colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def convert_currency(amount, from_currency, to_currency):
    """Fetches live exchange rates and converts the given amount."""
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    response = requests.get(url, timeout=10)
    data = response.json()

    if data.get("result") != "success":
        return None

    rates = data.get("rates", {})
    if to_currency not in rates:
        return None

    rate = rates[to_currency]
    converted_amount = amount * rate
    return converted_amount, rate


print("\n==========================================")
print(CYAN + "   💱 LIVE CURRENCY CONVERTER 💱" + RESET)
print("==========================================")
print("Popular codes: USD, EUR, GBP, UGX, KES, JPY, CAD")

while True:
    print("\n------------------------------------------")
    from_curr = input("🌍 Convert FROM (e.g. USD) or type 'exit': ").upper().strip()

    if from_curr == "EXIT":
        print(CYAN + "\n👋 Thanks for using the Live Currency Converter!\n" + RESET)
        break

    to_curr = input("🎯 Convert TO (e.g. UGX, EUR, KES): ").upper().strip()

    try:
        amount = float(input(f"💵 Amount in {from_curr}: "))
    except ValueError:
        print(RED + "❌ Please enter a valid number for the amount." + RESET)
        continue

    print("Fetching live exchange rates...")
    time.sleep(0.5)

    try:
        result = convert_currency(amount, from_curr, to_curr)

        if result is None:
            print(RED + "❌ Invalid currency code. Check your 3-letter codes and try again." + RESET)
        else:
            converted_amount, rate = result
            print("\n==========================================")
            print(GREEN + f"✅ {amount:,.2f} {from_curr} = {converted_amount:,.2f} {to_curr}" + RESET)
            print(YELLOW + f"📈 Live Rate: 1 {from_curr} = {rate:,.4f} {to_curr}" + RESET)
            print("==========================================")

    except requests.exceptions.RequestException:
        print(RED + "❌ Network error: Could not connect to the exchange rate server." + RESET)