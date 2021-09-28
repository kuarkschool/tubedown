import eel
import youtube_dl
import validators

eel.init('web')

@eel.expose
def download_yt(url):
    if not validators.url(url):
        return 'not valid'
    else:
        try:
            ydl_opts = {
                'format':'mp4',
                'progress_hooks': [callable_hook],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                return True
        except Exception:
            return False

def callable_hook(response):
    if response["status"] == "downloading":
        downloaded_percent = (response["downloaded_bytes"]*100)/response["total_bytes"]
        return downloaded_percent

eel.start('index.html', size=(400,200))