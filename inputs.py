import data.sets as sets
import data.goals as goals

def input_height():
    height_feet = 0
    height_inches = 0

    print('Enter your height (in feet and inches): ')
    while True:
        try:
            height_feet = int(input('Feet: '))
            if height_feet > 0:
                height_inches = int(input('Inches: '))
                if height_inches > 0:
                    print(('Your height is listed as {} foot {} inches.').format(height_feet, height_inches))
                    confirm = input('Is this correct? Y/N ')
                    if confirm.lower() == 'y' or confirm.lower() == 'yes':
                        print('Height entered.')
                        break
                    else:
                        print('Trying again.')
            else:
                print('Invalid input; try again')
        except Exception as e:
            print(e)

    return int(height_feet), int(height_inches)

def input_weight():
    weight = 0

    print('Enter your weight in pounds (lbs): ')
    while True:
        try:
            weight = int(input('Weight (lbs): '))
            if weight > 0:
                print(('Your weight is listed as {} lbs.').format(weight))
                confirm = input('Is this correct? Y/N ')
                if confirm.lower() == 'y' or confirm.lower() == 'yes':
                    print('Weight entered.')
                    break
                else:
                    print('Trying again.')
            else:
                print('Invalid input; try again')
        except Exception as e:
            print(e)
    
    return int(weight)

def input_exercise_type():
    exercise_type = 0
    print('Sets include:')
    for i in range(len(sets.sets)):
        print(('[{}] FOR: {}. Description: {}.').format(i, sets.sets[i].name, sets.sets[i].desc))

    while True:
        try:
            exercise_type = sets.sets[int(input('Select the chosen exercise type set (choose the number of the set above): '))]
            if exercise_type in sets.sets:
                print(('You have chosen {}.').format(exercise_type.name))
                confirm = input('Is this correct? Y/N ')
                if confirm.lower() == 'y' or confirm.lower() == 'yes':
                    print('Set chosen entered.')
                    break
                else:
                    print('Trying again.')
            else:
                print('Invalid input; try again')
        except Exception as e:
            print(e)

    return exercise_type

def input_goal():
    goal = 0
    print('Goals include:')
    for i in range(len(goals.goals)):
        print(('[{}] FOR: {}. Description: {}.').format(i, goals.goals[i].name, goals.goals[i].desc))

    while True:
        try:
            goal = goals.goals[int(input('Select the chosen goal (choose the number of the set above): '))]
            if goal in goals.goals:
                print(('You have chosen {}.').format(goal.name))
                confirm = input('Is this correct? Y/N ')
                if confirm.lower() == 'y' or confirm.lower() == 'yes':
                    print('Goal entered.')
                    break
                else:
                    print('Trying again.')
            else:
                print('Invalid input; try again')
        except Exception as e:
            print(e)

    return goal

'''
def input_gender():
    gender = ''
    while True:
        try:
            gender = str(input('Enter your gender (M/F): '))
            if gender.lower() == 'm' or gender.lower() == 'male':
                gender = 'male'
                break
            elif gender.lower() == 'f' or gender.lower() == 'female':
                gender = 'female'
                break
            else:
                print('Invalid gender')
        except Exception as e:
            print(e)
    return gender
'''