# Command-Line To-Do List Application

This is a simple command-line to-do list application written in Python. It allows users to manage tasks with features such as adding, removing, marking tasks as completed, setting priorities, and due dates. Tasks are persisted across sessions using a JSON file.

## Features

- **Task Management**: Add, remove, and mark tasks as completed.
- **Task Priority**: Set task priority levels (high, medium, low).
- **Due Dates**: Set due dates for tasks.
- **List View**: Display tasks in a list with their details.
- **Data Persistence**: Store tasks in a JSON file for persistence across sessions.

## Tech Stack

- **Python**
- **File Handling**: JSON for data persistence

## File Structure

The application is divided into multiple files for better modularity:

- `task_manager.py`: Contains functions for task management (add, remove, complete, list tasks).
- `file_handler.py`: Contains functions for loading and saving tasks to a JSON file.
- `todo.py`: Main application logic with a command-line interface.

## Installation

1. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).
2. Clone this repository or download the source code files.

## Usage

1. Navigate to the directory where the source code files are located.
2. Run the application using the following command:
   ```bash
   python todo.py
   ```

### Instructions to Run the Application

1. **Ensure you have Python installed**: You can check this by running `python --version` in your terminal. If not installed, download and install Python from [python.org](https://www.python.org/).

2. **Create the Files**: Create the following files with the provided code:

   - `task_manager.py`
   - `file_handler.py`
   - `todo.py`

3. **Run the Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the files are located.
   - Execute the application by running:
     ```bash
     python todo.py
     ```

Follow the on-screen prompts to interact with the to-do list application.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality of the Personal Budget Tracker.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
