import os
import zipfile
import shutil
import subprocess
from tqdm import tqdm

def clear_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error al eliminar {file_path}: {e}")

def unblock_file(filepath):
    streams_exe = r"C:\Tools\streams.exe"
    command = [streams_exe, '-d', filepath]
    try:
        subprocess.run(command, check=True)
        print(f"{filepath} ha sido desbloqueado.")
    except subprocess.CalledProcessError as e:
        print(f"Error al desbloquear {filepath}: {e}")

def unzip_file(zip_filepath, extract_to):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        total_files = len(zip_ref.namelist())
        with tqdm(total=total_files, unit='file') as pbar:
            for file_info in zip_ref.infolist():
                zip_ref.extract(file_info, extract_to)
                pbar.update(1)

def process_zip(zip_filepath, extract_to):
    clear_directory(extract_to)
    unblock_file(zip_filepath)
    unzip_file(zip_filepath, extract_to)

if __name__ == "__main__":
    zip_file_path = "C:/Users/st.rodriguez/Downloads/genexus-exe_std.zip"
    extract_path = "C:/gxtrunk"
    process_zip(zip_file_path, extract_path)