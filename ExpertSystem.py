from datetime import datetime

def get_valid_input(prompt, valid_options):

    while True:
        response = input(prompt).strip().lower()

        if(response in valid_options):
            return response
        
        print("Invalid Input!")

def evaluate_performance(punctuality, task_completed, team_behaviour, initiative):

    score = 0
    reasons=[]


    if punctuality == "high":
        score += 30
        reasons.append("High Punctuality (+30)")
    elif punctuality == "medium":
        score += 20
        reasons.append("Medium Punctuality (+20)")
    else:
        score += 10
        reasons.append("Low Punctuality (+10)")

    

    if task_completed == "yes":
        score += 20
        reasons.append("Completed Task (+30)")
    else:
        reasons.append("Did not complete task (0)")



    if team_behaviour == "good":
        score += 20
        reasons.append("Good team behaviour (+20)")
    elif team_behaviour == "average":
        score += 10
        reasons.append("Average team behaviour (+10)")
    else:
        reasons.append("Poor team behaviour (0)")




    if initiative == "yes":
        score += 20
        reasons.append("Showed initiative (+20)")
    else:
        reasons.append("No initiative (0)")



    if score >= 80:
        grade = "Excellent"
    elif score >= 60:
        grade = "Good"
    elif score >= 40:
        grade = "Average"
    else:
        grade = "Poor"

    return grade, score, reasons




def evaluate_employee():

    print("\n--------------------------------\n")
    print(f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    name = input("Enter Employee name: ").strip().title()
    punctuality = get_valid_input("1. Punctuality ? (high / medium / low)", ["high", "medium", "low"])
    task_completed = get_valid_input("2. Task Completed ? (yes / no)", ["yes", "no"])
    team_behaviour = get_valid_input("3. Team Behaviour ? (good / average / poor)", ["good", "average", "poor"])
    initiative = get_valid_input("4. Initiative ? (yes / no)", ["yes", "no"])

    grade, score, reasons = evaluate_performance(punctuality, task_completed, team_behaviour, initiative)
    print("\n")

    print("Evaluation Result: ",name)
    print("Score: ", score)
    print("Grade: ", grade)
    print("--------------------------------\n")

    for r in reasons:
        print("- ", r)

    if grade == "Poor":
        print("\nRecommended Manager attention or consultancy")
    elif grade == "Excellent":
        print("\nOutstanding Performance!")




def main():
    print("Employee Performance Eveluation System\n")

    while True:

        print("1. Evaluate employee.")
        print("2. Exit.")
        choice = input("Enter your choice (1/2): ").strip()

        while True:
            if choice == '1':
                evaluate_employee()
            elif choice == '2':
                print("Exiting the System. Thank You!")
                break
            else:
                print("Invalid Choice!")

if __name__ == "__main__":
    main()

