from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import EdgeOptions
import datetime
from typing import List
from dataclasses import dataclass

HOME_PAGE       = "https://gpss3.tipo.gov.tw"
PAT_SEARCH      = '//*[@id="header"]/div/ul/li[2]/a'
ADV_PAT_SEARCH  = '//*[@id="header"]/div/ul/li[2]/ul/li[3]/a'
SETTING         = '/html/body/form/div[1]/div/div/table/tbody/tr[1]/td/a[1]'
SETTING_FIELD   = '/html/body/form/div[1]/div/div[4]/div[2]/table/tbody/tr/td[{}]/table/tbody/tr[{}]/td/label/input'
SETTING_INDEX   = [(1, 2), (1, 4), (2, 3), (3, 2), (4, 1), (5, 5)]  
SETTING_DISPLAY = '/html/body/form/div[1]/div/div[6]/div[2]/table/tbody/tr/td/label[5]/input'    
SETTING_APPLY   = '/html/body/form/div[1]/div/div[2]/input[2]'   
SETTING_EXIT    = '/html/body/form/div[1]/div/div[2]/input[1]'
YEAR            = '/html/body/form/div[1]/div/div/table/tbody/tr[2]/td[1]/table/tbody/tr/td[3]/table/tbody/tr/td[1]/select/option[{}]'
SEARCH_BOX      = '//*[@id="focus_default"]'
SEARCH          = '/html/body/form/div[1]/div/div/table/tbody/tr[10]/td/input[1]'
SEARCH_EXIT     = '/html/body/form/div[1]/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td[1]/table/tbody/tr/td[5]/input[2]'
NOTFOUND_MSG    = '/html/body/form/div[1]'
RESULT_NUM      = '/html/body/form/div[1]/div/table/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/font[1]'
NEXT_PAGE       = '/html/body/form/div[1]/div/table/tbody/tr/td[3]/table/tbody/tr[5]/td/input'

PUB_NUMBER      = '/html/body/form/div[1]/div/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[{}]/td[4]/a'
TITLE           = '/html/body/form/div[1]/div/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[{}]/td[5]/div'
PUB_DATE        = '/html/body/form/div[1]/div/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[{}]/td[3]'
IPC             = '/html/body/form/div[1]/div/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[{}]/td[7]'
MAIN_IMG        = '/html/body/form/div[1]/div/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[{}]/td[2]/img'
CONTENT         = '/html/body/form/div[1]/div/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[{}]/td[6]/div'
CONTENT_FOLDED  = '//*[@id="rmjs-{}"]'


@dataclass
class Patent:
    pid: str
    url: str
    title: str
    date: datetime.date
    ipc: List[str]
    image_url: str
    content: str


options = EdgeOptions() 
options.add_argument('log-level=3')
options.add_argument('--headless=new')
driver = webdriver.Edge(options=options)
driver.get(HOME_PAGE)

def Q(xpath: str, default = None):
    try:
        return driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return None if not default else Q(default)

def C(xpath: str):
    ele = Q(xpath)
    ele.click()
    return ele

# Head to searching page
action = ActionChains(driver)
action.move_to_element(Q(PAT_SEARCH)).click(Q(ADV_PAT_SEARCH)).perform()

# Set the displayed content.
C(SETTING)
action.reset_actions()
for index in SETTING_INDEX:
    action.click(Q(SETTING_FIELD.format(*index)))
action.click(Q(SETTING_DISPLAY)).click(Q(SETTING_APPLY)).perform()
C(SETTING_EXIT)

def get_search_token():
    raise NotImplementedError()


#================================================================================================

def get_patents(date_from: datetime.date, date_to: datetime.date = None, ipc = ..., limit = 50):
    assert not date_to or date_from <= date_to, "Starting date must prior to ending date." 
    newest_year = int(Q(YEAR.format(2)).text)
    assert date_from.year <= newest_year and (not date_to or date_to.year <= newest_year), \
        f"Invalid year. Can't accept year after {newest_year}."
    
    Q(SEARCH_BOX).send_keys(get_search_token(date_from, date_to, ipc))
    C(SEARCH)

    # No matching result.
    ele = Q(NOTFOUND_MSG)
    if not ele or ele.get_attribute("class") == "msgfmt": return 0, []
    
    total_num = int(Q(RESULT_NUM).text.replace(',', ''))
    def patent_gen():     
        try:   
            per = 50
            for i in range(min(total_num, limit) if limit > 0 else total_num):
                index = i % per + 2
                yield Patent(
                    pid         = Q(PUB_NUMBER.format(index)).text,
                    url         = Q(PUB_NUMBER.format(index)).get_attribute("href"),
                    title       = Q(TITLE).text,
                    date        = Q(PUB_DATE.format(index)).text,
                    ipc         = Q(IPC.format(index)).text,
                    image_url   = Q(MAIN_IMG.format(index)).get_attribute("src"),
                    content     = Q(CONTENT_FOLDED.format(index-1), CONTENT.format(index)).text,
                )

                if index == per + 1:
                    try:
                        Q(NEXT_PAGE).click()
                    except NoSuchElementException:
                        return
        finally:
            C(SEARCH_EXIT)

    return total_num, patent_gen