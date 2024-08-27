import yaml
from box import Box

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


config = YamlLoader('src/config/config.yaml')

print(config.data.input_file)