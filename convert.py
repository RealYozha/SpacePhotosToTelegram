def change_splitter(istr: str, curr: str, next: str):
    return next.join(str.split(istr, curr))


def get_epic_url_v2(_,i:int):
    a=str.split(_[i]["date"]," ")[0]
    b=change_splitter(a,"-","/")
    c=_[i]["image"]
    return f"https://api.nasa.gov/EPIC/archive/natural/{b}/png/{c}.png"