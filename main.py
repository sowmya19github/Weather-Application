


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import requests, json
    api_key = "82397016eccdb1020f0ec30c8ddd989b"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Hyderabad"
    complete_url =  base_url + "appid=" + api_key +"&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    print(type(x))
    print(x['main']['pressure'])




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
