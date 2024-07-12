from PageObjects.NoviPageObject import NoviPageObject

class NoviBusinessObject:

    def __init__(self,driver):
        self.driver=driver
        self.NoviPageObject = NoviPageObject(self.driver)

    def buttonCookies(self):
        self.NoviPageObject.btnCookies

    def buttonX(self):
        self.NoviPageObject.btnClose

    def CategorySelection(self,category):
        self.NoviPageObject.selectCategory(category)

    def SelectProgramm(self,programm):
        self.NoviPageObject.selectProgramm(programm)

    def SelectDropDown(self,dropdown):
        self.NoviPageObject.selectDropdown(dropdown)

    def SportSelectiondp(self,sport):
        self.NoviPageObject.selectSportdp(sport)