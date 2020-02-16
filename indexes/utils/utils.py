def calculate_response(symbol: str, scraper, model) -> float:
    opening, high, low = scraper.get_intraday(symbol)
    print(opening)
    pred = model.predict([[opening, high, low]])

    return float(pred)
