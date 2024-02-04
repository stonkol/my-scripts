import os
import shutil

def move_videos(source_dir):
    # Set the destination directory
    destination_dir = os.path.join(source_dir, 'vids')

    # Create the 'vids' folder if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Move video files to the destination folder
    video_extensions = ['.mov', '.mp4']
    for file_name in os.listdir(source_dir):
        if any(file_name.lower().endswith(ext) for ext in video_extensions):
            source_path = os.path.join(source_dir, file_name)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(source_path, destination_path)

    print("Video files moved successfully.")

if __name__ == "__main__":
    source_directory = input("Enter the path to the source directory: ")
    move_videos(source_directory)
