import os
import shutil
import subprocess

def move_and_compress_videos(source_dir):
    # Set the destination and compressed directories
    destination_dir = os.path.join(source_dir, 'vids')
    compressed_dir = os.path.join(source_dir, 'comp vids')

    # Create the 'vids' and 'comp vids' folders if they don't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    if not os.path.exists(compressed_dir):
        os.makedirs(compressed_dir)

    # Move video files to the destination folder if not already there
    video_extensions = ['.mov', '.mp4']
    found_videos_source = False

    for file_name in os.listdir(source_dir):
        if any(file_name.lower().endswith(ext) for ext in video_extensions):
            found_videos_source = True
            source_path = os.path.join(source_dir, file_name)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(source_path, destination_path)

    # If no videos found in the source directory, check 'vids' folder
    if not found_videos_source:
        found_videos_vids = any(file_name.lower().endswith(ext) for ext in video_extensions for file_name in os.listdir(destination_dir))
        if not found_videos_vids:
            print("No video files found.")
            return

    print("Video files moved to the video subfolder.")

    # Compress videos in the 'vids' folder and save in 'comp vids' folder
    for file_name in os.listdir(destination_dir):
        source_path = os.path.join(destination_dir, file_name)
        compressed_path = os.path.join(compressed_dir, f"compressed_{file_name}")

        # Using ffmpeg to compress videos
        subprocess.run(["ffmpeg", "-i", source_path, "-c:v", "libx264", "-crf", "23", "-c:a", "aac", compressed_path])

    print("Videos compressed successfully.")

if __name__ == "__main__":
    source_directory = input("Enter the path of your folder: ")
    move_and_compress_videos(source_directory)
