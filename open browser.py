import webbrowser as wb

# Change https://example.com with your daily web page
url='https://example.com'
url2='https://example.com'
url3='https://example.com'
url4='https://example.com'
url5='https://example.com'
url6='https://example.com'

chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

wb.register('chrome',None,wb.BackgroundBrowser(chrome_path))

wb.get('chrome').open(url)
wb.get('chrome').open_new_tab(url2)
wb.get('chrome').open_new_tab(url3)
wb.get('chrome').open_new_tab(url4)
wb.get('chrome').open_new_tab(url5)
wb.get('chrome').open_new_tab(url6)