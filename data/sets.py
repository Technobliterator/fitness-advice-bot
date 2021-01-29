import data.exercises as exercises
from dataclasses import dataclass

@dataclass
class Set:
    def __init__(self, name: str, desc: str, exercises: list):
        self.name = name
        self.desc = desc
        self.exercises = exercises

bicep_exercises = Set(
    name = 'Bicep exercises',
    desc = 'Upper-body "pull" exercises.',
    exercises = [exercises.hammer_curl, exercises.concentration_curl]
)

tricep_exercises = Set(
    name = 'Tricep exercises',
    desc = 'Upper-body "push" exercises.',
    exercises = [exercises.bench_press, exercises.shoulder_press]
)

leg_exercises = Set(
    name = 'Leg exercises',
    desc = 'Lower-body exercises focused on leg resistance training.',
    exercises = [exercises.squat, exercises.leg_press]
)

sets = [bicep_exercises, tricep_exercises, leg_exercises]