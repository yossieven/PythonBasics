import os

import cv2
import numpy as np
import win32gui
from PIL import ImageGrab
from win32api import GetSystemMetrics
from win32con import SW_SHOW

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


class ScreenCapture():

    def __init__(self, window, filename):
        self.window = window
        self.filename = filename
        self.out = None
        self.stop = False

    def get_video_type(self):
        filename, ext = os.path.splitext(self.filename)
        if ext in VIDEO_TYPE:
            return VIDEO_TYPE[ext]
        return VIDEO_TYPE['mp4']

    def capture_screen_vid(self, x, y, w, h):
        # fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # you can use other codecs as well.
        self.out = cv2.VideoWriter(self.filename, self.get_video_type(), 25, (w, h))
        while not self.stop:
            img = ImageGrab.grab(bbox=(x, y, w+x, h+y))
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            self.out.write(frame)
            # cv2.imshow("frame", frame)
            # key = cv2.waitKey(1)
            # if key == 27:
            #     break

        self.out.release()
        cv2.destroyAllWindows()

    @staticmethod
    def window_enumeration_handler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    def capture_window_into_file(self):
        top_windows = []
        hwnd = None
        name = ""
        x = y = w = h = 0

        win32gui.EnumWindows(self.window_enumeration_handler, top_windows)
        if self.window is not None:
            if self.window == '':
                hwnd = win32gui.GetForegroundWindow()
            else:
                # name = win32gui.GetWindowText(win32gui.GET)
                # hwnd = win32gui.FindWindow(None, name)
                for i in top_windows:
                    print(i)
                    if self.window.lower() in i[1].lower():
                        name = i[1]
                        hwnd = i[0]
                        # wclass = win32gui.GetClassName(hwnd)
                        win32gui.ShowWindow(hwnd, SW_SHOW)
                        break

            win32gui.SetForegroundWindow(hwnd)
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
        else:
            x = 0
            y = 0
            w = GetSystemMetrics(0)
            h = GetSystemMetrics(1)

        print("Window %s:" % win32gui.GetWindowText(hwnd))
        print("\tLocation: (%d, %d)" % (x, y))
        print("\t    Size: (%d, %d)" % (w, h))

        self.capture_screen_vid(x, y, w, h)

    def stop_capturing(self):
        self.stop = True

# def main():
#     scr = ScreenCapture('', 'output2.avi')
#     captureThread = threading.Thread(target=scr.capture_window_into_file, args=())
#     captureThread.start()
#     # scr.capture_window_into_file()
#     sleep(3)
#     # scr.terminate_capturing(captureThread)
#     scr.stop_capturing()
#
#
# if __name__ == "__main__":
#     main()
