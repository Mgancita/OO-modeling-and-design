import os
import subprocess

# Get directories
directories = next(os.walk("."))[1]
chapter_directories = [directory for directory in directories if "chapter" in directory]

# Iterate over each chapter
for directory in chapter_directories:
    # Get file names
    file_names = next(os.walk(directory))[2]

    # Get notebook names
    notebooks = [file_name for file_name in file_names if ".ipynb" in file_name]
    # For each notebook, convert to html file
    for notebook in notebooks:
        notebook_convert_path = os.path.join(directory, notebook)
        subprocess.call(f"jupyter nbconvert --to html {notebook_convert_path}")

    # Get html files and readme path
    html_files = [file_name for file_name in file_names if ".html" in file_name]
    readme_path = os.path.join(directory, "README.md")
    # Open readme, write the header for the directory (chapter) and all the section html files.
    with open(readme_path, "w+") as directory_readme:
        chapter_name = directory.replace("chapter", "Chapter ")
        directory_readme.write(f"# {chapter_name}\n\n")

        for html_file in html_files:
            html_preview_link = f"https://htmlpreview.github.io/?https://github.com/Mgancita/OO-modeling-and-design/blob/master/{directory}/{html_file}"
            link_text = html_file.replace("-", " ").replace(".html", "").capitalize().title()
            directory_readme.write(f"- [{link_text}]({html_preview_link})\n")


