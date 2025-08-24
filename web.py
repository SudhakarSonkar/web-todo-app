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

# App Title
st.markdown(
    """
    <h2 style="color:#4CAF50; text-align:center; font-family:Helvetica; margin-bottom:10px;">
        ✅ My Todo App
    </h2>
    <p style="text-align:center; color:grey; font-size:16px;">
        Stay organized on the go 🚀
    </p>
    """,
    unsafe_allow_html=True
)

# Stats summary (stacked for mobile)
total_tasks = len(todos)
completed_tasks = len([t for i, t in enumerate(todos) if f"todo_{i}" in st.session_state])
pending_tasks = total_tasks - completed_tasks

with st.container():
    st.markdown("### 📊 Overview")
    st.markdown(
        f"""
        - 📝 **Total:** {total_tasks}  
        - ✅ **Completed:** {completed_tasks}  
        - ⏳ **Pending:** {pending_tasks}  
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# Show tasks (one per row, mobile friendly)
st.markdown("### 📌 Your Tasks")

if todos:
    for index, todo in enumerate(todos):
        # Show checkbox + delete icon inline
        task_col = st.columns([0.85, 0.15])
        with task_col[0]:
            checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
        with task_col[1]:
            if st.button("🗑️", key=f"delete_{index}"):
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

# Quick actions for mobile
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Mark All Done"):
        todos.clear()
        functions.write_todos(todos)
        st.rerun()
with col2:
    if st.button("🗑️ Clear All"):
        todos.clear()
        functions.write_todos(todos)
        st.rerun()

# Footer
st.markdown(
    """
    <p style="text-align:center; color:grey; font-size:13px; margin-top:20px;">
        Built with ❤️ using Streamlit | Mobile Optimized 📱
    </p>
    """,
    unsafe_allow_html=True
)
