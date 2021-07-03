from countryinfo import CountryInfo

country_name=input('Enter Any countory: ')
country=CountryInfo(country_name)

info=country.info()
for key , value in info.items():
    print(f'{key} : {value}')
 

