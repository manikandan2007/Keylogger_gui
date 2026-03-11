def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin=celsius+273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius=kelvin-273.15
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    celsius=fahrenheit_to_celsius(fahrenheit)
    kelvin=celsius_to_kelvin(celsius)
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    celsius=kelvin_to_celsius(kelvin)
    fahrenheit=celsius_to_fahrenheit(celsius)
    return fahrenheit

if __name__=="__main__":
    celsius=25
    fahrenheit=celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees celsius is equal to {fahrenheit} degrees Fahrenheit.")

    fahrenheit=77
    celsius=fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees fahrenheit is equal to {celsius} degrees celsius.")

    celsius=30
    kelvin=celsius_to_kelvin(celsius)
    print(f"{celsius} degrees celsius is equal to {kelvin} Kelvin.")

    kelvin=300
    celsius=kelvin_to_celsius(kelvin)
    print(f"{kelvin} Kelvin is equal to {celsius} degrees Celsius.")

    fahrenheit=90
    kelvin=fahrenheit_to_kelvin(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is equal to {kelvin} Kelvin.")

    kelvin=400
    fahrenheit=kelvin_to_fahrenheit(kelvin)
    print(f"{kelvin} Kelvin is equal to {fahrenheit} degrees Fahrenheit.")
    
