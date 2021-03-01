import datetime
import requests
import time
import base64
import hmac
import hashlib
import json
import re


class boe_weixin_notice(object):

    def __init__(self):

        requests.packages.urllib3.disable_warnings()
        self.api_name = "boe_weixin_notice_1"
        self.httpUrl = "https://api-csb-broker.boe.com.cn:8086/test"
        self.version = "1.0.0"
        self.ak = "4ac8bc10cfe44d44b4328fefe0853162"
        self.sk = "bzQD26aDKwczf1SLdjZxtX/TvSA="

    @staticmethod
    def __get_seconds():
        # import time
        return lambda: int(round(time.time() * 1000))

    def __getsign1(self):
        # import base64
        # import hmac
        # import hashlib
        params = dict()
        params['_api_name'] = self.api_name
        params['_api_version'] = self.version
        params['_api_access_key'] = self.ak
        params['_api_timestamp'] = str(self.__get_seconds()())
        keys = sorted(params.keys(), reverse=False)
        sign_params = []
        for key in keys:
            if key and key not in "_api_signature":
                sign_params.append("{}={}".format(key, params[key]))
        sign_params_str = '&'.join(sign_params)
        signature = base64.standard_b64encode(
            hmac.new(bytes(self.sk, encoding="utf-8"),
                     bytes(sign_params_str, encoding="utf-8"),
                     hashlib.sha1).digest()).decode("utf-8")
        # params["_api_signature"] = signature
        return {"_api_access_key": self.ak, "_api_signature": signature, "_api_name": self.api_name,
                "_api_version": self.version, "_api_timestamp": str(params["_api_timestamp"])}

    @staticmethod
    def testcimperson():
        return "10286172"

    def __sendmessage(self, sendtouser, sendtitle, sendcontent):
        # import json
        # import requests
        # import datetime
        headers = self.__getsign1()
        headers["Content-Type"] = "application/json"
        headers["sourceType"] = "to"
        print(headers)
        title = sendtitle
        createtime = datetime.datetime.now().strftime("%Y-%m-%d")
        content = sendcontent
        batchtousers = sendtouser
        data = json.dumps({"title": title, "createtime": createtime, "summary": content, "batchToUsers": batchtousers})
        # print(title, batchtousers, content)
        return requests.post(url=self.httpUrl, data=data, headers=headers, verify=False).json()

    def sendmessage(self, sendtouser, sendtitle, sendcontent):
        # wechat_sendcontent = sendcontent
        # wechat_sendtouser = str(sendtouser).replace(",", "|")
        # WeChat(wechat_sendtouser).send_data(wechat_sendcontent)
        sendcontent = str(sendcontent).replace("\n", "")
        self.__sendmessage(sendtouser, sendtitle, sendcontent)
        # if len(sendcontent) > 254:
        #     result = re.findall(r'.{254}', sendcontent)
        #     result.append(sendcontent[(len(result) * 254):])
        #     for i in result:
        #         self.__sendmessage(sendtouser, sendtitle, i)
        # else:
        #     self.__sendmessage(sendtouser, sendtitle, sendcontent)


if __name__ == '__main__':
    content = '小王同学'
    boe_weixin_notice().sendmessage("10286172", "Hello", content)
