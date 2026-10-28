# 🎀 MY AI Study Planner

A beginner-friendly, Gen Z-coded study planner built with **basic Python**. It has a pinkiee, creamy, gentle aesthetic with a little black, expressed through terminal styling and cute text.

> **Important:** This first version is a rule-based planner, not a real AI model. It uses no API, GUI, database, or external packages.

## Features

- Asks for a student's name, age, study level, subjects, weekly study days, and daily study hours.
- Asks how many hours the student has already studied this week.
- Calculates the weekly study target, remaining hours, and percentage progress.
- Creates a personalized weekly plan based on the subjects and available study time.
- Prints the plan in the terminal.
- Saves the full report as `study_plan.txt`.

## Requirements

- Python 3.8 or newer (no third-party packages needed).

## Run it

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some Windows installations, use:

   ```powershell
   py main.py
   ```

4. Answer the questions. Your plan will appear in the terminal and be saved to `study_plan.txt` in the current working folder.

## Project files

```text
my-ai-study-planner/
├── main.py
├── README.md
├── .gitignore
└── LICENSE
```

## How progress is calculated

```text
weekly target = study days per week × study hours per day
progress (%) = completed study hours ÷ weekly target × 100
```

The displayed progress is capped at 100%. The remaining target is never shown as a negative number.

## Customization ideas

- Add a preferred study time.
- Let students choose a break length.
- Add an end-of-week reflection.
- Save separate reports using a date in the filename.
- Later, add a GUI or a real AI service if the project requirements allow it.

## Publish on GitHub

1. Sign in to [GitHub](https://github.com/).
2. Create a **new public repository** named `my-ai-study-planner`. Do not initialize it with a README if you plan to push this folder as-is.
3. Open a terminal inside this project folder and run:

   ```bash
   git init
   git add .
   git commit -m "Build beginner-friendly study planner"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/my-ai-study-planner.git
   git push -u origin main
   ```

4. Replace `YOUR-USERNAME` with your GitHub username. GitHub may ask you to sign in through your browser or use its supported authentication flow.

If Git says `remote origin already exists`, use `git remote set-url origin https://github.com/YOUR-USERNAME/my-ai-study-planner.git` and then run the push command again.

## License

MIT — see `LICENSE`.
