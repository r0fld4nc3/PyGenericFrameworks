# Updater (GitHub)

A simple implementation of a GitHub updater, to check for new releases of a project.

You will see `TODO` comments sprinkled around. These are guides to help with the setup process so you know what needs to be altered.

## Edit the Updater class to suit your needs

`Updater` comes with `print` statements by default. You may or should replace them with a logger, so it's useful to pair with the Logger module.

Add necessary info to `self.owner` and `self.repo_name` according to your GitHub username and repository name, so it can fetch it properly.

## Disclaimer
The release comparison is set to compare between the typical `Major.Minor.Macro` format, so `0.0.1` vs `1.2.1`, etc.

---

In the other modules, you can simply import it like this example
```
from source_folder.updater.updater import Updater
```
And define it where you need to
```
updater = Updater()
updater.set_current_version("0.0.0") # <-- Your versioning number here
```

To trigger an update check:
```
has_update = updater.check_for_update()
```