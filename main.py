from pytube import YouTube
import ttkbootstrap as ttk
import tkinter as tk

window = ttk.Window(title="YouTube video downloader (by Honzoraptor)", themename="cyborg")
window.geometry("1200x700")
window.minsize(1000, 500)

ctrlsPadding = 10

def download():
  text["text"] = "Downloading the video..."
  yt = YouTube(inputFieldStr.get())
  yd = yt.streams.get_highest_resolution()
  yd.download("./Downloaded videos from YouTube")
  text["text"] = f"Just downloaded video \"{yt.title}\" by \"{yt.author}\""

# photo = ttk.PhotoImage(file = "./youtube-logo.png")
# window.iconphoto(False, photo)

main = ttk.Frame(window)
main.pack(expand=True)

nadpis = ttk.Label(main, text="YouTube video downloader", font="Calibri, 16 bold")
nadpis.pack(pady=30)

controlls = ttk.Frame(main)
controlls.pack()

inputFieldStr = tk.StringVar(value="Link...")
inputField = ttk.Entry(controlls, textvariable=inputFieldStr)
inputField.pack(pady=30, side="left", ipadx=ctrlsPadding, ipady=ctrlsPadding)

downloadBtn = ttk.Button(controlls, text="Download", cursor="hand2", command=download)
downloadBtn.pack(side="right", ipadx=ctrlsPadding, ipady=ctrlsPadding)

vidInfo = ttk.Frame(main)
vidInfo.pack()

text = ttk.Label(vidInfo, font="Calibri 12", justify="center")
text.pack()

window.mainloop()