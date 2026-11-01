from yt_dlp import YoutubeDL

def download_video(url, folder="yt_videos"):
	options = {
		"format" : "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
		"merge_output_format" : "mp4",
		"outtmpl" : f"{folder}/%(title).20s.%(ext)s"
	}
	
	with YoutubeDL(options) as yld:
		yld.download([url])

link = input("Paste hare: " )
download_video(link)
