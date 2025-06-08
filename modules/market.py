import datetime

def get_market_prices(crop: str) -> str:
    today = datetime.datetime.now().strftime('%d %b %Y')
    dummy_prices = {
        'wheat': 2200,
        'rice': 2000,
        'maize': 1850,
        'sugarcane': 310
    }

    crop_lower = crop.lower()
    price = dummy_prices.get(crop_lower)
    if price:
        return f"{crop.title()} market price on {today} is ₹{price}/quintal"
    else:
        return "Live price not found. Try common crops like wheat, rice."
