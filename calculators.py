import data.bmi_categories as bmi_categories

def bmi_calculator(height_feet, height_inches, weight):
    #BMI formula = (Weight in Pounds / (Height in inches x Height in inches)) x 703

    formula_height = (height_feet * 12) + height_inches

    bmi = round(((weight / (formula_height**2)) * 703), 1)

    return float(bmi)

def health_calculator(bmi):
    for i in bmi_categories.categories:
        if i.isCategory(bmi):
            return i
    return False