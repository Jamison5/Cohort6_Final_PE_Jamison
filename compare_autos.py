import math

def area_circle(diameter: float, count=1) -> float:

    radius = diameter / 2
    return count * math.pi * radius ** 2

def area_equelateral_triangle(side: float) -> float:

    return (math.sqrt(3) / 4) * side ** 2 

def area_square(side: float) -> float:

    return side ** 2

def efficiency(area: float, dough_units: float) -> float:

    return area / dough_units

def main():

    auto1_area = area_circle(15, 2)
    auto1_efficiency = efficiency(auto1_area, 20)

    auto2_area = area_equelateral_triangle(20)
    auto2_efficiency = efficiency(auto2_area, 20)

    auto3_area = area_square(18)
    auto3_efficiency = efficiency(auto3_area, 18)

    print(f"Automatron 1 Efficiency: {auto1_efficiency:.2f} sq.in/unit")
    print(f"Automatron 2 Efficiency: {auto2_efficiency:.2f} sq.in/unit")
    print(f"Automatron 3 Efficiency: {auto3_efficiency:.2f} sq.in/unit")

    efficiencies = {
        "Automatron 1" : auto1_efficiency,
        "Automatron 2" : auto2_efficiency,
        "Automatron 3" : auto3_efficiency
    }

    best = max(efficiencies, key=efficiencies.get)

    print(f'The most efficient is {best}.')

if __name__ == '__main__':

    main()
