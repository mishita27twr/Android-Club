# Android-Club  
# 🌐 Android Club Website

This is a **Streamlit-based website** built for the **Android Club VIT Bhopal**.  
It highlights the club’s vision, activities, projects, and events in a modern, styled UI.  

---

## ⚙️ Setup Instructions

Follow the steps below to run this project on your local machine:

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Android-Club.git
   cd Android-Club/club_website

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run club_website.py

# 5.Open your browser and navigate to:
http://localhost:8501

## 📸 Screenshots

### Club Website Page
![Home Page](https://github.com/mishita27twr/Android-Club/raw/main/club_home.png)

### About us page
![About us](https://github.com/mishita27twr/Android-Club/raw/main/club_about.png)

#### Projects
![Projects Page](https://github.com/mishita27twr/Android-Club/raw/main/club_projects.png)

#### Events
![Events Page](https://github.com/mishita27twr/Android-Club/raw/main/club_events.png)
![Events Page](https://github.com/mishita27twr/Android-Club/raw/main/club_events1.png)

### Contact Page
![Contact Page](https://github.com/mishita27twr/Android-Club/raw/main/club_contact.png)


# 🛠️ Tech Stack
Python 3
Streamlit
Pillow (PIL)

# 📂 Project Structure
club_website/
│── club_website.py       # Main app file
│── images/               # Logos & images
│── screenshots/          # App screenshots
│── requirements.txt      # Dependencies
│── README.md             # Documentation



# ✅ Task List App  

---

## 📷 Screenshots  

### 🏠 Home Page  
![Task App Home Page](https://github.com/mishita27twr/Android-Club/raw/main/Task_App%20home%20page.png)

### ➕ Adding a Task  
![Adding Task](https://github.com/mishita27twr/Android-Club/raw/main/Adding%20task.png)  

### ✅ Task Added  
![Task Added](https://github.com/mishita27twr/Android-Club/raw/main/Task%20Added.png)  

### 🎯 Task Completed (Green Title)  
![Task Completed](https://github.com/mishita27twr/Android-Club/raw/main/Task%20completion%20(Green%20Ttitle).png)

### ⚠️ Error (No Title Entered)  
![No Title Error](https://github.com/mishita27twr/Android-Club/raw/main/NoTitle%20Error.png)  


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

# 🛠️ Tech Stack (Task App)
Python 3
Streamlit → for building the web interface
Pillow (PIL) → for handling the logo/image

# 📂 Project Structure (Task App)
task_app/
│── Task_List_App.py        # Main Streamlit app
│── images/                 # Logo & image assets
│   └── android_club_vit_bhopal_logo.jpeg
│── screenshots/            # Screenshots of app functionality
│   ├── Task_App_home_page.png
│   ├── Adding_task.png
│   ├── Task_Added.png
│   ├── Task_completion_Green_Title.png
│   └── NoTitle_Error.png
│── README.md               # Documentation with setup, API, and screenshots
│── requirements.txt        # Python dependencies (streamlit, pillow)
