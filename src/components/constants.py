import yaml
from box import Box
from datetime import datetime
import os
from pathlib import Path

start_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
cwd = os.getcwd()


class YamlLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_yaml()

    def load_yaml(self):
        """Load YAML file and convert it to a Box object."""
        with open(self.file_path, 'r') as file:
            yaml_content = yaml.safe_load(file)
            return Box(yaml_content)

    def get_data(self):
        """Return the loaded data as a Box object."""
        return self.data



def create_folders(folders):
    """
    Create folders and subfolders if they do not exist.
    
    :param folders: List of folder paths to create.
    """
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")
        else:
            print(f"Folder already exists: {folder}")

config = YamlLoader('src/config/config.yaml')
config = config.data
if config.save_data:
    required_folders = [os.path.join(cwd, Path(config.ModelAssets.common_dir.replace("start_time", start_time)))]
    create_folders(required_folders)



print(config.data.input_file, config.data)