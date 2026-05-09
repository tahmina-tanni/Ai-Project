def get_questions_list():
    return [
        "What is your name?", "How old are you?", "What is your weight (kg)?",
        "What is your height (cm)?", "What is your resting heart rate (BPM)?",
        "How many hours do you sleep?", "How many liters of water do you drink daily?",
        "Do you smoke? (yes/no)", "Do you exercise daily? (yes/no)",
        "Do you have a family history of diabetes?", "Do you often feel stressed?",
        "Do you consume caffeine daily?", "Do you have any known allergies?",
        "What is your primary diet? (Veg/Non-Veg/Vegan)", "Any current medications?",
        "Do you experience frequent headaches?", "How is your energy level? (High/Low)",
        "Do you have chronic back pain?", "Do you sit for more than 6 hours a day?",
        "Any specific symptoms you want to report?"
    ]

def generate_final_analysis(responses):
    # Logic to summarize the 20 answers
    name = responses[0]
    weight = float(responses[2])
    height = float(responses[3]) / 100
    bmi = round(weight / (height**2), 2)
    
    report = f"📋 FULL HEALTH AUDIT: {name}\n"
    report += f"-----------------------------------\n"
    report += f"• BMI: {bmi}\n"
    report += f"• Activity Level: {'Active' if 'yes' in responses[8].lower() else 'Sedentary'}\n"
    report += f"• Hydration: {'Good' if float(responses[6]) >= 2 else 'Low'}\n"
    report += f"• Sleep: {responses[5]} hours\n"
    report += f"-----------------------------------\n"
    report += "Advice: Focus on consistent hydration and posture."
    return report