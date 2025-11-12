from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("local notes")

notes_file_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "notes.txt"))

@mcp.tool()
def add_note_to_file(content: str) -> str:
    """
    Add a note to the user's local notes file.

    Args:
        content (str): The content of the note to add.
    """
    try:
        with open(notes_file_path, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        return "Note added."
    except Exception as e:
        return f"Failed to add note: {e}"

@mcp.tool()
def read_notes() -> str:
    """
    Read all notes from the user's local notes file.
    """
    try:
        with open(notes_file_path, "r", encoding="utf-8") as f:
            notes = f.read()
        return notes
    except FileNotFoundError:
        return "No notes found."
    except Exception as e:
        return f"Failed to read notes: {e}"

@mcp.tool()
def note_file_path() -> str:
    """
    Get the absolute path to the user's local notes file.
    """
    return notes_file_path

if __name__ == "__main__":
    mcp.run()
