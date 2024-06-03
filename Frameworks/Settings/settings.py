import json
import os
import pathlib
import sys
import platform
from typing import Union

# TODO: Import logger here
# TODO: Optional: Import Singleton class

Path = pathlib.Path
HOST: str = ""
APP_FOLDER: str = ""
APP_NAME: str = ""

# TODO: Create/Assign Logger here
# TODO: Replace print() calls with logger calls

system = platform.system().lower()
if "windows" in system:
    print("Target System Windows")
    program_data_path = os.getenv("LOCALAPPDATA")
elif "linux" in system or "unix" in system:
    print("Target System Linux/Unix")
    program_data_path = Path("/usr/local/var/")
elif "darwin" in system or "mac" in system:
    print("Target System MacOS")
    # Write to user-writable locations, like ~/Applications
    program_data_path = Path(Path.home() / "Applications")
else:
    print("Target System Other")
    print(system)
    program_data_path = Path.cwd()

config_folder = Path(program_data_path) / HOST / APP_FOLDER / APP_NAME

print(f"Config folder: {config_folder}")

# TODO: Optional: metaclass=Singleton
class Settings:
    def __init__(self):
        self.settings = {
            "app-version": "",
        }
        self._config_file_name = "-settings.json" # TODO: App Name suffix
        self.config_dir = Path(config_folder)
        self.config_file = Path(config_folder) / self._config_file_name

    def set_app_version(self, version: str):
        self.settings["app-version"] = version
        self.save_config()

        return self

    def get_app_version(self) -> str:
        self.load_config()
        v = self.settings.get("app-version")
        return v

    # TODO: Set/Get methods here

    def save_config(self) -> Path:
        if self.config_dir == '' or not Path(self.config_dir).exists():
            os.makedirs(self.config_dir)
            print(f"Generated config folder {self.config_dir}")

        with open(self.config_file, 'w', encoding="utf-8") as config_file:
            config_file.write(json.dumps(self.settings, indent=2))
            print(f"Saved config {self.config_file}")

        return self.config_file

    def load_config(self) -> dict:
        if self.config_dir == '' or not Path(self.config_dir).exists()\
                or not Path(self.config_file).exists():
            print(f"Config does not exist.")
            return {}

        self.clean_save_file()

        print(f"Loading config {self.config_file}")
        config_error = False
        with open(self.config_file, 'r', encoding="utf-8") as config_file:
            try:
                self.settings = json.load(config_file)
            except Exception as e:
                print("An error occurred trying to read config file.")
                print(e)
                config_error = True

        if config_error:
            print("Generating new config file.")
            with open(self.config_file, 'w', encoding="utf-8") as config_file:
                config_file.write(json.dumps(self.settings, indent=2))
        print(self.settings)

        return self.settings

    def get_config_dir(self) -> Path:
        if not self.config_dir or not Path(self.config_dir).exists:
            return Path(os.path.dirname(sys.executable))

        return self.config_dir

    def clean_save_file(self) -> bool:
        """
        Removes unused keys from the save file.
        :return: `bool`
        """

        if not self.config_dir or not Path(self.config_dir).exists():
            print("No config folder found.")
            return False

        with open(self.config_file, 'r', encoding="utf-8") as config_file:
            settings = dict(json.load(config_file))

        for setting in reversed(list(settings.keys())):
            if setting not in self.settings.keys():
                settings.pop(setting)
                print(f"Cleared unused settings key: {setting}")

        # Add non existant settings
        for k, v in self.patcher_settings.items():
            if k not in settings:
                settings[k] = v
                print(f"Added {k}: {v}")

        with open(self.config_file, 'w', encoding="utf-8") as config_file:
            config_file.write(json.dumps(settings, indent=2))
            print(f"Saved cleaned config: {self.config_file}")

        print("Cleaned-up saved file")

        return True
