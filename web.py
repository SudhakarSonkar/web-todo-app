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
    st.session_state['new_todo'] = ""  # 🔥 Clear input after adding


# ========================= UI =========================

# App Title with custom style
st.markdown(
    """
    <h1 style="color:#4CAF50; text-align:center; font-family:Helvetica;">
        ✅ My Todo App
    </h1>
    <p style="text-align:center; color:grey; font-size:18px;">
        Organize your day and increase productivity 🚀
    </p>
    """,
    unsafe_allow_html=True
)

# Stats summary
st.subheader("📊 Task Overview")
total_tasks = len(todos)
completed_tasks = len([t for i, t in enumerate(todos) if f"todo_{i}" in st.session_state])
pending_tasks = total_tasks - completed_tasks

col1, col2, col3 = st.columns(3)
col1.metric("📝 Total", total_tasks)
col2.metric("✅ Completed", completed_tasks)
col3.metric("⏳ Pending", pending_tasks)

st.markdown("---")

# Show existing todos
st.subheader("📌 Your Tasks")

if todos:
    for index, todo in enumerate(todos):
        col1, col2 = st.columns([0.9, 0.1])  # Task + delete button
        with col1:
            checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
        with col2:
            if st.button("❌", key=f"delete_{index}"):
                todos.pop(index)
                functions.write_todos(todos)
                st.rerun()

        # If checked, auto-remove
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[f"todo_{index}"]
            st.rerun()
else:
    st.info("No tasks yet. Add your first todo below ⬇️")

# Add new todo input
st.subheader("➕ Add a New Task")
st.text_input(
    label="",
    placeholder="Type your todo and press Enter...",
    on_change=add_todo,
    key='new_todo'
)

# Footer
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:grey; font-size:14px;">
        Built with ❤️ using Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
