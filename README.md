# YouTube Video Downloader

A minimal Python command-line utility that downloads a YouTube video with
[`yt-dlp`](https://github.com/yt-dlp/yt-dlp), limits the selected video to
1080p, merges the best video and audio streams, and saves the result as an
MP4 file.

## Requirements

- Python 3.8 or newer
- `ffmpeg` available on your `PATH` for merging separate audio and video
  streams

## Installation

1. Clone the repository and enter the project directory:

   ```bash
   git clone https://github.com/Srijit4514/yt_audio_downloder.git
   cd yt_audio_downloder
   ```

2. Install the Python dependencies:

   ```bash
   python -m pip install -r requerements.txt
   ```

## Usage

Run the downloader:

```bash
python downloader.py
```

When prompted, paste the URL of the video to download. The output is saved in
the `yt_videos/` directory, using the first 20 characters of the video title
as the filename.

## Notes

- The downloader selects the best available video at or below 1080p.
- Separate video and audio streams are merged into an MP4 file.
- Only use this tool to download content you have permission to save, and
  follow YouTube's terms of service and applicable laws.
