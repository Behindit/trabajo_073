import cx_Freeze
import sys

cx_Freeze.setup(
	name="Main.py",
	version="0.5.5",
	options={"build_exe": {"packages": ["pygame"],
						   "include_files":["img1.png", "img2.png"]}
		    },
	executables=[cx_Freeze.Executable("Main.py")]
)
