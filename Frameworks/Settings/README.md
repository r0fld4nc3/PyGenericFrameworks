# Settings

A simple file that handles basic-ish application settings needs and can quickly get you up to speed with implementing saving and retrieval of disk-saved settings for the project.

You will see `TODO` comments sprinkled around. These are guides to help with the setup process so you know what needs to be altered.

You should rename this file to a more appropriate name for your project. The following examples will use the default name herein contained of `settings`, though should you change the name of the file, bear in mind to reflect sucha a change in the import statement.

## Edit the Settings class to suit your needs

`Settings` comes with 1 example of get/set methods inside the Settings class, so the aim is to add your own settings as needed.

---

To do so, these are the basic steps:
1. In the `dict` `self.settings`, add your entries with their own keys and default values
2. In the `# TODO: Set/Get methods here` write your own Get/Set methods for each specific entry. The Get/Set methods for app-version can serve as a guideline

In the other modules, you can simply import it like this example
```
from source_folder.your_settings_folder import Settings
```
And define it where you need to
```
settings = Settings()
settings.load_config() # Can be loaded at a later stage, but recommended is right after
settings.set_app_version("0.0.0") # Optional but recommended
```

Then, to set or get a variable, simply call their respective methods.

Finally, you may run `settings.save_config()` to ensure everything is saved, you might want to call the save function to ensure the changes are committed, if you are not saving them as you Set them.
