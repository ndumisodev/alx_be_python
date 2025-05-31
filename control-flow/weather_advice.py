# weather_advice.py

weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide Clothing Recommendations based on input
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    # Handle unexpected input
    print("Sorry, I don't have recommendations for this weather.")


# --- Potential Outputs ---
# Example 1: User enters 'sunny'
# What's the weather like today? (sunny/rainy/cold): sunny
# Wear a t-shirt and sunglasses.

# Example 2: User enters 'rainy'
# What's the weather like today? (sunny/rainy/cold): rainy
# Don't forget your umbrella and a raincoat.

# Example 3: User enters 'COLD' (case-insensitive due to .lower())
# What's the weather like today? (sunny/rainy/cold): COLD
# Make sure to wear a warm coat and a scarf.

# Example 4: User enters 'windy' (unrecognized input)
# What's the weather like today? (sunny/rainy/cold): windy
# Sorry, I don't have recommendations for this weather.