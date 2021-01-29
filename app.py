#!/usr/bin/python3

import os
from flask import Flask
from flask import render_template, request

import calculators
import data.goals as goals
import data.sets as sets
import data.exercises as exercises

app = Flask(__name__)

@app.route('/')
def form():
    print(sets)
    return render_template('form.html', sets=sets.sets, sets_len=len(sets.sets), goals=goals.goals, goals_len=len(goals.goals))

@app.route('/', methods=["POST"])
def bmi_post():
    weight = request.form['weight']
    feet = request.form['feet']
    inches = request.form['inches']

    bmi = calculators.bmi_calculator(int(feet), int(inches), int(weight))
    health = calculators.health_calculator(bmi)

    goal = goals.goals[int(request.form['goal'])]
    set = sets.sets[int(request.form['set'])]

    output_set = []

    for i in set.exercises:
        resitance = i.default_weight * health.resistance_multiplier * goal.resistance_multiplier
        equipment = ('You will need the following equipment: {}').format(i.equipment)
        desc = ('You will be doing {} sets of {} reps at approx. {} lbs.').format(goal.number_of_sets, goal.reps, resitance)
        output_set.append({ 'name': i.name, 'equipment': equipment, 'desc': desc })

    print(output_set)

    return render_template('form.html', goals=goals.goals, goals_len=len(goals.goals), sets=sets.sets, sets_len=len(sets.sets), weight=weight, bmi=bmi, health=health.name, output_set=output_set)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

