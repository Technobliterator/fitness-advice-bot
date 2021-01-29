from dataclasses import dataclass

@dataclass
class Exercise:
    def __init__(self, name: str, equipment: list, alternative_equipment: list, muscle_groups: list, default_weight: int):
        self.name = name
        self.equipment = equipment
        self.alternative_equipment = alternative_equipment
        self.muscle_groups = muscle_groups
        self.default_weight = default_weight
        
hammer_curl = Exercise(
    name = 'Hammer curl',
    equipment = ['Dumbbell'],
    alternative_equipment = [],
    muscle_groups = ['Biceps', 'Back'],
    default_weight = 10
)

concentration_curl = Exercise(
    name = 'Concentration curl',
    equipment = ['Dumbbell', 'Bench'],
    alternative_equipment = [],
    muscle_groups = ['Biceps'],
    default_weight = 15
)

bench_press = Exercise(
    name = 'Bench press',
    equipment = ['Barbell', 'Bench'],
    alternative_equipment = ['Dumbbell'],
    muscle_groups = ['Triceps', 'Detloids', 'Shoulders'],
    default_weight = 40
)

shoulder_press = Exercise(
    name = 'Shoulder press',
    equipment = ['Dumbbell', 'Bench'],
    alternative_equipment = [],
    muscle_groups = ['Triceps', 'Shoulders'],
    default_weight = 15
)

squat = Exercise(
    name = 'Squats',
    equipment = ['Barbell'],
    alternative_equipment = ['Dumbbell'],
    muscle_groups = ['Legs'],
    default_weight = 40
)

leg_press = Exercise(
    name = 'Leg press',
    equipment = ['Leg press machine'],
    alternative_equipment = [],
    muscle_groups = ['Legs'],
    default_weight = 60
)

exercises = [hammer_curl, concentration_curl, bench_press, shoulder_press, squat, leg_press]