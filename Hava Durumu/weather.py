import requests
class Weather():
    def get_weather(city):    
        try:
            url = f"https://wttr.in/{city.replace(' ', '+')}?format=3"
            response = requests.get(url)
            response.raise_for_status()

            weather_data = response.text.strip()

            if weather_data:
                return (weather_data.replace("+"," "))
            else:
                return "Hava durumu bilgisi alınamadı."
                

        except requests.exceptions.RequestException:
                print("Hava durumu bilgisi alınamadı.")
        
