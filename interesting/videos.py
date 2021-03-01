import re
from venv import logger
import requests

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


class BeautifulSoup:
    beautiful = {}


def login():
    params = {
        'account': 1923300120120,
        'password': 342221199711263514,
    }
    r = session.post("http://jiaowu.cugbonline.cn/academic/subUserLogin/linkUserSwitch.do", params=params,
                     headers=headers)
    jsessionid = session.cookies.get('JSESSIONID')
    return jsessionid


def get_play_list_info():
    video_list = []
    for i in range(4):
        params = {
            'pageNum': i + 1,
            'url': '/zgProject/front/learncenter/list'
        }
        r = session.get("http://jiaoxue.cugbonline.cn/meol/welcomepage/student/course_list.jsp?r=0.21932704514367884",
                        params, headers)
        soup = BeautifulSoup(r, "html.parser")
        for el in soup.findAll("div", {'onclick': re.compile("skip(.*)")}):
            video_name = el.find("div", {'class': 'clearfix'}).get('title')
            function_name = el.get('onclick')
            video_id = function_name.split(",")[0].split('(')[1].strip()
            progress = el.find("span", {'class': 'baif'}).get_text()
            durationTime = el.find("span", {'class': 'durationTime'}).get_text()
            if progress != '已完成':
                video_list.append({'video_name': video_name, 'video_id': video_id, 'progress': progress,
                                   'durationTime': int(durationTime)})

    logger.info(f"共 {len(video_list)} 个待播放的课程，将依次播放：")
    for video in video_list:
        logger.info(f"{video['video_name']},总时长：{video['durationTime']}秒")
    return video_list
