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

# Stats summary
total_tasks = len(todos)
completed_tasks = len([t for i, t in enumerate(todos) if f"todo_{i}" in st.session_state])
pending_tasks = total_tasks - completed_tasks

st.markdown("### 📊 Overview")
st.markdown(
    f"""
    <div style="display:flex; justify-content:space-around; text-align:center;">
        <div style="flex:1; padding:8px; background:#f9f9f9; border-radius:10px; margin:3px;">
            📝 <br><b>{total_tasks}</b><br><span style="font-size:13px; color:grey;">Total</span>
        </div>
        <div style="flex:1; padding:8px; background:#f1fff1; border-radius:10px; margin:3px;">
            ✅ <br><b>{completed_tasks}</b><br><span style="font-size:13px; color:grey;">Completed</span>
        </div>
        <div style="flex:1; padding:8px; background:#fff9f1; border-radius:10px; margin:3px;">
            ⏳ <br><b>{pending_tasks}</b><br><span style="font-size:13px; color:grey;">Pending</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Task list
st.markdown("### 📌 Your Tasks")

if todos:
    for index, todo in enumerate(todos):
        task_html = f"""
        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            padding:10px;
            margin:5px 0;
            border-radius:8px;
            background:#f8f9fa;
            ">
            <label style="display:flex; align-items:center; font-size:16px; flex:1;">
                <input type="checkbox" id="chk_{index}" style="margin-right:10px; transform: scale(1.2);" />
                {todo.strip()}
            </label>
            <form action="" method="post">
                <button name="delete_{index}" type="submit" style="
                    background:none;
                    border:none;
                    color:#ff4d4d;
                    font-size:18px;
                    cursor:pointer;
                ">✖️</button>
            </form>
        </div>
        """
        st.markdown(task_html, unsafe_allow_html=True)

        # Streamlit state handling
        if st.session_state.get(f"todo_{index}"):
            todos.pop(index)
            functions.write_todos(todos)
            st.rerun()
        if f"delete_{index}" in st.session_state:
            todos.pop(index)
            functions.write_todos(todos)
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
st.markdown(
    """
    <div style="display:flex; justify-content:space-around; margin-top:10px;">
        <button style="
            flex:1; margin:5px; padding:10px;
            background:#4CAF50; color:white;
            border:none; border-radius:8px; cursor:pointer;
        ">✅ Mark All Done</button>
        <button style="
            flex:1; margin:5px; padding:10px;
            background:#ff4d4d; color:white;
            border:none; border-radius:8px; cursor:pointer;
        ">❌ Clear All</button>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown(
    """
    <p style="text-align:center; color:grey; font-size:13px; margin-top:20px;">
        Built with ❤️ using Streamlit | Mobile Optimized 📱
    </p>
    """,
    unsafe_allow_html=True
)
