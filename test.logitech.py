import ctypes

from win32gui import GetCursorPos  # conda install pywin32

try:
    driver = ctypes.CDLL('logitech.driver.dll')
    # 该驱动每个进程可打开一个实例
    ok = driver.device_open() == 1
    if not ok:
        print('Error, GHUB or LGS driver not found')
except FileNotFoundError:
    print('Error, DLL file not found')


class GHub:

    class mouse:

        """
        code: 1:左键, 2:中键, 3:右键
        """

        @staticmethod
        def press(code):
            if not ok:
                return
            driver.mouse_down(code)

        @staticmethod
        def release(code):
            if not ok:
                return
            driver.mouse_up(code)

        @staticmethod
        def click(code):
            if not ok:
                return
            driver.mouse_down(code)
            driver.mouse_up(code)

        @staticmethod
        def scroll(a):
            """
            a:没搞明白
            """
            if not ok:
                return
            driver.scroll(a)

        @staticmethod
        def move(x, y, absolute=False):
            """
            x: 水平移动的方向和距离, 正数向右, 负数向左
            y: 垂直移动的方向和距离
            absolute: 是否绝对移动, 是:跳到水平x和垂直y的位置, 否:水平跳x距离垂直跳y距离
            """
            if not ok:
                return
            if x == 0 and y == 0:
                return
            mx, my = x, y
            if absolute:
                ox, oy = GetCursorPos()
                mx = x - ox
                my = y - oy
            driver.moveR(mx, my, True)

    class keyboard:

        """
        键盘按键函数中，传入的参数采用的是键盘按键对应的键码
        code: 'a'-'z':A键-Z键, '0'-'9':0-9, 其他的没猜出来
        """

        @staticmethod
        def press(code):

            if not ok:
                return
            driver.key_down(code)

        @staticmethod
        def release(code):
            if not ok:
                return
            driver.key_up(code)

        @staticmethod
        def click(code):
            if not ok:
                return
            driver.key_down(code)
            driver.key_up(code)
