from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ''

# file location
def open_location():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        location_error.config(text=Folder_Name, fg='green')

    else:
        location_error.config(text='Please Choose Folder!!', fg='red')

# download video
def download_video():
    quality_choice = ytd_choices.get()
    url = ytd_entry.get()

    if len(url)>1:
        ytd_error.config(text='')
        yt = YouTube(url)

        if quality_choice == choices[0]:
            select = yt.streams.filter(progressive=True).first()

        elif quality_choice == choices[1]:
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif quality_choice == choices[2]:
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytd_error.config(text='Paste Link again!!', fg='red')

        # download function
        select.download(Folder_Name)
        ytd_error.config(text='Download Completed!!')


root = Tk()
root.title('YTD Downloader')
root.geometry('350x400')
root.columnconfigure(0, weight=1)

root.iconphoto(False, PhotoImage(file='icon_photo.png'))

ytd_label = Label(root, text='Enter the URL of the Video', font=('jost', 15))
ytd_label.grid()

ytd_entry_var = StringVar()
ytd_entry = Entry(root, width=50, textvariable=ytd_entry_var)
ytd_entry.grid()

ytd_error = Label(root, text='Error Msg', fg='red', font=('jost', 10))
ytd_error.grid()

sace_label = Label(root, text="Save the Video File", font=('jost', 15, 'bold'))
sace_label.grid()

save_entry = Button(root, width=10, bg='red', fg='white', text='Choose Path', command=open_location)
save_entry.grid()

location_error = Label(root, text='Error Msg of Path', fg='red', font=('jost', 10))
location_error.grid()

ytd_quality = Label(root, text='Select Quality', font=('jost', 15))
ytd_quality.grid()

choices = ['720p', '144p', 'Only Audio']
ytd_choices = ttk.Combobox(root, values=choices)
ytd_choices.grid()

download_button = Button(root, text='Download', width=10, bg='red', fg='white', command=download_video)
download_button.grid()

developer_label = Label(root, text='Shirali2002', font=('jost', 15))
developer_label.grid(pady=140)

root.mainloop()
