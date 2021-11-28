from tkinter import *
from tkinter import ttk
from pytube import YouTube

def DownloadVideo():
    link=download_link.get()
    print(link)
    video=YouTube(link)
    stream=video.streams.filter(progressive=True,res="360p", file_extension="mp4")
    try:
        stream.first().download()
        print('download completed')
    except Exception as e:
        print(f'video download unsuccessful : {e}')



root=Tk()

root.geometry('640x480')
root.minsize(320,280)
root.maxsize(640,480)
root.title("YouTube Downloader")

content_frame=Frame(relief="sunken", borderwidth=5,padx=50,pady=50)
content_frame.pack(anchor="center")


label_frame=Frame(content_frame,pady=5)
label_frame.pack()

label=Label(label_frame,text="Enter the link of the video to download", font=(10))
label.pack()

input_frame=Frame(content_frame,pady=10)
input_frame.pack()

download_link=StringVar()

input_bar=Entry(input_frame, borderwidth=3, width=200,textvariable=download_link)
input_bar.pack()

download_button_frame=Frame(content_frame,pady=10)
download_button_frame.pack()

btn=Button(download_button_frame,bg="teal", command=DownloadVideo ,text="Download",pady=5,padx=5, font=(20), fg="white")
btn.pack()

root.mainloop()



# frm=ttk.Frame(root,border=5)
# frm.pack()
# label=Label(frm,text="This is frame label")
# label.pack()