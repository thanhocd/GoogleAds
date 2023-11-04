from seleniumbase import SB
import time
# import json
# from selenium.webdriver.common.keys import Keys
import re
# import html
# import requests

from email_google import EmailGoogleAccess
from keyworkCPC import KeywordCPC
from BeeModule import BeeHelper


class MainClass:
    def __init__(self):
        self.sb_config = {
            "uc": True,
            "device_metrics": None,
            "is_mobile": None,
            "agent": None,
        }
        self.sb = None
        self.email_google = None

    def clean_html_tags(self, text):
        cleaned_text = re.sub(r"<.*?>", "", text)
        cleaned_text = cleaned_text.replace("\n", "").strip()
        return cleaned_text

    def run(self):
        try:
            with SB(
                uc=self.sb_config["uc"],
                maximize=True,
                device_metrics=self.sb_config["device_metrics"],
                is_mobile=self.sb_config["is_mobile"],
                agent=self.sb_config["agent"],
            ) as self.sb:
                self.email_google = EmailGoogleAccess(self.sb).access_google_ads()
                final = []
                while True:
                    final = KeywordCPC(self.sb, self.email_google).keyword_cpc()

                    myhelper = BeeHelper()
                # #data test
                    url = "https://dev92.beetech.one/post/index.php"
                    response = myhelper.push_everything(url, final)
                    print(response.json())
                    time.sleep(60)

        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    main_instance = MainClass()
    main_instance.run()
