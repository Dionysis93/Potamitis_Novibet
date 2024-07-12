from selenium.webdriver.common.by import  By

class NoviPageObject:

    def __init__(self,driver):
        self.driver = driver

    btnCookies = (By.XPATH, "//div[@class='u-flexRow u-flexXCenter']//button[contains(text(),'Εντάξει')]")
    btnClose = (By.XPATH,"//div[@id='cdk-overlay-0']//div[@class='registerOrLogin_closeButton u-flex u-flexCenter u-clickable']//cm-icon[@name='close']")


    def btnCookies(self):
        self.find_element(*NoviPageObject.btnCookies).click()

    def btnClose(self):
        self.find_element(*NoviPageObject.btnClose).click()

    def selectCategory(self,category):
        self.driver.find_element(By.XPATH,"//a[@title='"+category+"']").click()

    def selectProgramm(self,programm):
        self.driver.find_element(By.XPATH,"//div[@class='headerSubmenu u-flex u-flexYCenter']//a[@title='"+programm+"']")

    def selectDropdown(self,dropdown):
        self.driver.find_element(By.XPATH,"//div[@class='scheduleFilters u-flex u-flexYCenter']//span[contains(text(),'"+dropdown+"')]")

    def selectSportdp(self,sport):
        self.driver.find_element(By.XPATH,"//div[@class='cdk-overlay-pane']//span[contains(text(),'"+sport+"')]")
