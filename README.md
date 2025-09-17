# Android-Club
# ✅ Task List App

---

## 📸 Screenshots

### 🏠 Home Page  
![Home Page](screenshots/Task_App home page.png)

### ➕ Adding a Task  
![Adding Task](screenshots/Adding task.png)

### ✅ Task Added  
![Task Added](screenshots/Task Added.png)

### 🎯 Task Completed (Green Title)  
![Task Completed](screenshots/Task completion (Green Title).png)

### ⚠️ Error (No Title Entered)  
![No Title Error](screenshots/NoTitle Error.png)

---

## 📡 API Endpoints

Although this project is built with **Streamlit** (UI-focused), the following logical endpoints describe the main actions of the Task App:

### 1. Add a Task
- **Description:** Adds a new task with a title and description.  
- **Input:**  
  - `title` (string, required)  
  - `description` (string, optional)  
- **Response:**  
  - Success message if task is added.  
  - Error if `title` is missing.

### 2. View Tasks
- **Description:** Displays the list of all tasks.  
- **Response:**  
  - JSON-like list of tasks shown in the UI with title & description.

### 3. Complete a Task
- **Description:** Marks a task as completed.  
- **Response:**  
  - Updates the UI → Completed tasks appear with a **green title**.

### 4. Delete a Task
- **Description:** Removes a selected task from the list.  
- **Response:**  
  - Task disappears from the list.  
  - Success message is shown.
