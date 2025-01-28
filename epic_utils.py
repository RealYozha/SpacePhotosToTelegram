import datetime


def get_epic_url_v4(data, number: int):
    imgdata = data[number]
    datetimeobj = datetime.datetime.strptime(imgdata["date"], "%Y-%m-%d %H:%M:%S")
    date = datetimeobj.strftime("%Y/%m/%d")
    img = imgdata["image"]
    return f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{img}.png"
