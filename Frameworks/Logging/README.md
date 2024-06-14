# Logging
A simple file that handles basic-ish logging needs and can quickly get you up to speed with implementing a logger for the project.
Replace the string bound to `log_fle` to your own log file name.

You should rename this file to a more appropriate name for your project. The following examples will use the default name herein contained of `custom_logger`, though should you change the name of the file, bear in mind to reflect sucha a change in the import statement.

---

In the other modules, you can simply import it like this example
```
from source_folder.your_logger_folder import create_logger
```
And define it where you need to
```
custom_logger = create_logger("MyLogger", 1)
```

`create_logger` Takes 2 arguments:
- **[str]** Logger Name
- **[int]** Logger Level (_0 - 3_)

The logger levels from 0 through 3 correspond to most logging to more cherry-picked logging:
- 0: **DEBUG**
- 1: **INFO**
- 2: **WARN**
- 3: **ERROR**

If you need to reset the log file, you can also import the method to do so and just call it when you need it

```
from source_folder.your_logger_folder import reset_log_file
```
