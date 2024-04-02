import os
import subprocess

cwd = os.getcwd()
cwd = cwd + "/files"
def convert(input,format):
    command = [
    'libreoffice',      # Command
    '--headless',       # Run in headless mode
    '--convert-to',     # Convert to specified format
    format,
    '--outdir',
    cwd,             # Convert to epub format
    input          # Input file name (variable)
    ]
    subprocess.run(command)


def delete_files(folder_path):
    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the path points to a file (not a directory)
        if os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)
