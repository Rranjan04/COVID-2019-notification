from plyer import notification
import requests
from bs4 import BeautifulSoup, Comment
import time


def notify_me(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=15
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    while True:
        htmlData = getData("https://www.mohfw.gov.in/")

        soup = BeautifulSoup(htmlData, 'html.parser')
        for table in soup.find_all('table'):
            comment = table.find(text=lambda text: isinstance(text, Comment))
            commentSoup = BeautifulSoup(comment, 'html.parser')
            myDataStr = " "
            for tr in commentSoup.find_all('tr'):
                myDataStr += tr.get_text()
            myDataStr = myDataStr[2:]
            item_list = (myDataStr.split("\n\n"))
        states = ['Gujarat', 'Tamil Nadu', 'Delhi']
        for item in item_list[0:35]:
            dataList = item.split("\n")
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of COVID-19'
                nText = f"State: {dataList[1]} \nTotal Active Cases: {dataList[2]}\nTotal Discharged:{dataList[3]}\nTotal Deaths:{dataList[4]}\n"
                notify_me(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)
