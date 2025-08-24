import os

FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns the list of to-do items.
    Args:
        filepath (str): The path to the text file containing to-do items.
    Returns:
        list: A list of to-do items read from the file.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes the list of to-do items to a text file.
    Args:
        todos_arg (list): The list of to-do items to write to the file.
        filepath (str): The path to the text file where to-do items will be written.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    # This block is for testing purposes only
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, 'w') as file:
            pass
    print("Functions module loaded successfully.")
