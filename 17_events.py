import time, threading

download_finished = threading.Event()


def downloader_worker():
    download_finished.clear()

    print("Download Started...")
    time.sleep(5)
    print("Download Finished!")

    download_finished.set()


def file_scanner_worker():
    download_finished.wait()

    print("File Scanner Started")
    time.sleep(4)
    print("File Scanner Finished")


t1 = threading.Thread(target=downloader_worker)
t2 = threading.Thread(target=file_scanner_worker)

t1.start()
t2.start()
