from test_case.myunit import StartEnd
from pubilc.pages.business_functions.computer_office import ComputerOffice
from pubilc.pages.page_elements.computer_office_page import ComputerOfficePage
from data.expected_computer_office import ExpectedComputerOffice
from pubilc.tools.get_courses import GetCourses
import os
import sys
# 获取根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将根目录添加到path中
sys.path.append(BASE_DIR)
class TestComputerOffice(StartEnd,ComputerOfficePage,ExpectedComputerOffice):
    def test_computer_primary(self):
        ComputerOffice(self.driver).computer_primary()
        courses = GetCourses(self.driver).get_courses()
        print(courses)
        print(self.expect_computer_primary_courses)
        self.assertEqual(courses,self.expect_computer_primary_courses)

    def test_five_stroke(self):
        ComputerOffice(self.driver).five_stroke()
        courses = GetCourses(self.driver).get_courses()
        print(courses)
        print(self.expect_five_stroke_courses)
        self.assertEqual(courses, self.expect_five_stroke_courses)
    def test_word(self):
        ComputerOffice(self.driver).word()
        courses = GetCourses(self.driver).get_courses()
        print(courses)
        print(self.expect_word_courses)
        self.assertEqual(courses, self.expect_word_courses)

    def test_ppt(self):
        ComputerOffice(self.driver).ppt()
        courses = GetCourses(self.driver).get_courses()
        print(courses)
        print(self.expect_ppt_courses)
        self.assertEqual(courses, self.expect_ppt_courses)

    def test_excel_base(self):
        ComputerOffice(self.driver).excel_base()
        courses = GetCourses(self.driver).get_courses()
        print(courses)
        print(self.expect_excel_base_courses)
        self.assertEqual(courses, self.expect_excel_base_courses)

    def test_excel_progress(self):
        ComputerOffice(self.driver).excel_progress()
        courses = GetCourses(self.driver).get_courses()
        print(courses)
        print(self.expect_excel_progress_courses)
        self.assertEqual(courses, self.expect_excel_progress_courses)

    def test_wps(self):
        ComputerOffice(self.driver).wps()
        courses = GetCourses(self.driver).get_courses()
        print(courses)
        print(self.expect_wps_courses)
        self.assertEqual(courses, self.expect_wps_courses)

    def test_type_rank_combined(self):
        ComputerOffice(self.driver).type_rank_combined()
        courses = GetCourses(self.driver).get_courses()
        self.assertEqual(courses, self.expect_type_rank_combined_courses)

    def test_type_rank_sort_combined_(self):
        ComputerOffice(self.driver).type_rank_sort_combined()
        courses = GetCourses(self.driver).get_courses()
        self.assertEqual(courses, self.expect_type_rank_sort_combined_courses)
