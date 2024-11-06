import json
import os
import sys
import platform
from pathlib import Path

# TODO: Import logger here

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

CONFIG_FOLDER = Path(program_data_path) / HOST / APP_FOLDER / APP_NAME

print(f"Config folder: {CONFIG_FOLDER}")

class Settings:
    _instance = None
    _loaded = False

    KEY_APP_VERSION = "app-version"

    settings = {
        "app-version": "",
    }
    _config_file_name = "-settings.json" # TODO: App Name suffix
    config_dir = Path(CONFIG_FOLDER)
    config_file = Path(CONFIG_FOLDER) / _config_file_name

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance

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
        if not self._loaded:
            if self.config_dir == '' or not Path(self.config_dir).exists()\
                    or not Path(self.config_file).exists():
                print(f"Config does not exist.")
                return self.settings

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

            self._loaded = True

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

        if not self.config_file.exists():
            print("No config file to cleanup")
            return False

        with open(self.config_file, 'r', encoding="utf-8") as config_file:
            settings = dict(json.load(config_file))
            print(f"[clean_save_file] Loaded settings: {json.dumps(settings, indent=2)}")

        for setting in reversed(list(settings.keys())):
            if setting not in self.settings.keys():
                settings.pop(setting)
                print(f"Cleared unused settings key: {setting}")

        with open(self.config_file, 'w', encoding="utf-8") as config_file:
            config_file.write(json.dumps(settings, indent=2))
            print(f"Saved cleaned config: {self.config_file}")

        print("Cleaned-up saved file")

        return True
