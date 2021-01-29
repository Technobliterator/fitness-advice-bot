from dataclasses import dataclass

@dataclass
class Goal:
    def __init__(self, name: str, desc: str, number_of_sets: int, reps: int, rest: str, resistance_multiplier: int):
        self.name = name
        self.desc = desc
        self.number_of_sets = number_of_sets
        self.reps = reps
        self.rest = rest
        self.resistance_multiplier = resistance_multiplier

endurance = Goal(
    name = 'Endurance',
    desc = 'Focused on muscle stamina (i.e. for marathons)',
    number_of_sets = 2,
    reps = 15,
    rest = '30 seconds',
    resistance_multiplier = 1
)

hypertrophy = Goal(
    name = 'Hypertrophy',
    desc = 'Focused on building muscle mass (i.e. bodybuilding)',
    number_of_sets = 4,
    reps = 8,
    rest = '1 minute',
    resistance_multiplier = 1.5
)

strength = Goal(
    name = 'Strength',
    desc = 'Focused on strengthening muscles (i.e. ability to lift weights)',
    number_of_sets = 2,
    reps = 6,
    rest = '2 minutes',
    resistance_multiplier = 3
)

power = Goal(
    name = 'Power',
    desc = 'Focused on strengthening + speed for muscles (i.e. amount of work in short time)',
    number_of_sets = 3,
    reps = 6,
    rest = '3 minutes',
    resistance_multiplier = 2
)

goals = [endurance, hypertrophy, strength, power]