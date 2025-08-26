def macro_calculator(weight, height, age, gender, activity_level, goal="maintain"):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Dictionary of activity multipliers
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725
    }

    #  Fix: lowercase input
    activity_level = activity_level.lower()
    tdee = bmr * activity_multipliers.get(activity_level, 1.2)

    if goal == "cut":
        tdee -= 300
    elif goal == "bulk":
        tdee += 300

    protein = (0.3 * tdee) / 4
    carbs   = (0.4 * tdee) / 4
    fats    = (0.3 * tdee) / 9

    return {
        "Calories": round(tdee),
        "Protein (g)": round(protein),
        "Carbs (g)": round(carbs),
        "Fats (g)": round(fats)
    }

# Example:
print(macro_calculator(70, 175, 20, "Male", "Moderate", "maintain"))
