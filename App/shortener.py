import pyshorteners

def shortener(url):
    tiny = pyshorteners.Shortener()
    shortened = tiny.tinyurl.short(url)
    return shortened