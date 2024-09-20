# file_handling_assignment.py

def create_file():
    """Create a new text file and writes initial content."""
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Jambo, Kenya!\n")
            file.write("Habari ya Nairobi.\n")
            file.write("Uchumi ikoje sikuhizi.\n")
        print("Nairobi kuzuri Homa ndo imezidi.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("imesawasizwa.")

def read_file():
    """Reads the content of the text file and displays it."""
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Read file operation completed.")

def append_to_file():
    """Appends additional content to the existing text file."""
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending new line 1.\n")
            file.write("Appending new line 2.\n")
            file.write("Appending new line 3.\n")
        print("Additional content appended successfully.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Append to file operation completed.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  