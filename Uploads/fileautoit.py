import autoit

autoit.run("notepad.exe")
autoit.win_wait("Untitled - Notepad", 15)
autoit.control_send("Untitled - Notepad", "Edit1", "text")
