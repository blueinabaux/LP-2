# Expert System for Library Book Recommendation

def recommend_book(department, topic, year):
    # Normalize inputs
    department = department.lower()
    topic = topic.lower()
    year = year.lower()

    # Knowledge Base (rule-based)
    if department == "cs" and topic == "ai":
        if year in ["final", "third"]:
            return "Recommended Book: 'Artificial Intelligence: A Modern Approach' by Russell and Norvig"
        else:
            return "Recommended Book: 'Introduction to AI' by Wolfgang Ertel"

    elif department == "cs" and topic == "networks":
        return "Recommended Book: 'Computer Networking' by Kurose and Ross"

    elif department == "ece" and topic == "iot":
        return "Recommended Book: 'Internet of Things: A Hands-On Approach' by Arshdeep Bahga"

    elif department == "ece" and topic == "robotics":
        return "Recommended Book: 'Introduction to Robotics' by Craig"

    elif department == "mech" and topic == "cad":
        return "Recommended Book: 'Mastering CAD/CAM' by Ibrahim Zeid"

    else:
        return "No specific book found for the given input. Please consult the librarian for help."


# Sample interaction
print("Welcome to the Library Expert System!")
dept = input("Enter your department (CS, ECE, MECH): ")
proj = input("Enter your project topic (AI, Networks, Robotics, IoT, CAD): ")
yr = input("Enter your year of study (Second, Third, Final): ")

recommendation = recommend_book(dept, proj, yr)
print("\n" + recommendation)
