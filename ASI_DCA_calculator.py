import requests


def get_live_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'fetch-ai,singularitynet,ocean-protocol',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    prices = response.json()
    fet_price = prices['fetch-ai']['usd']
    agix_price = prices['singularitynet']['usd']
    ocean_price = prices['ocean-protocol']['usd']
    return fet_price, agix_price, ocean_price


def calculate_asi_tokens(budget, fet_price, agix_price, ocean_price):
    # Conversion rates
    fet_to_asi = 1
    agix_to_asi = 0.433350
    ocean_to_asi = 0.433226

    # ASI tokens for the given budget
    asi_from_fet = budget / fet_price * fet_to_asi
    asi_from_agix = budget / agix_price * agix_to_asi
    asi_from_ocean = budget / ocean_price * ocean_to_asi

    return asi_from_fet, asi_from_agix, asi_from_ocean


def decide_investment(asi_from_fet, asi_from_agix, asi_from_ocean):
    max_asi = max(asi_from_fet, asi_from_agix, asi_from_ocean)
    if max_asi == asi_from_fet:
        return 'FET', asi_from_fet
    elif max_asi == asi_from_agix:
        return 'AGIX', asi_from_agix
    else:
        return 'OCEAN', asi_from_ocean


def main():
    budget = float(input("Enter your budget in USD: "))

    fet_price, agix_price, ocean_price = get_live_prices()
    asi_from_fet, asi_from_agix, asi_from_ocean = calculate_asi_tokens(budget, fet_price, agix_price, ocean_price)
    best_investment, asi_amount = decide_investment(asi_from_fet, asi_from_agix, asi_from_ocean)

    print(f"FET Price: ${fet_price}")
    print(f"AGIX Price: ${agix_price}")
    print(f"OCEAN Price: ${ocean_price}")

    print(f"ASI tokens from ${budget} investment in FET: {asi_from_fet}")
    print(f"ASI tokens from ${budget} investment in AGIX: {asi_from_agix}")
    print(f"ASI tokens from ${budget} investment in OCEAN: {asi_from_ocean}")

    print(f"The best token to invest in right now is: {best_investment}")
    print(f"Expected ASI tokens from the best investment: {asi_amount}")


if __name__ == "__main__":
    main()
