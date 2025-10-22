# Distance Unit Converter

import argparse

# Define the conversion constant
# 1 mile is approximately 1.60934 kilometers
MILES_TO_KM_RATE = 1.60934

def miles_to_kilometers(miles: float) -> float:
    """Converts a value in miles to kilometers."""
    return miles * MILES_TO_KM_RATE

def kilometers_to_miles(kilometers: float) -> float:
    """Converts a value in kilometers to miles."""
    return kilometers / MILES_TO_KM_RATE

def main():
    """Main function to handle command-line interaction."""
    
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="A utility for converting distance between miles (mi) and kilometers (km)."
    )
    
    # Define mutually exclusive arguments for the conversion type
    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument(
        '--mi-to-km', 
        type=float, 
        help="Value in miles to convert to kilometers."
    )
    
    group.add_argument(
        '--km-to-mi', 
        type=float, 
        help="Value in kilometers to convert to miles."
    )

    args = parser.parse_args()

    try:
        if args.mi_to_km is not None:
            miles = args.mi_to_km
            km = miles_to_kilometers(miles)
            print(f"{miles:.2f} miles is equal to {km:.2f} kilometers.")
            
        elif args.km_to_mi is not None:
            km = args.km_to_mi
            miles = kilometers_to_miles(km)
            print(f"{km:.2f} kilometers is equal to {miles:.2f} miles.")
            
    except ValueError:
        print("Error: Please ensure the input value is a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

# Example usage from command line (assuming saved as distance_converter.py):
# python distance_converter.py --mi-to-km 10
# python distance_converter.py --km-to-mi 100
