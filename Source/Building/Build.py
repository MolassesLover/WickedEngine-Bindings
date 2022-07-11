#region Modules

import os
import subprocess 
from sys import platform
import warnings

#endregion

#region Functions

def Build(): 
    # GNU/Linux
    if platform == "linux" or platform == "linux2":
        subprocess.run(['sh', 'Build.sh'], shell=False)
    
    # macOS & Darwin
    elif platform == "darwin":
        subprocess.run(['sh', 'Build.sh'], shell=False)

    # Windows
    elif platform == "win32":
        warnings.warn("Script not designed for Windows!")
        subprocess.run(['sh', 'Build.sh'], shell=False)

#endregion

#region Launch

if __name__ == "__main__":
    Build()

#endregion