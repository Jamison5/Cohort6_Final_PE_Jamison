import math

def required_fule(mass:float) -> float:

    fuel = (mass / 3) - 2
    return fuel

def calc_total():

    file_path = '/home/jamison-kelly/python-basics-class/Cohort6_Final_PE_Jamison/Jamison_Kelly/input.txt'
    total_fuel = 0 

    with open(file_path, 'r') as file:
        for line in file:
            mass = float(line.strip())
            total_fuel += required_fule(mass)

    print(f'Required fuel: {round(total_fuel, 2)}')


if __name__ == '__main__':

   calc_total()
