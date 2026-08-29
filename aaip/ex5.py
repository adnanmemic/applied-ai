import os


def create_project_structure(base_path, project_name):
    if not isinstance(base_path, str):
        raise TypeError("Base path must be a string!")

    if not isinstance(project_name, str):
        raise TypeError("Project name must be a string!")

    if not base_path.strip():
        raise ValueError("Base path can not be an empty string!")

    if not project_name.strip():
        raise ValueError("Project name can not be an empty string!")

    path = os.path.join(base_path, project_name)
    if os.path.exists(path):
        print("Project already exists!")
        return
    src_path = os.path.join(path, "src")
    docs_path = os.path.join(path, "docs")

    os.makedirs(path)
    os.mkdir(src_path)
    os.mkdir(docs_path)

    readme_path = os.path.join(path, "README.md")
    main_file_path = os.path.join(src_path, "main.py")

    with open(readme_path, "w", encoding="utf-8") as file:
        default = f"# {project_name}\n\nDescription of your project"
        file.write(default)

    with open(main_file_path, "w", encoding="utf-8") as file:
        default = 'print("Hello, World!")'
        file.write(default)
