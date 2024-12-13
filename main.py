import os
import fnmatch
import subprocess
from SyncBuild import process_zip

def main():
    root_dir = "C:/"
    gx_folders = [folder for folder in os.listdir(root_dir)
                  if (("trunk" in folder.lower() or "stable" in folder.lower())
                      and os.path.isdir(os.path.join(root_dir, folder)))]

    print("Seleccione la carpeta de extracción:")
    for index, folder in enumerate(gx_folders, start=1):
        print(f"{index}. {folder}")

    print(f"{len(gx_folders) + 1}. Otra (ingrese la ruta a mano)")

    option = input("Ingrese el número de su opción: ")

    if option.isdigit() and 1 <= int(option) <= len(gx_folders):
        extract_path = os.path.join(root_dir, gx_folders[int(option) - 1])
    elif option == str(len(gx_folders) + 1):
        extract_path = input("Por favor, ingrese la carpeta en la que desea extraer el archivo: ")
    else:
        print("Opción no válida. Saliendo del programa.")
        return

    # Listar los archivos ZIP en el directorio donde se espera que estén
    zip_search_directory = "C:/Users/st.rodriguez/Downloads/"
    file_to_extract_partial = input("¿Cómo se llama parcialmente el archivo que desea extraer? ")

    found_files = [f for f in os.listdir(zip_search_directory)
                   if fnmatch.fnmatch(f.lower(), f"*{file_to_extract_partial.lower()}*")]

    valid_files = [f for f in found_files if f.lower().endswith(('.zip', '.zipy'))]

    if valid_files:
        print("Archivos encontrados:")
        for index, file in enumerate(valid_files, start=1):
            print(f"{index}. {file}")

        file_index = input("Seleccione el número del archivo que desea extraer: ")

        if file_index.isdigit() and 1 <= int(file_index) <= len(valid_files):
            selected_file = valid_files[int(file_index) - 1]
            zip_file_path = os.path.join(zip_search_directory, selected_file)  # Obtiene la ruta completa del archivo ZIP
            process_zip(zip_file_path, extract_path)
            print(f"RUTA DE EXTRACCION: {extract_path}")

            # Crear el archivo por lotes
            bat_file_path = os.path.join(extract_path, 'run_genexus.bat')
            with open(bat_file_path, 'w') as bat_file:
                bat_file.write(f'@echo off\ncd /d "{extract_path}"\nstart "" "genexus" /install\n')

            # Ejecutar el archivo por lotes con privilegios de administrador
            try:
                subprocess.run(
                    ['powershell', '-Command', f'Start-Process cmd -ArgumentList "/c {bat_file_path}" -Verb RunAs'],
                    check=True)
                print("Genexus /install ejecutado con éxito.")
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el comando: {e}")
            except FileNotFoundError as e:
                print(f"No se encontró el archivo: {e}")
            except PermissionError as e:
                print(f"Error de permisos: {e}")
            except OSError as e:
                print(f"Error de sistema: {e}")
        else:
            print("Opción no válida. Saliendo del programa.")
    else:
        print("No se encontraron archivos que coincidan con el criterio.")

if __name__ == "__main__":
    main()