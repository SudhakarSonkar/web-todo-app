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

# Stats
total_tasks = len(todos)
completed_tasks = len([t for i, t in enumerate(todos) if f"todo_{i}" in st.session_state])
pending_tasks = total_tasks - completed_tasks

st.markdown("### 📊 Overview")
st.markdown(
    f"""
    - 📝 **Total:** {total_tasks}  
    - ✅ **Completed:** {completed_tasks}  
    - ⏳ **Pending:** {pending_tasks}  
    """
)

st.markdown("---")

# Task list
st.markdown("### 📌 Your Tasks")

if todos:
    for index, todo in enumerate(todos):
        # Inline row: checkbox + delete button
        row = st.columns([0.85, 0.15])
        with row[0]:
            checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
        with row[1]:
            delete_html = f"""
                <button style="
                    background:none;
                    border:none;
                    color:red;
                    font-size:18px;
                    cursor:pointer;
                    " onclick="fetch('/_stcore/replace?key=delete_{index}')">
                    ❌
                </button>
            """
            st.markdown(delete_html, unsafe_allow_html=True)

            if st.session_state.get(f"delete_{index}"):  # workaround since HTML button won't trigger
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
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Mark All Done"):
        todos.clear()
        functions.write_todos(todos)
        st.rerun()
with col2:
    if st.button("❌ Clear All"):
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
