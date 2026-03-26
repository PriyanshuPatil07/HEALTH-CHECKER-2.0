import pandas as pd
import numpy as np

symptoms = ["fever", "cough", "cold", "gas", "loose motion", "hypertension"]

severity_scores = [3, 2, 2, 1, 3, 4]

data = pd.DataFrame({
    "symptom": symptoms,
    "severity": severity_scores
})


def get_remedy(symptom):

    if symptom == "fever":
        return "Drink tulsi tea and take rest.", \
               "Reduces body weakness.", \
               "See doctor if fever stays more than 2 days."

    elif symptom == "cough":
        return "Take honey with ginger.", \
               "Soothes throat naturally.", \
               "Avoid cold drinks."

    elif symptom == "cold":
        return "Take steam and warm soup.", \
               "Clears blocked nose.", \
               "Stay away from cold air."

    elif symptom == "gas":
        return "Drink ajwain water.", \
               "Improves digestion.", \
               "Avoid spicy food."

    elif symptom == "loose motion":
        return "Drink ORS and eat banana.", \
               "Prevents dehydration.", \
               "Consult doctor if continues 1 day."

    elif symptom == "hypertension":
        return "Reduce salt and walk daily.", \
               "Helps control BP.", \
               "Check BP regularly."

    else:
        return None, None, None

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array(severity_scores)

model = np.polyfit(x, y, 1)
line = np.poly1d(model)

print("\nWelcome to Health Checker")
print("This program suggests simple home remedies.\n")


while True:

    print("Available symptoms:")

    for s in symptoms:
        print("-", s)

    user_input = input("\nEnter symptom name (or type exit): ").lower()

    if user_input == "exit":
        print("Stay healthy. Goodbye!")
        break


    if user_input in symptoms:

        index_value = symptoms.index(user_input) + 1

        predicted = round(line(index_value), 2)

        remedy, benefit, precaution = get_remedy(user_input)

        print("\nSuggested Remedy:", remedy)
        print("Benefit:", benefit)
        print("Precaution:", precaution)
        print("Severity Level:", predicted)

        if predicted >= 3:
            print("Advice: Please monitor your condition carefully.\n")
        else:
            print("Advice: Home remedy should help.\n")

    else:
        print("Symptom not found. Try again.\n")