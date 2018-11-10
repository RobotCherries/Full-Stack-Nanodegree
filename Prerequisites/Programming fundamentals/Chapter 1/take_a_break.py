import time
import webbrowser

for num in range (1, 4):
    print('Opening video in 5 seconds...')
    timer = time.sleep(5)
    webbrowser.open('http://www.youtube.com/watch?v=dQw4w9WgXcQ')
    num = num + 1
