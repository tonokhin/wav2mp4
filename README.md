### If you run on Windows
you need to download from FFmpeg official site and add it to your system's PATH.

### If you run on Mac
you can install via homebrew `brew install ffmpeg`


### If you run on Linux
you can install via package manager

#### Debian/Ubuntu
`sudo apt install ffmpeg`
#### Fedora
`sudo dnf install ffmpeg`


### Run the Script
Open a terminal or command prompt and run:

#### For audio-only conversion:
`python wav_to_mp4.py input.wav output.mp4`

#### For audio with an image as video background:
`python wav_to_mp4.py input.wav output.mp4 --image background.jpg`

Replace input.wav, output.mp4, and background.jpg with your actual file names.
