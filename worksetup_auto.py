import webbrowser as wb
import os


def workauto():
    note_path = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
    os.startfile(note_path)
    Chrome_path = "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe %s"
    URLS = ("https://github.com/Rajesh-B-Git/Python_projects",
            "https://www.youtube.com/")

    for url in URLS:
        wb.get(Chrome_path).open(url)


workauto()
