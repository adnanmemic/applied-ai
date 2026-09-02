import os
from datetime import UTC, datetime


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


def traverse_directory(path: str) -> None:
    if not isinstance(path, str):
        raise TypeError("Path must be a string!")

    if not path.strip():
        raise ValueError("Path can not be an empty string!")

    for current_dir, dirs, files in os.walk(path):
        print(f"Current directory: {current_dir}")

        dir_names = "-" if not dirs else ", ".join(dirs)
        print(f"Directories: {dir_names}")

        file_names = "-" if not files else ", ".join(files)
        print(f"Files: {file_names}")
        print()


def file_metadata(file_path):
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string!")

    if not file_path.strip():
        raise ValueError("File path can not be an empty string!")

    metadata = os.stat(file_path)
    print(f"Filesize: {metadata.st_size} Byte")

    mtime = datetime.fromtimestamp(metadata.st_mtime, tz=UTC).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    print(f"Last modified: {mtime}")

    ctime = datetime.fromtimestamp(metadata.st_ctime, tz=UTC).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    print(f"Creation time: {ctime}")

    os.chmod(file_path, 0o444)
    print(f"File '{file_path}' is now read-only!")

    os.chmod(file_path, 0o644)
    print(f"File '{file_path}' is now writeable again!")
