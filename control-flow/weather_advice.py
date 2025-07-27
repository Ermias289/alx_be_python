weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

def provide_weather_advice(weather):
    if weather=='sunny':
        return "Wear a t-shirt and sunglasses."
    elif weather=='rainy':
        return "Don't forget your umbrella and a raincoat."
    elif weather=='cold':
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."
    
if __name__ == "__main__":
    advice = provide_weather_advice(weather)
    print(advice)