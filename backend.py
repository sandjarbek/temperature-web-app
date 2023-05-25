API_key = "308acb57db569aab2752b58bbcd42265"
import requests
def get_data(place, forecast_days):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    responce = requests.get(url)
    data=responce.json()
    filtered_data=data["list"]
    nr_values= 8*forecast_days
    filtered_data=filtered_data[:nr_values]

    return filtered_data


if __name__==("__main__"):
    print(get_data("Tokyo", 3))
    #
    # def get_data(days):
    #     dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    #     temperatures = [11, 12, 15]
    #     temperatures = [days * i for i in temperatures]
    #     return dates, temperatures