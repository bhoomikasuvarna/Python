import os
def find_files(directory, extensions):
    files = []
    for file in os.listdir(directory):
        if file.endswith(extensions):
            files.append(os.path.join(directory, file))
    return files


directory = 'D:\Aparna'
media_extensions = ('.mp3', '.mp4', '.wav', '.avi', '.mov','png','jpg','jpeg')
text_extensions = ('.txt', '.pdf', '.docx')
text_files = find_files(directory, text_extensions)
media_files=find_files(directory,media_extensions)
print("all files stored in directory",os.listdir(directory))
print(text_files)
print(media_files)


