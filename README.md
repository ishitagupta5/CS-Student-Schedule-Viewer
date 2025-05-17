# CS Student Schedule Viewer

This project is a Python-based utility for querying a **SQLite database of Computer Science students**. It allows users to filter students by **academic year** and display their information either in the **terminal** or as a **well-formatted HTML report**.

The tool is useful for course scheduling assistants, academic advisors, or students who want to inspect enrollment information programmatically.

---

## Project Overview

This repository includes:

- A database file: `cs_course_scheduling.sqlite` containing student information
- A terminal-based viewer: `list_studentsog.py`
- An HTML report generator: `list_students.py`
- A sample output HTML file: `students_academic_year_4.html`

---

## Database Schema (Assumed)

The `cs_course_scheduling.sqlite` database contains a table named `students` with at least the following columns:

| Column         | Type     | Description                   |
|----------------|----------|-------------------------------|
| `first_name`   | TEXT     | Student's first name          |
| `last_name`    | TEXT     | Student's last name           |
| `academic_year`| INTEGER  | Year of study (e.g., 1 to 4)  |

---

## How It Works

### 1. Argument Handling

Both scripts accept a single **command-line argument**: the desired academic year (e.g., `1`, `2`, `3`, or `4`).

```bash
python list_students.py 4
