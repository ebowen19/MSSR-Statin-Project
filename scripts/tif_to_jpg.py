#%%
import os
from PIL import Image

folder = '/workspaces/MSSR-Statin-Project/images'
#%%
for filename in os.listdir(folder):
    if filename.endswith(".tif"):
        # Construct the full file path for the TIFF file
        file_path = os.path.join(folder, filename)
        # Extract filename without extension
        file_name_without_ext = os.path.splitext(filename)[0]
        # Define the new filename with .jpg extension
        new_file_path = os.path.join(folder, file_name_without_ext + ".jpg")

        # Check if the JPEG version already exists
        if not os.path.exists(new_file_path):
            # Open the image
            with Image.open(file_path) as img:
                # Convert to RGB (JPEG does not support alpha channel as in PNG)
                rgb_img = img.convert('RGB')
                # Save the image as JPEG
                rgb_img.save(new_file_path, "JPEG")
            print(f"converted '{filename}' to jpg.")
        # else:
        #     print(f"JPEG version of '{filename}' already exists. Skipping conversion.")

print("Conversion complete.")

# %%
