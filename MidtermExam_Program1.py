def main():
    class TemperatureConversion:

        def __init__(self, temp=1):
            self._temp = temp

    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * (5/9)

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    convert = KelvinToCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Kelvin")

    convert = FahrenheitToCelsius(tempInFahrenheit)
    print(str(convert.conversion()) + " Fahrenheit")


main()