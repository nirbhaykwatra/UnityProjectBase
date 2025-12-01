import os
import shutil

# TODO: Create a command line utility for making projects using this template.
#   Parameters:
#       project_name - Name of the new project
#       project_path - Path to copy project files to
#
#   Functionality: Once user has entered the parameters, recursively copy all the necessary files and folders to the
#                  given path. Once copied, edit the readme to say the name of the project.

def create_project(project_source:str, project_name: str, project_path: str):
    project_directory: str = os.path.join(project_path, project_name)
    folders_to_copy: list[str] = ["Assets", "DOCUMENTATION", "FMOD", "Packages", "ProjectSettings", "RAW", "Scripts"]
    files_to_copy: list[str] = [".gitattributes", ".gitignore", "Jenkinsfile", "LICENSE", "README.md"]

    print("Creating project directory...")

    for folder in folders_to_copy:
        print(f"Copying {folder} folder...")
        shutil.copytree(os.path.join(project_source, f"{folder}"), os.path.join(project_directory, f"{folder}"))
        print("Done!")

    for file in files_to_copy:
        print(f"Copying {file} file...")
        shutil.copy(os.path.join(project_source, f"{file}"), os.path.join(project_directory, f"{file}"))
        print("Done!")

    print(f"Project created successfully at {project_directory}!")
    print("Edit the README.md file to change the project name.")

if __name__ == "__main__":
    name: str = str(input("Enter the name of the new project: "))
    source: str = str(input("Enter the path to the template project: "))
    path: str = str(input("Enter the path to copy the project to: "))
    create_project(source, name, path)
    input("Press any key to exit...")
