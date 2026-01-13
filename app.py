import shutil
from pathlib import Path

# Define specific target folders and their extensions
# Extension lists based on 2026 development and data science standards
FILE_MAPPING = {
    "Datasets": [".csv", ".xlsx", ".json", ".parquet", ".h5", ".parquet", ".feather", ".db", ".sql"],
    "PDFs": [".pdf"],
    "Code": [".py", ".ipynb", ".js", ".html", ".css", ".cpp", ".java", ".sh", ".yaml", ".toml"]
}

def organize_files(target_directory):
    base_path = Path(target_directory)
    
    if not base_path.exists():
        print("Error: The specified folder does not exist.")
        return

    # Iterate through every file in the directory
    for file_path in base_path.iterdir():
        # Skip if it's a folder or the script itself
        if file_path.is_dir() or file_path.name == Path(__file__).name:
            continue

        # Determine target folder based on file extension
        extension = file_path.suffix.lower()
        target_folder_name = "Others" # Default for unknown files

        for folder_name, extensions in FILE_MAPPING.items():
            if extension in extensions:
                target_folder_name = folder_name
                break

        # Create destination folder and move file
        dest_folder = base_path / target_folder_name
        dest_folder.mkdir(exist_ok=True)
        
        try:
            shutil.move(str(file_path), str(dest_folder / file_path.name))
            print(f"Moved '{file_path.name}' to {target_folder_name}/")
        except Exception as e:
            print(f"Failed to move {file_path.name}: {e}")

if __name__ == "__main__":
    folder_to_clean = input("Enter the path of the folder to organize: ").strip()
    organize_files(folder_to_clean)
