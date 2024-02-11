import os
import shutil
import subprocess
from tqdm import tqdm

def move_and_compress_videos(source_dir):
    # Set the destination and compressed directories
    destination_dir = os.path.join(source_dir, '_vids')
    compressed_dir = os.path.join(source_dir, '_comp_vids')

    # Create the 'vids' and 'comp vids' folders if they don't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    if not os.path.exists(compressed_dir):
        os.makedirs(compressed_dir)

    # Move video files to the destination folder if not already there
    video_extensions = ['.mov', '.mp4', '.m4v']
    total_videos = 0
    compressed_videos = 0
    for file_name in os.listdir(source_dir):
        if any(file_name.lower().endswith(ext) for ext in video_extensions):
            total_videos += 1
            source_path = os.path.join(source_dir, file_name)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(source_path, destination_path)

    print(f"    {total_videos} videos founded 👁️🫦👁️ let's compress them ↓\n")

    # Compress videos in the 'vids' folder and save in 'comp vids' folder
    for file_name in os.listdir(destination_dir):
        if file_name.lower() == ".ds_store":
            continue  # Skip .DS_Store files
        source_path = os.path.join(destination_dir, file_name)
        compressed_path = os.path.join(compressed_dir, file_name)

        # Using ffmpeg to compress videos
        output_file_name = f"{file_name}"  # New file name for compressed video
        output_path = os.path.join(compressed_dir, output_file_name)
        command = ["ffmpeg", "-i", source_path, "-c:v", "libx264", "-crf", "23", "-c:a", "aac", output_path]
        
        compressed_videos += 1
        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True) as p:
            for line in tqdm(p.stdout, total=100, desc=f"[{compressed_videos}/{total_videos}] 🔥 {file_name}", unit=" frames"):
                pass

    print("\n         🍔All Videos are now Hot and Compressed🍔")

if __name__ == "__main__":
    source_directory = input("    💬  Tell me the Path -> ")
    move_and_compress_videos(source_directory)
