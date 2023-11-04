from seleniumbase import SB
from seleniumbase import Driver
import time

class EmailGoogleAccess:
    def __init__(self, sb):
        self.sb = sb

    def access_google_ads(self):
        email = {
            "email": "nguyendiphong159@gmail.com",
            "pass_login": "Nguyenngocphong3121999",
        }
        try:
            print("Đang vào Google Ads")
            self.sb.open("https://ads.google.com/")
        except Exception as e:
            return 'Error occurred : ' + str(e)
        try:
            print("Trỏ vào ô Đăng nhập")
            self.sb.click('//*[@id="header-topbar"]/div/div[3]/div/div[4]/a', timeout=5)
        except Exception as click_error:
            # Xử lý lỗi khi không thể nhấn vào nút "Next"
            print("Error while clicking 'Next' button:", click_error)
            # Thêm các hành động xử lý lỗi ở đây
            return 'Click error: ' + str(click_error)

        #Nhập email
        self.sb.type('input[type="email"]', email["email"], timeout=5)
        try:
            print(f"Đã nhập Email thành công,   Next......")
            self.sb.click('button:contains("Next")', timeout=15, delay=1)
        except Exception as click_error:
            # Xử lý lỗi khi không thể nhấn vào nút "Next"
            print("Error while clicking 'Next' button:", click_error)
            # Thêm các hành động xử lý lỗi ở đây
            return 'Click error: ' + str(click_error)
        time.sleep(10)
        #Nhập password
        self.sb.type('input[type="password"]', email["pass_login"], timeout=10, )

        try:
            print("Đã nhập Password thành công,   Next.....")
            self.sb.click('button:contains("Next")', timeout=20, delay=1)
        except Exception as click_error:
            # Xử lý lỗi khi không thể nhấn vào nút "Next"
            print("Error while clicking 'Next' button:", click_error)
            # Thêm các hành động xử lý lỗi ở đây
            return 'Click error: ' + str(click_error)
        time.sleep(10)
        try:
            self.sb.wait_for_element_absent('button:contains("Next")', timeout=5)
            time.sleep(15)
        except Exception as click_error:
            # Xử lý lỗi khi không thể nhấn vào nút "Next"
            print("Error while clicking 'Next' button:", click_error)
            # Thêm các hành động xử lý lỗi ở đây
            return 'Click error: ' + str(click_error)
        try:
            self.sb.click('//*[@id="navigation.tools"]/div/a/rail-item', timeout=15, delay=1)
        except Exception as click_error:
            # Xử lý lỗi khi không thể nhấn vào nút "Next"
            print("Error while clicking 'Next' button:", click_error)
            # Thêm các hành động xử lý lỗi ở đây
            return 'Click error: ' + str(click_error)
        try:
            self.sb.click(
                "/html/body/div[1]/root/div/div[1]/div[2]/div/div[3]/div/div/awsm-child-content/div[1]/div[2]/kp-root/div/div/"
                "view-loader[2]/splash-view/div/div/div[1]/splash-cards/div/div[1]",
                timeout=15,
                delay=1,
            )
        except Exception as click_error:
            # Xử lý lỗi khi không thể nhấn vào nút "Next"
            print("Error while clicking 'Next' button:", click_error)
            # Thêm các hành động xử lý lỗi ở đây
            return 'Click error: ' + str(click_error)