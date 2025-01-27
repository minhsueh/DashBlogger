from dash import html, dcc
from pathlib import Path
import os


# Automatically generate links based on files in the pages folder
def generate_sidebar_links(page_path, text_color):
    """
    Generates a sidebar based on Python files located directly under the /pages/ directory.

    Args:
        page_path (pathlib.PosixPath): A Path object representing the /pages/ directory for easy modification.
        text_color (str): The color of the text for the sidebar links.

    Returns:
        links (list of Dash components): A list of Dash components that can be directly used as the children of a dash.Div.
    """
    links = []
    filenames = [file.name for file in page_path.iterdir() if file.is_file()]
    for filename in filenames:
        if not filename.startswith('_') and filename != 'home.py' and filename.endswith(".py"):  # Include only Python files
            # Remove the .py extension for the link name
            page_name = filename[:-3]
            link = dcc.Link(
                page_name.capitalize(),  # Capitalize for display purposes
                href=f"/{page_name}",  # Use the page name as the URL
                style={"color": text_color, "text-decoration": "none", "padding": "5px"}
            )

            links.append(link)
            links.append(html.Br())  # Add a line break between links
    return links


# Automatically generate links based on files in the /pages/*/ folder
def generate_content_links(page_path, text_color):
    """
    Generates a sidebar based on Python files located directly under the /pages/*/ directory.

    Args:
        page_path (pathlib.PosixPath): A Path object representing the /pages/ directory for easy modification.
        text_color (str): The color of the text for the sidebar links.

    Returns:
        links (list of Dash components): A list of Dash components that can be directly used as the children of a dash.Div.
    """
    links = []
    filenames = [file.name for file in page_path.iterdir() if file.is_file()]
    for filename in filenames:
        if not filename.startswith('_') and filename != 'home.py' and filename.endswith(".py"):  # Include only Python files
            # Remove the .py extension for the link name
            page_name = filename[:-3]
            link = dcc.Link(
                page_name.capitalize(),  # Capitalize for display purposes
                href=f"/{page_path.stem}/{page_name}",  # Use the page name as the URL
                style={"color": text_color, "text-decoration": "none"}
            )

            links.append(link)
            links.append(html.Br())  # Add a line break between links
    return links

def get_url_path(file_path):
    """
    Generates a URL path for the 'path' argument in 'dash.register_page'.
    The URL path is derived based on the structure of the /pages/ directory.

    Args:
        file_path (str): The file path of the script invoking this function, typically obtained using '__file__'.

    Returns:
        url_str (str): The URL path corresponding to the invoking file.
    """
    # Normalize the file path
    file_path = os.path.normpath(file_path)

    # Split the path into parts
    parts = file_path.split(os.sep)

    # Find the 'pages' directory in the path
    if "pages" not in parts:
        raise ValueError("The path does not contain a 'pages' directory.")
    pages_index = parts.index("pages")

    # Extract the relative path after 'pages'
    relative_parts = parts[pages_index + 1:]

    # Remove the .py extension from the last part
    relative_parts[-1] = os.path.splitext(relative_parts[-1])[0]

    # Join the parts with "/" to create the desired relative path
    return "/" + "/".join(relative_parts)


def get_page_path(file_path):
    """
    Generates a file path for the `generate_content_links` function to iterate through the files in a specified folder.

    Args:
        file_path (str): The file path of the script invoking this function, typically obtained using '__file__'.

    Returns:
        url_str (str): The URL path corresponding to the invoking file.
    """
    current_file = Path(file_path)
    page_path = current_file.parent / current_file.stem

    return(page_path)
