"""
MY AI STUDY PLANNER
A beginner-friendly, terminal-based study planner made with basic Python only.

No APIs, GUI frameworks, databases, or third-party packages are used.
Run with: python main.py
"""

from datetime import date


PINK = "=" * 48


def ask_non_empty(prompt):
    """Ask until the student enters something other than a blank response."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Oopsie! Please enter something so we can continue. 💗")


def ask_int(prompt, minimum, maximum):
    """Ask for a whole number within a safe range."""
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"Please enter a number from {minimum} to {maximum}.")
        except ValueError:
            print("Numbers only, please! Try again ✨")


def ask_float(prompt, minimum, maximum):
    """Ask for a number that may include decimals."""
    while True:
        try:
            value = float(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"Please enter a number from {minimum} to {maximum}.")
        except ValueError:
            print("Please enter a valid number, like 1 or 1.5.")


def make_weekly_plan(subjects, study_days, daily_hours):
    """Create a simple plan using the student's subjects and available time."""
    plan = []
    subject_count = len(subjects)

    for day_number in range(1, study_days + 1):
        subject = subjects[(day_number - 1) % subject_count]
        next_subject = subjects[day_number % subject_count] if subject_count > 1 else subject
        plan.append(
            f"Day {day_number}: {subject} ({daily_hours:g} hour(s))\n"
            f"  • {daily_hours * 0.6:g} hour(s): learn/revise {subject}\n"
            f"  • {daily_hours * 0.3:g} hour(s): practice questions for {subject}\n"
            f"  • {daily_hours * 0.1:g} hour(s): quick recap + plan next steps\n"
            f"  • If you have extra energy: preview {next_subject}."
        )
    return plan


def main():
    print("\n" + "♡" + PINK)
    print("          MY AI STUDY PLANNER")
    print("       your soft-life study era starts here")
    print(PINK + "♡")
    print("A tiny note: this beginner project uses rule-based Python")
    print("to make a personalized plan. It does not use an AI API.\n")

    student_name = ask_non_empty("What's your name, study star? ")
    age = ask_int("How old are you? ", 5, 100)
    school_level = ask_non_empty("Your class/grade or study level: ")
    subjects_text = ask_non_empty("Subjects (separate them with commas): ")
    subjects = [subject.strip() for subject in subjects_text.split(",") if subject.strip()]
    while not subjects:
        subjects_text = ask_non_empty("Please enter at least one subject: ")
        subjects = [subject.strip() for subject in subjects_text.split(",") if subject.strip()]

    study_days = ask_int("Your goal: study days per week (1-7): ", 1, 7)
    daily_hours = ask_float("Your goal: study hours per study day (0.5-12): ", 0.5, 12)
    completed_hours = ask_float(
        "How many hours have you already studied this week? (0-84): ", 0, 84
    )

    weekly_goal = study_days * daily_hours
    progress = min((completed_hours / weekly_goal) * 100, 100) if weekly_goal else 0
    remaining_hours = max(weekly_goal - completed_hours, 0)
    plan = make_weekly_plan(subjects, study_days, daily_hours)

    if progress >= 100:
        progress_message = "Goal reached! Icon behaviour. Celebrate your effort 🎀"
    elif progress >= 60:
        progress_message = "You're getting there! Keep your rhythm gentle and steady."
    elif progress >= 25:
        progress_message = "A lovely start. Small sessions still count."
    else:
        progress_message = "Fresh-start energy: choose one small task and begin."

    output_lines = [
        "♡" + PINK,
        "          MY AI STUDY PLANNER",
        "           PERSONAL STUDY PLAN",
        PINK + "♡",
        f"Created: {date.today().isoformat()}",
        "",
        f"Student: {student_name}",
        f"Age: {age}",
        f"Study level: {school_level}",
        f"Subjects: {', '.join(subjects)}",
        "",
        "YOUR WEEKLY GOALS",
        "-" * 28,
        f"Study days per week: {study_days}",
        f"Hours per study day: {daily_hours:g}",
        f"Weekly study target: {weekly_goal:g} hours",
        "",
        "YOUR PROGRESS",
        "-" * 28,
        f"Hours already studied: {completed_hours:g}",
        f"Hours remaining to target: {remaining_hours:g}",
        f"Progress: {progress:.1f}%",
        f"Progress bar: [{'#' * int(progress // 5)}{'.' * (20 - int(progress // 5))}]",
        progress_message,
        "",
        "YOUR PERSONALIZED WEEKLY PLAN",
        "-" * 28,
    ]

    for day in plan:
        output_lines.extend([day, ""])

    output_lines.extend([
        "GENTLE STUDY TIPS",
        "-" * 28,
        "• Try a 25-minute focus session followed by a 5-minute break.",
        "• Keep your phone away during focus time if it distracts you.",
        "• Start with the subject that needs the most attention.",
        "• Leave room for meals, sleep, rest, and fun. You are a person, not a machine.",
        "• Update your completed study hours next time to refresh your progress.",
        "",
        "Made with basic Python, pinkiee vibes, creamy calm, and a little black.",
        "Note: 'AI' is the project theme; this version uses simple Python rules,",
        "not a real AI model or online service.",
        PINK,
    ])

    report = "\n".join(output_lines)
    print("\n" + report)

    try:
        with open("study_plan.txt", "w", encoding="utf-8") as file:
            file.write(report)
        print("\n✨ Saved successfully as study_plan.txt in the current folder.")
    except OSError as error:
        print(f"\nCould not save the plan: {error}")
        print("Try running the program from a folder where you can save files.")


if __name__ == "__main__":
    main()
