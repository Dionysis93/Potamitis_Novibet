from selenium.webdriver.common.by import By

class LiveSchedulePage:
    def __init__(self, driver):
        self.driver = driver

    def landInPage(self):
        self.driver.find_element(By.XPATH,"//a[@title='Live Στοίχημα']").click()
        self.driver.find_element(By.XPATH,"//div[@class='headerSubmenu u-flex u-flexYCenter']//a[@title='Live πρόγραμμα']").click()


    def get_live_schedule_matches(self):
        matches = self.driver.find_elements(By.XPATH, "//div[@class='liveSchedule_content u-flex u-flexYCenter']")
        schedule = {}
        for index, match in enumerate(matches):
            match_key = f"match-{index}"
            schedule[match_key] = match
        return schedule

    def match_exists(self, match_key):
        matches = self.driver.find_elements(By.XPATH, "//div[@class='liveSchedule_content u-flex u-flexYCenter']")
        for index, match in enumerate(matches):
            current_match_key = f"match-{index}"
            if current_match_key == match_key:
                return True
        return False

