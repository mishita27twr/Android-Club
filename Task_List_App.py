import sqlite3
import streamlit as st

# ------------------ Backend ------------------
conn = sqlite3.connect("tasks.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    completed BOOLEAN
)
""")
conn.commit()

def get_tasks():
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    return [{"id": r[0], "title": r[1], "description": r[2], "completed": r[3]} for r in rows]

def add_task(title, description):
    c.execute("INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)", (title, description, False))
    conn.commit()

def toggle_task(id, completed):
    c.execute("UPDATE tasks SET completed=? WHERE id=?", (not completed, id))
    conn.commit()

def delete_task(id):
    c.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()


# ------------------ Frontend ------------------
st.set_page_config(page_title="Task List App", page_icon="📝", layout="centered")

# Initialize session state flag for refresh
if 'refresh' not in st.session_state:
    st.session_state.refresh = False

# ------------------ Custom CSS ------------------
st.markdown("""
<style>
.stApp { background-color: black; }
label { color: red !important; font-weight: bold; font-size: 18px; }
.stTextInput>div>div>input, .stTextArea textarea { background-color: black; color: white; border: 2px solid white; border-radius: 6px; transition:0.3s; }
.stTextInput>div>div>input:hover, .stTextArea textarea:hover { box-shadow: 0 0 8px white; }
.stButton>button { background-color: black; color: pink; border: 2px solid pink; border-radius: 8px; font-weight: bold; padding: 6px 20px; transition: 0.3s; }
.stButton>button:hover { background-color: black; color: pink; box-shadow:0px 0px 15px pink; }
.task-box { background-color: black; color:white; padding:15px; margin:8px 0; border:2px solid white; border-radius:10px; transition:0.3s; }
.task-box:hover { box-shadow:0px 0px 15px white; }

/* Proper Add Task button styling inside form */
form > div > div.stButton > button {
    background-color: black !important;
    color: pink !important;
    border: 2px solid pink !important;
    border-radius: 8px !important;
    font-weight: bold !important;
    padding: 6px 20px !important;
    transition: 0.3s !important;
}
form > div > div.stButton > button:hover {
    background-color: black !important;
    color: pink !important;
    box-shadow: 0px 0px 15px pink !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Header with Logo ------------------
import streamlit as st
from PIL import Image

# ------------------ Header with Logo ------------------
# Load the JPEG logo
logo = Image.open("android_club_vit_bhopal_logo.jpeg")

# Display logo and header text side by side
col1, col2 = st.columns([1, 4])
with col1:
    st.image(logo, width=80)  # Adjust width if needed
with col2:
    st.markdown(
        '<span style="color:#00FF00; font-size:60px; font-weight:bold; vertical-align:middle;">ANDROID CLUB</span>',
        unsafe_allow_html=True
    )

# ------------------ Add Task Heading ------------------
st.markdown('<div style="color:#00BFFF; font-size:30px; font-weight:bold; margin-bottom:20px;">➕ Add a New Task</div>', unsafe_allow_html=True)

# ------------------ Add Task Form ------------------
with st.form("new_task"):
    title = st.text_input("Title")
    description = st.text_area("Description")
    submit = st.form_submit_button("Add Task")
    if submit:
        if title.strip():
            add_task(title, description)
            st.success("✅ Task added successfully!")
            st.session_state.refresh = True
        else:
            st.warning("⚠️ Please enter a title before adding.")

# ------------------ Show Tasks ------------------
st.markdown("<h3 style='color:yellow;'>Your Tasks:</h3>", unsafe_allow_html=True)
tasks = get_tasks()

for task in tasks:
    with st.container():
        title_color = "#00FF00" if task["completed"] else "white"
        st.markdown(f"<div class='task-box'><b style='color:{title_color};'>{task['title']}</b><br>{task['description']}</div>", unsafe_allow_html=True)
        cols = st.columns([1,1,1])
        with cols[0]:
            checkbox_val = st.checkbox("Completed", value=task["completed"], key=f"chk_{task['id']}")
            if checkbox_val != task["completed"]:
                toggle_task(task["id"], task["completed"])
                st.session_state.refresh = True
        with cols[1]:
            if st.button("Delete", key=f"del_{task['id']}"):
                delete_task(task["id"])
                st.session_state.refresh = True

# ------------------ Refresh Logic ------------------
if st.session_state.refresh:
    st.session_state.refresh = False
    # UI updates naturally; no experimental_rerun required
