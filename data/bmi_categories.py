from dataclasses import dataclass

@dataclass
class BMICategory:
    def __init__(self, name: str, min_bmi: int, max_bmi: int, resistance_multiplier: int):  
        self.name = name  
        self.min_bmi = min_bmi
        self.max_bmi = max_bmi
        self.resistance_multiplier = resistance_multiplier

    def isCategory(self, bmi):
        if bmi >= self.min_bmi and bmi < self.max_bmi:
            return True
        else:
            return False

underweight = BMICategory(
        name = 'underweight',
        min_bmi = 0,
        max_bmi = 18.4,
        resistance_multiplier = 0.5
)

normal = BMICategory(
    name = 'normal weight',
    min_bmi = 18.5,
    max_bmi = 24.9,
    resistance_multiplier = 1.5
)

overweight = BMICategory(
    name = 'overweight',
    min_bmi = 25.0,
    max_bmi = 29.9,
    resistance_multiplier = 1
)

obese = BMICategory(
    name = 'obese',
    min_bmi = 30,
    max_bmi = 100,
    resistance_multiplier = 1
)

categories = [underweight, normal, overweight, obese]