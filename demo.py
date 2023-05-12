import os
import chromedriverhandlar

p1 = os.path.join(os.environ['USERPROFILE'], 'Desktop') + f'\\'
p2 = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

chromedriverhandlar.check_driver(p1, p2)
