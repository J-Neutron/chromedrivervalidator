import os
import zipfile
import subprocess
import requests
from win32com.client import Dispatch


def get_version_via_com(filename):
    try:
        parser = Dispatch("Scripting.FileSystemObject")
        version = parser.GetFileVersion(filename)
    except Exception as e:
        print('Chrome version checker :', str(e).replace('\n', '').replace('\t', '').strip())
        version = None
    return version

def driver_download_code(chrome_driver_path, chrome_path):
    try:
        chrome_version = get_version_via_com(chrome_path)
        print(f'{chrome_version} = chrome version')
        url_link = 'https://chromedriver.storage.googleapis.com/'
        response = requests.get(url_link)
        position_one = str(response.text).find('<Key>' + chrome_version.split('.')[0] + '.')
        position_two = str(response.text).find('/chromedriver_win32.zip', position_one)
        driver_version = str(response.text)[position_one:position_two].split('/')[0].replace('<Key>', '').strip()
        print(f'{driver_version} = chrome driver version')
        download_url = "https://chromedriver.storage.googleapis.com/" + driver_version + "/chromedriver_win32.zip"
        response = requests.get(download_url)
        data_remove_list = os.listdir(chrome_driver_path)
        if response.status_code == 200:
            open(chrome_driver_path + '\\chromedriver_win32.zip', 'wb').write(response.content)
        # wget.download(download_url, chrome_driver_path)
        if os.path.exists(chrome_driver_path + '\\chromedriver_win32.zip'):
            with zipfile.ZipFile(chrome_driver_path + '\\chromedriver_win32.zip', 'r') as zip_ref:
                zip_ref.extractall(chrome_driver_path)
        data_remove_list.append('chromedriver.exe')
        useless_data_list = list(set(os.listdir(chrome_driver_path)) - set(data_remove_list))
        for i in useless_data_list:
            if 'chromedriver.exe' == i:
                pass
            else:
                os.remove(chrome_driver_path + i)
        print('your chrome browser compatible chrome driver has downloaded')
    except Exception as e:
        print('Driver download error :', str(e))

def check_driver(chrome_driver_path, chrome_path):
    chrome_version = get_version_via_com(chrome_path)
    if 'none' not in str(chrome_version).lower():
        if os.path.exists(chrome_driver_path + 'chromedriver.exe'):
            print(f'{chrome_version} = chrome version')
            chrome_version = chrome_version.split('.')[0] + '.'
            try:
                os.chdir(chrome_driver_path)
                cmd = "chromeDriver --version"
                chrome_driver_version = str(subprocess.check_output(cmd))
                chrome_driver_version = chrome_driver_version.split(' ')[1]
                print(f'{chrome_driver_version} = chrome driver version')
                chrome_driver_version = chrome_driver_version.split('.')[0] + '.'
                if chrome_driver_version == chrome_version:
                    print('chrome browser and chrome driver version are almost same')
                else:
                    os.system(f'taskkill /f /im chromedriver.exe')
                    for i in os.listdir(chrome_driver_path):
                        os.remove(chrome_driver_path + i)
                    driver_download_code(chrome_driver_path, chrome_path)
            except Exception as e:
                print('ChromeDriver is not available :', str(e).replace('\n', '').replace('\t', '').strip())
                os.system(f'taskkill /f /im chromedriver.exe')
                for i in os.listdir(chrome_driver_path):
                    os.remove(chrome_driver_path + i)
                driver_download_code(chrome_driver_path, chrome_path)
        elif os.path.exists(chrome_driver_path):
            driver_download_code(chrome_driver_path, chrome_path)
        else:
            os.makedirs(chrome_driver_path)
            driver_download_code(chrome_driver_path, chrome_path)
    else:
        print('Invalid "chrome.exe" path')
