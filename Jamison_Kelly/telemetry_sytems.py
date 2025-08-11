def telemetry() -> float:

    print("1. Miles above Mars")
    print("2. Kilometers above Mars")
    choice = input("Please select either option 1, or option 2: \n").lower()

    if choice == '1' or choice == 'miles above mars':

        yards_per_mile = 1760
        feet_per_mile = 5280
        inches_per_mile = 63360

        miles = int(
            input('Please enter the number of miles you are above mars: \n')
            ) 
        
        print(

            f'There are {miles * yards_per_mile} yards, {miles * feet_per_mile} feet, and {miles * inches_per_mile} inches in {miles} miles.'
            
            )
        
    elif choice == '2' or choice == 'kilometers above mars':

        meters_per_km = 1000
        cm_per_km = 100_000
        mm_per_km = 1_000_000

        kilometers = int(
            input('Please enter the number of kilometers you are above mars: \n')
        )
        
        print(

            f'There are {kilometers * meters_per_km} meters, {kilometers * cm_per_km} centimeters, and {kilometers * mm_per_km} millimeters in {kilometers} kilometers.'
            
            )
        
    else:

        print('Please make a valid selection.')

if __name__ == '__main__':

    telemetry()