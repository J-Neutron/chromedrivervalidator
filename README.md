# chromedriverhandlar

A simple Python library that check, update or download chrome driver.

## Installation

You can install chromedriverhandlar using pip:

```bash
pip install chromedriverhandlar
```

## How to use

```bash
import chromedriverhandlar

driver_path = os.path.join(os.environ['USERPROFILE'], 'Desktop') + f'\\' # Provide downloaded chrome driver path 
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' # Provide installed chrome browser path

chromedriverhandlar.check_driver(driver_path, chrome_path)
```
