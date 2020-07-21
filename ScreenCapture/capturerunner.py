import threading
from concurrent.futures.thread import ThreadPoolExecutor

import cv2

from ScreenCapture.screencapture import ScreenCapture

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


class ScreenCaptureRunner:

    executor = ThreadPoolExecutor(max_workers=10)
    threads = []

    @staticmethod
    def run(test, filename, window):
        sc = ScreenCapture(window, filename)
        ScreenCaptureRunner.executor.submit(sc.capture_window_into_file)
        ScreenCaptureRunner.threads.append((test, sc, threading.current_thread().ident))
        print("Threads ------->", ScreenCaptureRunner.threads)

    @staticmethod
    def shutdown(test):
        output = [item for item in ScreenCaptureRunner.threads if test in item]
        print("output class =", output[0][1])
        output[0][1].stop_capturing()
        # sc.stop_capturing()



# def main():
    # scr = ScreenCapture('', 'output2.avi')
    # ScreenCaptureRunner.run('test1', 'yossi2.avi', 'Adobe Acrobat Pro DC')
    # sleep(6)
    # ScreenCaptureRunner.shutdown('test1')
    # ScreenCaptureRunner.run('test2', 'yossi2.avi', '')
    # ScreenCaptureRunner.run('test3', 'yossi3.avi', None)
    # captureThread = threading.Thread(target=scr.capture_window_into_file, args=())
    # captureThread.start()
    # # scr.capture_window_into_file()
    # sleep(3)
    # # scr.terminate_capturing(captureThread)
    # scr.stop_capturing()


# if __name__ == "__main__":
#     main()
