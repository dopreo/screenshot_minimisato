# main.py

# Please be warned that means of artificial intelligence
# (e.g. Copilot Autocomplete / Suggestions) were possibly
# utilised in the creation of this code. As such, it should
# not necessarily be treated as human-written, even if it
# may have largely been human-written.


import os, shutil
from PIL import Image
from pathlib import Path

home_dir = os.path.expanduser("~")
# home_dir = "/mnt/YOURDRIVE/Users/yourusername"
print("home_dir: " + str(home_dir))

screenshots_dir = home_dir + "/Pictures/Screenshots"
os.makedirs(screenshots_dir + "/old", exist_ok=True)

class Screenshot:
    def __init__(self, file, path, size=None):
        self.file = file
        self.path = path
        self.size = size

    def convert_to_webp(self, input_path: str, output_path: str, quality: int=100):
        img = Image.open(input_path)
        exif_data = img.info.get('exif') # collect any exif metadata

        save_kwargs = {}
        if quality >= 100 or quality <= 0:
            save_kwargs['lossless'] = True
        else:
            save_kwargs['quality'] = quality
        
        # tell img.save to re-embed exif metadata
        if exif_data:
            save_kwargs['exif'] = exif_data

        try:
            img.save(output_path, format="WEBP", **save_kwargs)
            print(f"SUCCESS: {output_path} (quality={quality})")
        except Exception as e:
            print(f"FAILED: {e}")
        
    def move_to_old_folder(self, source_path: str):
        file_name = os.path.basename(source_path)
        destination_path = os.path.join(screenshots_dir, "old", file_name)
        try:
            shutil.move(source_path, destination_path)
            print(f"MOVED: {source_path} → {destination_path}")
        except Exception as e:
            print(f"MOVE FAILED: {e}")

# Add all files in directory that are not directories
screenshots = [file for file in os.listdir(screenshots_dir) if os.path.isfile(screenshots_dir +"/"+ file) and not file.lower().endswith('.webp')]

print("screenshots:")
for file_name in screenshots:
    file_path = screenshots_dir + "/" + file_name
    file_path_no_ext, ext = os.path.splitext(file_path)
    print(
        "FILE NAME:", str(file_name) + "\n" +
        "FILE PATH:", str(file_path) + "\n"
    )
    file = Image.open(file_path)
    screenshot = Screenshot(file, file_path)
    screenshot.convert_to_webp(file_path, str(file_path_no_ext + ".minimisato.webp"))
    screenshot.move_to_old_folder(file_path)


# Please be warned that means of artificial intelligence
# (e.g. Copilot Autocomplete / Suggestions) were possibly
# utilised in the creation of this code. As such, it should
# not necessarily be treated as human-written, even if it
# may have largely been human-written.
#
# Logical decisions were still made by a human, and these
# models should have only assisted in the ensurance of proper
# syntax, for example, and the likes.
#
# Please always be upfront about the extent to which any piece
# of code or any material you may endorse, share or publish is
# AI-generated. The general public should have a right to know
# what parts of what they consume have been created by humans.