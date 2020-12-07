from selenium import webdriver
import pandas as pd

url = 'https://www.youtube.com/channel/UC8tgRQ7DOzAbn9L7zDL8mLg'

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(url)

# document.querySelector("#meta > h3")
# document.querySelector("#video-title")
# document.querySelector("#metadata-line > span:nth-child(1)")
# document.querySelector("#metadata-line > span:nth-child(2)")

driver.implicitly_wait(5)

videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')

vid_list = []

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    dates = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    print(title, views, dates)

    vid_item = {
        'title': title,
        'views': views,
        'dates': dates
    }

    vid_list.append(vid_item)

df = pd.DataFrame(vid_list)
print(df)


