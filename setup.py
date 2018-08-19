from cx_Freeze import setup, Executable

base = None    

executables = [Executable("ReadPDF.py", base=base)]

packages = ["idna", "os", "gtts", "PyPDF2", "pygame", "tkinter", "cx_Freeze"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
