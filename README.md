# Python Live Currency Converter

A real-time command-line currency converter built with Python that fetches live exchange rates from an external API.

## Features
- **Live Exchange Rates:** Connects to the ExchangeRate-API open endpoint for up-to-date conversion rates across 160+ currencies.
- **Modular Function Design:** Separates API fetching and conversion math into a clean reusable `convert_currency()` function.
- **Formatted Output:** Displays converted totals with comma separators and exact unit exchange rates.
- **Error Handling:** Gracefully handles invalid 3-letter currency codes, non-numeric amounts, and offline network errors.

## Setup & How to Run
1. Install the required `requests` library:
   ```bash
   pip install requests
   ```
2. Run the program:
   ```bash
   python currency_converter.py
   ```

## What I Learned
- Writing reusable functions with **`def`** and **`return`**
- Installing and importing third-party packages using **`pip`** and **`requests`**
- Fetching and parsing live **JSON** responses from a web **API**
- Handling network and input exceptions with **`try / except`**
