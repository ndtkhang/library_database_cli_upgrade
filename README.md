# Python-Library-Database-CLI-Application
A Command-Line Interface (CLI) project built in Python to manage library books. This project was created to complete the final program for the MVC3 Python Development project competition. While developing, I practiced and deepened my skills with pandas, object-oriented programming (OOP), working with CSV files, and using SQLAlchemy for database interactions.

# Project Purpose
This application was built as part of completing the MVC3 Python Development project competition. It demonstrates various Python best practices and skills in:

pandas for data manipulation
OOP for code organization
CSV reading/writing
SQLAlchemy for ORM-based database interactions

## Features
Add, Import, Export Books

Manually add book entries through the CLI.
Import book data from CSV files.
Export data to CSV for backup or sharing.
SQLite Database Integration

Store and retrieve records using SQLite.
Easily export the library data to an SQLite database with SQLAlchemy.
pandas for Data Handling

Convert lists of books into pandas DataFrames for easy manipulation and CSV export.

## Installation
1. Clone the repository: git clone https://github.com/YourUsername/Python-Library-Database-CLI-Application.git
2. Navigate into the project folder: cd Python-Library-Database-CLI-Application
3. Create and activate a virtual environment (optional but recommended): python -m venv venv
4. 
* (Windows) venv\Scripts\activate

* (macOS/Linux) source venv/bin/activate

## Install requirements:
pip install -r requirements.txt

## Usage
1. Run the main script: python main.py
2. Follow CLI prompts to:
* Import books manually
* Import from CSV
* Export to CSV
* Export to SQLite database