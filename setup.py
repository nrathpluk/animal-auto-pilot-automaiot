from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pyautogui", "time", "random", "tkinter"],
    "excludes": [],
    "include_files": []
}

setup(
    name="AnimalAutoPilot_UI",
    version="1.0",
    description="Auto clicker with UI",
    options={"build_exe": build_exe_options},
    executables=[Executable("Farm_UI.py", base="gui")]
)
