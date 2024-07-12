from selenium.webdriver.common.by import By

class LiveFootballPage:
    def __init__(self, driver):
        self.driver = driver

    def get_matches_live_programm(self):
        self.driver.find_element(By.XPATH,"//div[@class='headerSubmenu u-flex u-flexYCenter']//a[@title='Live πρόγραμμα']").click()
        table = self.driver.find_element(By.XPATH,"//div[@class='liveSchedule_content u-flex u-flexYCenter']")
        rows = table.find_elements(By.XPATH,"//cm-card-body[@class='scheduleView u-cmp'//*]")
        data = []
        for row in rows:
            cells = row.find_elements(By.XPATH,".//sb-event-default-list-item")
            row_data = [cell.text for cell in cells]
            data.append(row_data)
        return data

    def get_matches_live_bet(self):
        self.driver.find_element(By.XPATH,"//a[@title='Live Στοίχημα']").click()
        lb_table = self.driver.find_element(By.XPATH,"//div[@class='inPlay_main u-flexColumn u-fullWidth ng-tns-c5475771864-753']")
        lb_rows = lb_table.find_elements(By.XPATH,"//cm-card-body[@class='inPlayEvents_competition u-cmp ng-star-inserted'//*]")
        lb_data = []
        for lb_row in lb_rows:
            lb_cells = lb_row.find_elements(By.XPATH,".//sb-event-default-list-item-live")
            lb_row_data = [lb_cell.text for lb_cell in lb_cells]
            lb_data.append(lb_row_data)
        return lb_data
