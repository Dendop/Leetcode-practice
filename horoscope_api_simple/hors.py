import requests
import json


def main():
    print("Accepted signs: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces\nDay:TODAY,TOMORROW,YESTERDAY")
    sign = input("Sign:").capitalize()
    day = input("Day:").upper()
    
    valid_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    valid_days = ["TODAY", "TOMORROW", "YESTERDAY"]
    
    if sign not in valid_signs:
        print("Invalid sign")
        return False
    if day not in valid_days:
        print("Invalid day")
        return False

    url = f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={sign}&day={day}"
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            
            data = response.json()
            if data["success"]:
                print(f"\n {sign.capitalize()}'s Horoscope for {day.capitalize()}")
                print(f"\n{data['data']['horoscope_data']}\n")
            else:
                print("API returned error")
                
        else:
            print(f"Error: API request returned {response.status_code}")
    
    except Exception as e:
        print("An error occured: {e}")

if __name__ == "__main__":
    main()