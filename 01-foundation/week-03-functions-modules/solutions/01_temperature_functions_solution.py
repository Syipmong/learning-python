# Solution 1: Temperature Converter Functions

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def temperature_info(temp, scale):
    """Provide information about a temperature"""
    scale = scale.lower()
    
    # Convert to Celsius for comparison
    if scale == 'f' or scale == 'fahrenheit':
        celsius = fahrenheit_to_celsius(temp)
    elif scale == 'k' or scale == 'kelvin':
        celsius = kelvin_to_celsius(temp)
    else:  # Assume Celsius
        celsius = temp
    
    info = []
    
    # Temperature comparisons
    if celsius <= 0:
        info.append("🧊 At or below freezing point of water")
    elif celsius >= 100:
        info.append("💨 At or above boiling point of water")
    elif celsius >= 37:
        info.append("🌡️ Above normal human body temperature")
    elif celsius >= 20 and celsius <= 25:
        info.append("🏠 Comfortable room temperature")
    
    # Additional insights
    if celsius < -40:
        info.append("🥶 Extremely cold - Celsius and Fahrenheit meet at -40°!")
    elif celsius > 50:
        info.append("🔥 Dangerously hot temperature")
    elif celsius < 0:
        info.append("❄️ Below freezing")
    elif celsius < 10:
        info.append("🧥 Cold - wear warm clothes")
    elif celsius > 30:
        info.append("☀️ Hot weather")
    
    return "; ".join(info) if info else "Normal temperature range"

# Additional utility functions
def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def temperature_converter_menu():
    """Interactive temperature converter"""
    print("🌡️ Temperature Converter")
    print("Available conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    try:
        choice = int(input("Choose conversion (1-6): "))
        temp = float(input("Enter temperature: "))
        
        if choice == 1:
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F")
            print(f"Info: {temperature_info(temp, 'c')}")
        elif choice == 2:
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C")
            print(f"Info: {temperature_info(temp, 'f')}")
        elif choice == 3:
            result = celsius_to_kelvin(temp)
            print(f"{temp}°C = {result:.2f}K")
            print(f"Info: {temperature_info(temp, 'c')}")
        elif choice == 4:
            if temp < 0:
                print("❌ Error: Kelvin cannot be negative!")
                return
            result = kelvin_to_celsius(temp)
            print(f"{temp}K = {result:.2f}°C")
            print(f"Info: {temperature_info(temp, 'k')}")
        elif choice == 5:
            result = fahrenheit_to_kelvin(temp)
            print(f"{temp}°F = {result:.2f}K")
            print(f"Info: {temperature_info(temp, 'f')}")
        elif choice == 6:
            if temp < 0:
                print("❌ Error: Kelvin cannot be negative!")
                return
            result = kelvin_to_fahrenheit(temp)
            print(f"{temp}K = {result:.2f}°F")
            print(f"Info: {temperature_info(temp, 'k')}")
        else:
            print("❌ Invalid choice!")
            
    except ValueError:
        print("❌ Please enter valid numbers!")

# Test your functions
if __name__ == "__main__":
    print("Testing temperature conversion functions...")
    
    # Test basic conversions
    print(f"0°C = {celsius_to_fahrenheit(0)}°F (should be 32)")
    print(f"32°F = {fahrenheit_to_celsius(32)}°C (should be 0)")
    print(f"0°C = {celsius_to_kelvin(0)}K (should be 273.15)")
    print(f"273.15K = {kelvin_to_celsius(273.15)}°C (should be 0)")
    
    # Test edge cases
    print(f"-40°C = {celsius_to_fahrenheit(-40)}°F (should be -40)")
    print(f"100°C = {celsius_to_fahrenheit(100)}°F (should be 212)")
    
    # Test temperature info
    print(f"\nTemperature info for 0°C: {temperature_info(0, 'C')}")
    print(f"Temperature info for 100°C: {temperature_info(100, 'C')}")
    print(f"Temperature info for 98.6°F: {temperature_info(98.6, 'F')}")
    print(f"Temperature info for 300K: {temperature_info(300, 'K')}")
    
    # Test interactive converter
    print("\n" + "="*50)
    temperature_converter_menu()
