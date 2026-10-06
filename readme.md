# CLI Expense Tracker

A simple command-line Expense Tracker built with Python.

This project was created as a practical Python project to apply core programming concepts including **OOP, dataclasses, enums, JSON file handling, exception handling, input validation, modules, and CRUD-style operations**.

## Features

- Add new expenses
- View all expenses
- Search expenses by category
- Search expenses by description
- View category-wise spending summary
- Delete an expense by ID
- Clear all expenses
- Automatic expense ID generation
- Persistent storage using JSON
- Input validation and error handling
- Handles missing or invalid JSON files

## Project Structure

```text
                    ┌──────────────┐
                    │   main.py    │
                    │     CLI      │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ services.py  │
                    │   Business   │
                    │    Logic     │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  storage.py  │
                    │ JSON Storage │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │expenses.json │
                    └──────────────┘
```

## Menu

When the application starts:

```text
1. Add Expense
2. View Expenses
3. Search by Category
4. Search by Description
5. View the Category Summary
6. Delete Expense
7. Clear Expenses
8. Exit
```

## Error Handling

The application handles common user and storage errors, including:

- Empty input
- Invalid integer input
- Invalid amount input
- Zero or negative amounts
- Invalid expense IDs
- Attempting to delete from an empty list
- Missing `expenses.json`
- Invalid/corrupted JSON data

## Python Concepts Used

This project demonstrates:

- Variables and data types
- Conditions and loops
- Functions
- Lists and dictionaries
- List comprehensions
- Modules and imports
- Dataclasses
- Object-oriented programming
- Dunder methods
- Type hints
- File handling
- JSON serialization/deserialization
- Exception handling
- Input validation
- Persistent data storage

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/KVC7121/CLI_Expense_tracker.git
cd CLI_Expense_tracker
```

### 2. Navigate to the project

```bash
cd expense_tracker
```

### 3. Run the application

```bash
python main.py
```

## Data Persistence

Expenses are stored locally in:

```text
data/expenses.json
```

The application loads existing expenses when it starts and saves changes whenever an expense is added, deleted, or cleared.

The actual `expenses.json` file should be excluded from Git because it contains personal expense data.

## Future Improvements

Possible future enhancements:

- Monthly spending reports
- Date-based filtering
- Edit an existing expense
- Export expenses to CSV
- Budget tracking
- SQLite database instead of JSON
- Unit tests with `pytest`
- More advanced CLI argument support

---
