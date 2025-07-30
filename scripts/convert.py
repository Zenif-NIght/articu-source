from pxr import Sdf
import os
import shutil

# # Load the .usd (binary) layer
# layer = Sdf.Layer.FindOrOpen("/home/user/Documents/articu-source/assets/open-door/door_09/parts/Frame_JQD.usd")

# # Export as .usda (ASCII)
# layer.Export("Frame_JQD.usda")

def convert_usd_to_usda_recursive(src_folder):

    # Create destination root folder with _1 suffix
    dst_root = src_folder.rstrip(os.sep) + "_1"
    if os.path.exists(dst_root):
        shutil.rmtree(dst_root)
    os.makedirs(dst_root)

    for root, _, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith('.usd'):
                src_path = os.path.join(root, file)
                # Compute relative path and destination path
                rel_dir = os.path.relpath(root, src_folder)
                dst_dir = os.path.join(dst_root, rel_dir)
                os.makedirs(dst_dir, exist_ok=True)
                dst_file = os.path.splitext(file)[0] + '.usda'
                dst_path = os.path.join(dst_dir, dst_file)
                # Convert and export
                layer = Sdf.Layer.FindOrOpen(src_path)
                if layer:
                    layer.Export(dst_path)


convert_usd_to_usda_recursive("assets/open-door/door_09")