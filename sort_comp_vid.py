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
    if not os.path.isdir(source_dir):
        raise NotADirectoryError(source_dir)
    # Set the destination and compressed directories
    destination_dir = os.path.join(source_dir, '_vids')
    compressed_dir = os.path.join(source_dir, '_comp_vids')

    # Create the 'vids' and 'comp vids' folders if they don't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    if not os.path.exists(compressed_dir):
        os.makedirs(compressed_dir)

    # Move video files to the destination folder if not already there
    video_extensions = ('.mov', '.mp4', '.m4v')
    for file_name in os.listdir(source_dir):
        source_path = os.path.join(source_dir, file_name)
        if os.path.isfile(source_path) and file_name.lower().endswith(video_extensions):
            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(source_path, destination_path)

    files_to_compress = [name for name in os.listdir(destination_dir)
                         if os.path.isfile(os.path.join(destination_dir, name))
                         and name.lower().endswith(video_extensions)]
    total_videos = len(files_to_compress)
    print(f"    {total_videos} videos found 👁️🫦👁️  Compressing!\n")
    compressed_videos = 0

    for file_name in files_to_compress:
        source_path = os.path.join(destination_dir, file_name)
        stem, _extension = os.path.splitext(file_name)
        output_path = os.path.join(compressed_dir, f"{stem}_compressed.mp4")

        ############## adjust ffmpeg parameters as needed #################
        # libx264 (encode), 18~24 is the common CRF parameter
        command = ["ffmpeg", "-y", "-i", source_path, "-c:v", "libx264", "-crf", "21", "-c:a", "aac", output_path]
        ####################################################################

        print(f"    [{compressed_videos + 1}/{total_videos}] 🔥 Compressing {file_name}...")

        try:
            result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                                    text=True, check=False)
            if result.returncode == 0 and os.path.isfile(output_path) and os.path.getsize(output_path) > 0:
                compressed_videos += 1
                print(f"    Finished: {output_path}")
            else:
                print(f"    Failed to compress {file_name}: {result.stderr.strip()}")
                if os.path.exists(output_path) and os.path.getsize(output_path) == 0:
                    os.remove(output_path)
        except Exception as e:
            print(f"Error occurred while compressing {file_name}: {e}")

    # After finished
    print(f"\n    🍔Compressed {compressed_videos} of {total_videos} videos🍔")

if __name__ == "__main__":
    source_directory = input("    💬 Tell me the Path: ")
    move_and_compress_videos(source_directory)
