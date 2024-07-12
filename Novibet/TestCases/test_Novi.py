from BaseClass import BaseClass
from BusinessObjects.NoviBusinessObject import NoviBusinessObject

class TestSoccerEvents(BaseClass):

    def test_selectcategoryandsport(self):
        categoryandsport = NoviBusinessObject(self.driver)

        categoryandsport.buttonCookies()
        categoryandsport.buttonX()
        categoryandsport.CategorySelection("Live Στοίχημα")
        categoryandsport.SelectProgramm("Live πρόγραμμα")
        categoryandsport.SelectDropDown("Όλοι οι αγώνες")
        categoryandsport.SportSelectiondp("Ποδόσφαιρο")