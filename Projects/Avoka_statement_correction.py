import os
import shutil
import datetime

def avoka_file_locator():

    avoka_source = r"D:\Avoka_files"          # root folder containing folders like 20250228
    copy_destination = r"E:\Avoka_copied"    # where month folders will be created

    files_copied = 0

    for root, dirs, files in os.walk(avoka_source):
        for file in files:
            if file.strip().upper() == "MM_STMXT.TXT":
                source_file = os.path.join(root, file)

                # Get the parent of the member folder (the folder named like 20250228)
                date_folder = os.path.basename(os.path.dirname(root))  # e.g., 20250228

                # Parse year and month from folder name
                try:
                    statement_date = datetime.datetime.strptime(date_folder, "%Y%m%d")
                    month_folder_name = statement_date.strftime("221475786_%Y%m%d")
                except ValueError:
                    month_folder_name = "Unknown"  # fallback if folder name isn't a date

                # Create month folder in destination
                destination_root = os.path.join(copy_destination, month_folder_name)
                os.makedirs(destination_root, exist_ok=True)

                # Numbered filename to avoid overwriting
                files_copied += 1
                destination_file = os.path.join(
                    destination_root,
                    f"221475786_{os.path.splitext(file)[0]}_{files_copied:02d}.txt"
                )

                # Copy the file
                shutil.copy2(source_file, destination_file)

                # print(f"Copied:\n{source_file}\n→ {destination_file}\n")

    print(f"Total files copied: {files_copied}")

avoka_file_locator()
