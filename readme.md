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
expense_tracker/
│
├── data/
│   ├── expenses.json
│   └── expenses.example.json
│
├── main.py
├── models.py
├── services.py
├── storage.py
├── .gitignore
└── README.md
```

### `main.py`

Handles the command-line interface and menu.

```text
User
 ↓
main.py
 ↓
services.py
```

### `models.py`

Contains the `Expense` dataclass.

```python
@dataclass
class Expense:
    id: int
    amount: float
    category: str
    description: str
    date: str
```

### `services.py`

Contains the application's business logic:

- Adding expenses
- Viewing expenses
- Deleting expenses
- Searching
- Category summaries
- Input validation
- Clearing expenses

### `storage.py`

Handles persistent storage.

```text
JSON file → Python Expense objects
Python Expense objects → JSON file
```

## Data Flow

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

## Example

Adding an expense:

```text
Enter the details of the expense

Amount: 300
Category: Food
Description: Lunch
Date: 10-05-2026

A new expense data is added successfully!
```

Viewing expenses:

```text
ID: 1
Amount: ₹300.0
Category: Food
Description: Lunch
Date: 10-05-2026
```

Category summary:

```text
Summary of expenses by category

Food --> ₹1200.0
Travel --> ₹800.0
Shopping --> ₹2500.0
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
- Dunder methods (`__str__`)
- Type hints
- File handling
- JSON serialization/deserialization
- Exception handling
- Input validation
- Persistent data storage

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
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
