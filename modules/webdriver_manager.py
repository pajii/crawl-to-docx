from selenium import webdriver
import selenium


class WebdriverManager:

    def __init__(self, path: str):
        # setting
        self.DISPLAY_CHROME_DRIVER = False
        self.DISPLAY_PROCESS = False
        self.PROCESS_LINE_LENGTH = 50
        self.WAIT_TIME = 4

        self.driver = None
        self.chrome_options = webdriver.ChromeOptions()
        self.driver_opened = False
        self.driver_path = path

    # region Start Driver
    def start_driver(self) -> None:
        if not self.driver_opened:
            if not self.DISPLAY_CHROME_DRIVER:
                self.chrome_options.add_argument("headless")

            try:
                self.driver = webdriver.Chrome(self.driver_path, options=self.chrome_options)
            except selenium.common.exceptions.SessionNotCreatedException:
                print("=" * self.PROCESS_LINE_LENGTH)
                print("!! Chrome Driver must be installed in right version.")
                print(f"!! Please check driver in {self.driver_path} than update it\n!!")
                print("!! Check Chrome version in Chrome : chrome://settings/help")
                print("!! Download Chrome : https://chromedriver.chromium.org/downloads")
                print("=" * self.PROCESS_LINE_LENGTH)
                _ = input()
                exit()
            else:
                self.driver_opened = True
                self.driver.implicitly_wait(self.WAIT_TIME)
                if self.DISPLAY_CHROME_DRIVER:
                    self.driver.set_window_size(300, 100)

                if self.DISPLAY_PROCESS:
                    print("   The chrome opened successfully.")
        elif self.DISPLAY_PROCESS:
            print("!  The driver already opened!")

    # endregion

    def quit_driver(self) -> None:
        if self.driver_opened:
            self.driver.quit()
            if self.DISPLAY_PROCESS:
                print("   The chrome closed successfully.")
        elif self.DISPLAY_PROCESS:
            print("   The driver already closed!")