# Updater (GitHub)

A simple implementation of a GitHub updater, to check for new releases of a project.

You will see `TODO` comments sprinkled around. These are guides to help with the setup process so you know what needs to be altered.

## Edit the Updater class to suit your needs

`Updater` comes with `print` statements by default. You may or should replace them with a logger, so it's useful to pair with the Logger module.

## Disclaimer
The release comparison is set to compare between the local release and the latest remote release.

You may extend it further with the included methods and variables for the API calls.

`self._api_releases = "/releases"` Endpoint to retrieve all remote releases. Returns a List of Dictionaries (`list[dict]`)

`self._api_releases_latest = "/releases/latest"` Endpoint to retrieve the latest release. Returns a Dictionary `dict` 

## Pre-configured keys for Release Information
`self._release_name = "name"` Used on pulled release dictionary `dict.get(self._release_name)`

`self._release_tag = "tag_name"` Used on pulled release dictionary `dict.get(self._release_tag)`

`self._assets_tag = "assets"` Used on pulled release dictionary `dict.get(self._assets_tag)`

`self._download_url = "browser_download_url"` Used on pulled release dictionary `dict.get(self._download_url)`

---

In the other modules, you can simply import it like this example
```
from source_folder.updater.updater import Updater
```
And define it where you need to, giving it your GitHub username and GitHub repository name

Set the local version after, so it matches your current version to compare to the remote version
```
updater = Updater("<github_user>", "<repository name>")
updater.set_current_version("0.0.0") # <-- Your versioning number here
```

To trigger an update check:
```
has_update = updater.check_for_update()
```