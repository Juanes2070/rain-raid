import Window
import multiprocessing

if __name__ == '__main__':
    multiprocessing.freeze_support()
    window = Window.MainWindow()
    window.start()
