from pubilc.pages.business_functions.login import Login
from pubilc.pages.page_elements.computer_office_page import ComputerOfficePage
from pubilc.pages.page_elements.home_page import HomePage
from pubilc.pages.business_functions.Base import Base
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.common.by import By
import time

class ComputerOffice(Base,ComputerOfficePage,HomePage):
    def computer_primary(self):
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT,self.computer_office_loc).click()
                    self.driver.find_element(By.LINK_TEXT,self.computer_primary_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)


    def five_stroke(self):
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.computer_office_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.five_stroke_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)
    def word(self):
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.computer_office_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.word_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)

    def ppt(self):
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.computer_office_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.ppt_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)
    def excel_base(self):
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.computer_office_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.excel_base_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)
    def excel_progress(self):
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.computer_office_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.excel_progress_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)
    def wps(self):
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.computer_office_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.wps_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)
    def type_rank_combined(self):
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.computer_office_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.computer_primary_loc).click()
                    self.driver.find_element(By.LINK_TEXT,self.progress_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    self.driver.refresh()
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)
    def type_rank_sort_combined(self):
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.computer_office_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.excel_progress_loc).click()
                    self.driver.find_element(By.LINK_TEXT,self.senior_loc).click()
                    self.driver.find_element(By.LINK_TEXT,self.visits_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)

