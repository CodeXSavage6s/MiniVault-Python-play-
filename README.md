# MiniVault 🔐

**My First Python Project — A Simple CLI Note Manager**

MiniVault is a command-line note management application built with Python. It allows users to create, view, edit, and delete notes directly from their terminal, with data stored locally in a JSON file.

This is my first Python project, built as part of my journey into Python programming, backend development, and software engineering.

The goal was to move beyond learning Python syntax and put those concepts into practice by building a functional application from scratch.

## ✨ Features

- **Create Notes:** Add new notes with unique IDs.
- **View Notes:** Display all saved notes alongside their IDs.
- **Edit Notes:** Modify the content of existing notes.
- **Delete Notes:** Remove notes that are no longer needed.
- **Persistent Storage:** Notes are saved locally in a JSON file, so they remain available after closing the application.
- **Input Validation:** Handles empty inputs and invalid menu selections.
- **Error Handling:** Includes basic handling for missing or invalid JSON data.

## 🛠️ Technologies Used

- **Python 3** – Core programming language.
- **JSON** – Used for storing and retrieving notes.
- **UUID** – Generates unique identifiers for individual notes.
- **OS module** – Checks whether the notes file exists.
- **Standard Library** – Uses Python's built-in modules without requiring external dependencies.

## 📂 Project Structure

```text
MiniVault/
├── main.py          # Main application logic
├── .gitignore       # Files excluded from Git
└── README.md        # Project documentation
```

`notes.json` is generated automatically when notes are saved. It is excluded from version control to avoid uploading personal note data.

## 🚀 Getting Started

### Prerequisites

- Python 3 installed on your system.
- A terminal or command-line environment.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/CodeXSavage6s/MiniVault-Python-play-.git MiniVault
```

2. Navigate into the project directory:

```bash
cd MiniVault
```

3. Run the application:

```bash
python3 main.py
```

No external packages are required.

## 💻 Usage

After starting the application, you'll be presented with a menu:

```text
=== MiniVault ===
1. Add note
2. List notes
3. Delete note
4. Edit note
5. Exit

Choose an option:
```

Select an option by entering its corresponding number.

### Example

To create a note:

```text
Choose an option: 1

Enter your note: Learning Python is a journey.

Note saved successfully!
```

To view saved notes, select the list option. Each note is displayed with its unique ID and content.

You can also edit or delete individual notes through their displayed list positions.

## 🧠 What I Learned

Building MiniVault helped me move from understanding Python syntax to applying it in a practical project.

Some of the concepts I worked with include:

- **Functions:** Breaking the application into smaller, reusable operations.
- **File Handling:** Reading from and writing to files using Python's `open()`.
- **JSON Serialization:** Using `json.load()` and `json.dump()` to persist application data.
- **Data Structures:** Working with lists and dictionaries to organize notes.
- **UUID:** Generating unique identifiers for records.
- **Exception Handling:** Handling errors such as invalid JSON data.
- **Input Validation:** Checking user input before performing operations.
- **Control Flow:** Using loops and conditional statements to manage the application menu.
- **CRUD Operations:** Implementing Create, Read, Update, and Delete functionality.

## 🔮 Future Improvements

MiniVault is a learning project, and there are several ways I would like to improve it:

- Add search functionality.
- Introduce note categories or tags.
- Add timestamps for note creation and modification.
- Improve data validation and error handling.
- Replace JSON storage with SQLite or PostgreSQL.
- Eventually explore converting the application into a REST API using FastAPI.

## 🎯 Project Purpose

MiniVault is not intended to be a fully featured note-taking product. It is a practical learning project created to strengthen my Python fundamentals and develop my problem-solving skills.

It represents my first step toward becoming more comfortable building software independently.

More projects and improvements will follow as I continue learning.

---

**Built with Python 🐍**

*One project at a time. One concept at a time.*

