import os
import subprocess
import shutil

def convert_wav_to_mp4(wav_file, mp4_file, image_file=None):
    """
    Converts a .wav file to .mp4.
    If an image is provided, it creates a video with the audio.
    """

    # Check if ffmpeg is installed
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is not installed. Please install it first.")

    if image_file:
        # Convert audio + image to video
        command = [
            "ffmpeg", "-loop", "1", "-i", image_file,
            "-i", wav_file,
            "-c:v", "libx264", "-profile:v", "main", "-preset", "medium",
            "-tune", "stillimage", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-shortest",
            "-f", "mp4", mp4_file
        ]
    else:
        # Convert audio only
        command = [
            "ffmpeg", "-i", wav_file,
            "-f", "lavfi", "-i", "color=c=black:s=720x480:r=30",
            "-c:v", "libx264", "-profile:v", "main", "-preset", "medium",
            "-pix_fmt", "yuv420p", "-shortest",
            "-c:a", "aac", "-b:a", "192k",
            "-f", "mp4", mp4_file
        ]

    subprocess.run(command, check=True)
    print(f"Conversion completed: {mp4_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert WAV to MP4")
    parser.add_argument("wav_file", help="Path to the input .wav file")
    parser.add_argument("mp4_file", help="Path to the output .mp4 file")
    parser.add_argument("--image", help="Optional image file for video background", default=None)

    args = parser.parse_args()

    convert_wav_to_mp4(args.wav_file, args.mp4_file, args.image)
