"""Convert temperatures from Fahrenheit to Celsius."""


def fahrenheit_to_celsius(temperature_fahrenheit):
    """Return the temperature in Celsius."""
    return (temperature_fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print(fahrenheit_to_celsius(212))