import time, threading


def downloader_worker():
    print("Download Started...")
    time.sleep(5)
    print("Download Finished!")


def file_scanner_worker():
    print("File Scanner Started")
    time.sleep(4)
    print("File Scanner Finished")