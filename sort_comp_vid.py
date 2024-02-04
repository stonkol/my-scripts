import os
import shutil
import subprocess

def move_videos(source_dir, destination_dir):
    # Move video files to the destination folder if not already there
    video_extensions = ['.mov', '.mp4']
    found_videos_source = False

    for file_name in os.listdir(source_dir):
        if any(file_name.lower().endswith(ext) for ext in video_extensions):
            found_videos_source = True
            source_path = os.path.join(source_dir, file_name)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(source_path, destination_path)

    return found_videos_source

def compress_videos(source_dir, destination_dir):
    # Compress videos in the 'vids' folder and save in 'comp vids' folder
    compressed_videos_exist = False

    for file_name in os.listdir(destination_dir):
        source_path = os.path.join(destination_dir, file_name)
        compressed_path = os.path.join(destination_dir, 'comp vids', f"compressed_{file_name}")

        # Check if compressed video already exists
        if not os.path.exists(compressed_path):
            compressed_videos_exist = True
            # Using ffmpeg to compress videos
            subprocess.run(["ffmpeg", "-i", source_path, "-c:v", "libx264", "-crf", "23", "-c:a", "aac", compressed_path])

    return compressed_videos_exist

def move_and_compress_videos(source_dir):
    # Set the destination and compressed directories
    destination_dir = os.path.join(source_dir, 'vids')
    compressed_dir = os.path.join(source_dir, 'comp vids')

    # Create the 'vids' and 'comp vids' folders if they don't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    if not os.path.exists(compressed_dir):
        os.makedirs(compressed_dir)

    # Move video files to the destination folder
    found_videos_source = move_videos(source_dir, destination_dir)

    # If no videos found in the source directory, check 'vids' folder
    if not found_videos_source:
        found_videos_vids = any(file_name.lower().endswith(ext) for ext in ['.mov', '.mp4'] for file_name in os.listdir(destination_dir))
        if not found_videos_vids:
            print("No video files found.")
            return

    print("Video files moved to the video subfolder.")

    # Check if compressed videos already exist
    compressed_exist = compress_videos(source_dir, destination_dir)

    if compressed_exist:
        print("Some videos were already compressed in the 'comp vids' folder.")
    else:
        print("Videos compressed successfully.")

if __name__ == "__main__":
    source_directory = input("Enter the path of your folder: ")
    move_and_compress_videos(source_directory)
