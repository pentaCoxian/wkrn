import scrape
from bs4 import BeautifulSoup

# Setup vars
offset = 2
target = offset + 2
target = str(target).zfill(2)

# debug set by manual
# target='04'

# Check var eq?
print('Target No. is:{}'.format(target))
print("var == str: {}".format(str(target) == '04'))
print("str+var == str: {}".format(str('ctl00_ContentPlaceHolder1_grv_course_ct{}_lbl_title_j'.format(target)) == 'ctl00_ContentPlaceHolder1_grv_course_ctl04_lbl_title_j'))
print("feching data from site...")

# Get data from site
table = scrape.get_courses()
soup = BeautifulSoup(table,'lxml')
courses = soup.find('tr').find_all('tr')

# Search from data
print("\n")
print('Search 1: '+'ctl00_ContentPlaceHolder1_grv_course_ctl{}_lbl_title_j'.format(target))
print('Search 2: '+'ctl00_ContentPlaceHolder1_grv_course_ctl04_lbl_title_j')
print('------RESULT-------')
print(soup.find('span',{'id':'ctl00_ContentPlaceHolder1_grv_course_ct{}_lbl_title_j'.format(target)}))
print(soup.find('span',{"id":'ctl00_ContentPlaceHolder1_grv_course_ctl04_lbl_title_j'}))


