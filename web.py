import streamlit as st
import functions

# Load todos
todos = functions.get_todos()

# Function to add a todo
def add_todo():
    todo = st.session_state['new_todo'].strip()
    if todo:
        todos.append(todo + '\n')
        functions.write_todos(todos)
    st.session_state['new_todo'] = ""  # Clear input after adding


# ========================= UI =========================

# Title
st.title("✅ My Todo App")
st.caption("Stay organized and productive 🚀")

# Stats summary
total_tasks = len(todos)
completed_tasks = len([t for i, t in enumerate(todos) if f"todo_{i}" in st.session_state])
pending_tasks = total_tasks - completed_tasks

st.markdown("### 📊 Overview")
c1, c2, c3 = st.columns(3)
c1.metric("📝 Total", total_tasks)
c2.metric("✅ Completed", completed_tasks)
c3.metric("⏳ Pending", pending_tasks)

st.divider()

# Task list
st.markdown("### 📌 Your Tasks")

if todos:
    for index, todo in enumerate(todos):
        cols = st.columns([0.8, 0.2])  # checkbox | delete
        with cols[0]:
            checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
        with cols[1]:
            if st.button("❌", key=f"delete_{index}"):
                todos.pop(index)
                functions.write_todos(todos)
                st.rerun()

        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[f"todo_{index}"]
            st.rerun()
else:
    st.info("No tasks yet. Add your first todo below ⬇️")

# Add new task
st.markdown("### ➕ Add Task")
st.text_input(
    label="",
    placeholder="Type and press Enter...",
    on_change=add_todo,
    key='new_todo'
)

# Quick actions
st.divider()
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Mark All Done", use_container_width=True):
        todos.clear()
        functions.write_todos(todos)
        st.rerun()
with col2:
    if st.button("🗑️ Clear All", type="primary", use_container_width=True):
        todos.clear()
        functions.write_todos(todos)
        st.rerun()

# Footer
st.divider()
st.caption("Built with ❤️ using Streamlit | Mobile & Dark Mode Friendly")
