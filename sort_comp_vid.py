# WHAT IT IS ->

# todo list:
# [ ] check if has been succesfully compressed
# [ ] calculate the videos that will be going to compressed from
#     the video number in "vids" and not the videos moved to "vids"
# [ ] if a video cource is missing show an error
# [ ] if thepath didnt exidt show an error, instead of creating a wrong path
# [ ] change the line print after a file has been commpressed
# [ ] improve the progress bar, it often stucks visually, like 0% -> 72% and
#     then ends at 82% and go to compresse the next file, it should end in 100%
# [ ] progress bar shouldnt be stuck there after finished compressing that file
# [ ] hide remaing and elapsed
# [ ] hide '83/100' parameter in progress bar.

import os
import shutil
import subprocess

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

    print(f"    {total_videos} videos found 👁️🫦👁️  Let's compress them!\n")

    # Compress videos in the 'vids' folder and save in 'comp vids' folder
    for file_name in os.listdir(destination_dir):
        if file_name.lower() == ".ds_store":
            continue  # Skip .DS_Store files
        source_path = os.path.join(destination_dir, file_name)
        compressed_path = os.path.join(compressed_dir, file_name)

        # Using ffmpeg to compress videos
        output_file_name = f"{file_name}"  # New file name for compressed video
        output_path = os.path.join(compressed_dir, output_file_name)

        ############## adjust ffmpeg parameters as needed #################
        # libx264 (encode), 18~24 is the common CRF parameter
        command = ["ffmpeg", "-i", source_path, "-c:v", "libx264", "-crf", "21", "-c:a", "aac", output_path]
        ####################################################################

        compressed_videos += 1
        print(f"    [{compressed_videos}/{total_videos}] 🔥 Compressing {file_name}...")

        try:
            with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True) as p:
                if p.stdout:
                    for line in p.stdout:
                        pass  # Process output line by line
                else:
                    print("No output from ffmpeg command.")
        except Exception as e:
            print(f"Error occurred while compressing {file_name}: {e}")

    # After finished
    print("\n         🍔All Videos are now Hot and Compressed🍔")

if __name__ == "__main__":
    source_directory = input("    💬  Tell me the Path -> ")
    move_and_compress_videos(source_directory)
