# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:38:34 2022

@author: ACER
"""

### completed 

#Directory 

import os 
os.chdir(r"C:\Users\ACER\Documents\Python\jupuyter\crash course in py")

## Import packages

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import itertools




"""
_______________________________________________________________________________
Launch chrome 
_______________________________________________________________________________
"""
url = 'https://portal.nysc.org.ng/nysc1/CheckInstitutionCoursesPCMs.aspx' 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
wait = ui.WebDriverWait(driver, 10)

"""
_______________________________________________________________________________
_______________________________________________________________________________
"""







"""
_______________________________________________________________________________
Get Batch and Institution
_______________________________________________________________________________
"""
batch = Select(driver.find_element(By.ID, value = 'ctl00_ContentPlaceHolder1_cboBatch'))
time.sleep(1)
batchs = [option.text for option in batch.options]

BATCH = []
INSTITUTION = []

for index, bat in enumerate(batchs):
    option = wait.until(lambda driver: driver.find_element(By.ID, value = 'ctl00_ContentPlaceHolder1_cboBatch'))
    
    #get the institution 
    institution = Select(driver.find_element(By.ID, value = 'ctl00_ContentPlaceHolder1_cbo1stMostInstitutionType'))
    time.sleep(1)
    
    inst = [option.text for option in institution.options]
    
    for index, ins in enumerate(inst):
        BATCH.append(bat)
        INSTITUTION.append(ins)
"""
_______________________________________________________________________________
_______________________________________________________________________________

"""







"""
_______________________________________________________________________________
Remove select 
_______________________________________________________________________________
"""
BATCH = np.array(BATCH)
INSTITUTION = np.array(INSTITUTION)
INSTITUTION = INSTITUTION.reshape(len(BATCH), 1)
BATCH = BATCH.reshape(len(BATCH), 1)

opt = np.concatenate((BATCH, INSTITUTION), axis=1)
opt = pd.DataFrame(opt, columns=("batch", "inst_type")) 

opt = opt[opt.batch != "Select..."]
opt = opt[opt.inst_type != "Select..."] 
new_batch = opt['batch'].tolist()
new_inst = opt['inst_type'].tolist()
"""
_______________________________________________________________________________
_______________________________________________________________________________
"""


    
    
    
    
    



"""
_______________________________________________________________________________
Get School names
_______________________________________________________________________________
"""

BATCH = []
INSTITUTION = [] 
SCHOOL = []
for b, i in zip(new_batch, new_inst):
    batch = Select(driver.find_element(By.ID, value = 'ctl00_ContentPlaceHolder1_cboBatch'))
    batch.select_by_visible_text("{}".format(b))  
    driver.implicitly_wait(30)
    institution = Select(driver.find_element(By.ID, value ='ctl00_ContentPlaceHolder1_cbo1stMostInstitutionType'))
    institution.select_by_visible_text("{}".format(i)) 
    driver.implicitly_wait(30)
    university = Select(driver.find_element(By.ID, value = 'ctl00_ContentPlaceHolder1_cboFirstInstitution'))
    driver.implicitly_wait(30)
    uni = [option.text for option in university.options] 
    for index, un in enumerate(uni):
        time.sleep(1)        
        SCHOOL.append(un)
        BATCH.append(b)
        INSTITUTION.append(i)       
  
        
"""
_______________________________________________________________________________
_______________________________________________________________________________
"""
 


       

"""
_______________________________________________________________________________
Remove Select
_______________________________________________________________________________
"""

BATCH2 = np.array(BATCH)
INSTITUTION2 = np.array(INSTITUTION)
SCHOOL2 = np.array(SCHOOL)

INSTITUTION2 = INSTITUTION2.reshape(len(BATCH), 1)
BATCH2 = BATCH2.reshape(len(BATCH), 1) 
SCHOOL2 = SCHOOL2.reshape(len(BATCH), 1)

opt = np.concatenate((BATCH2, INSTITUTION2, SCHOOL2), axis=1)
opt = pd.DataFrame(opt, columns=("batch", "inst_type", "school")) 

opt = opt[opt.batch != "Select..."]
opt = opt[opt.inst_type != "Select..."]
opt =  opt[opt.school != "Select..."]

new_batch2 = opt['batch'].tolist()
new_inst2 = opt['inst_type'].tolist()
new_school2 = opt['school'].tolist()
"""
_______________________________________________________________________________
_______________________________________________________________________________
"""





"""
_______________________________________________________________________________
Get Courses
_______________________________________________________________________________
"""
BATCH = []
INSTITUTION = [] 
SCHOOL = []
COURSES = []

for b, i, s in zip(new_batch2, new_inst2, new_school2):
    batch = Select(driver.find_element(By.ID, value = 'ctl00_ContentPlaceHolder1_cboBatch'))
    batch.select_by_visible_text("{}".format(b))  
    driver.implicitly_wait(30)
    institution = Select(driver.find_element(By.ID, value = 'ctl00_ContentPlaceHolder1_cbo1stMostInstitutionType'))
    institution.select_by_visible_text("{}".format(i)) 
    driver.implicitly_wait(30)
    university = Select(driver.find_element(By.ID, value = 'ctl00_ContentPlaceHolder1_cboFirstInstitution'))
    university.select_by_visible_text("{}".format(s)) 
    driver.implicitly_wait(30)
    
    courses = Select(driver.find_element(by = By.ID, value = 'ctl00_ContentPlaceHolder1_cboCourses'))
    # get courses    
    course = [option.text for option in courses.options]  
    for index, co in enumerate(course):
        time.sleep(1)
        COURSES.append(co)
        SCHOOL.append(s)
        BATCH.append(b)
        INSTITUTION.append(i)
        
"""
_______________________________________________________________________________
_______________________________________________________________________________

"""




"""
_______________________________________________________________________________
Remove Select
_______________________________________________________________________________


"""

BATCH3 = np.array(BATCH)
INSTITUTION3 = np.array(INSTITUTION)
SCHOOL3 = np.array(SCHOOL)
COURSES3 = np.array(COURSES)

INSTITUTION3 = INSTITUTION3.reshape(len(BATCH), 1)
BATCH3 = BATCH3.reshape(len(BATCH), 1)
SCHOOL3 = SCHOOL3.reshape(len(BATCH), 1)
COURSES3 = COURSES3.reshape(len(BATCH), 1)

opt = np.concatenate((BATCH3, INSTITUTION3, SCHOOL3, COURSES3), axis=1)
opt = pd.DataFrame(opt, columns=("batch", "inst_type", "school", "course")) 

opt = opt[opt.batch != "Select..."]
opt = opt[opt.inst_type != "Select..."]
opt =  opt[opt.school != "Select..."]
opt = opt[opt.course != "Select..."]

new_batch3 = opt['batch'].tolist()
new_inst3 = opt['inst_type'].tolist()
new_school3 = opt['school'].tolist()
new_course3 = opt['course'].tolist()


"""
_______________________________________________________________________________
_______________________________________________________________________________
"""



"""
_______________________________________________________________________________
Get all data 
_______________________________________________________________________________
"""

sno = []
surname = []
onames = []
gender = []
course = []
status = []
BATCH = {}
INSTITUTION = {} 
SCHOOL = {}
COURSE = {}


for b, i, s, co in zip(new_batch3, new_inst3, new_school3, new_course3):
        BATCH["{}".format(b)] = []
        INSTITUTION[f"{i}_{b}"] = []
        SCHOOL[f"{s}_{b}"] = []
        COURSE[f"{co}_{b}"] = []
        
        

for b, p, s, co in zip(new_batch3, new_inst3, new_school3, new_course3):
    batch = Select(driver.find_element(By.ID, value = 'ctl00_ContentPlaceHolder1_cboBatch'))
    batch.select_by_visible_text("{}".format(b))  
    driver.implicitly_wait(30)
    institution = Select(driver.find_element(By.ID, value ='ctl00_ContentPlaceHolder1_cbo1stMostInstitutionType'))
    institution.select_by_visible_text("{}".format(p)) 
    driver.implicitly_wait(30)
    university = Select(driver.find_element(By.ID, value = 'ctl00_ContentPlaceHolder1_cboFirstInstitution'))
    university.select_by_visible_text("{}".format(s)) 
    driver.implicitly_wait(30)
    courses = Select(driver.find_element(by = By.ID, value = 'ctl00_ContentPlaceHolder1_cboCourses'))
    courses.select_by_visible_text("{}".format(co))
    driver.implicitly_wait(10)
    btn = driver.find_element(by = By.ID, value = 'ctl00_ContentPlaceHolder1_btnExtract')
    btn.click()
    
    try:
        show = Select(driver.find_element(by = By.NAME, value = 'GdvPCMCourses_length'))
        show.select_by_value('100')
        driver.implicitly_wait(10)
    except NoSuchElementException as e:
        pass
        #print('Tag was not found, try another combination')
 
    try:
        div = driver.find_element(By.ID, "GdvPCMCourses_paginate")  
        a = div.find_elements(By.TAG_NAME, "a")
    
    
        keep_running = True
        for i in a[1:-1]:
            cols = driver.find_elements(by = By.XPATH, value = "//table/tbody/tr/td[1]")
            col1 = driver.find_elements(by = By.XPATH, value = "//table/tbody/tr/td[2]")
            col2 = driver.find_elements(by = By.XPATH, value = "//table/tbody/tr/td[3]")
            col3 = driver.find_elements(by = By.XPATH, value = "//table/tbody/tr/td[4]")
            col4 = driver.find_elements(by = By.XPATH, value = "//table/tbody/tr/td[5]")
            col5 = driver.find_elements(by = By.XPATH, value = "//table/tbody/tr/td[6]")

            sno.append([s.text for s in cols]) 
            surname.append([s.text for s in col1])
            onames.append([s.text for s in col2])
            gender.append([s.text for s in col3])
            course.append([s.text for s in col4])
            status.append([s.text for s in col5])
            
            BATCH["{}".format(b)].append([s.text for s in cols])
            SCHOOL[f"{s}_{b}"].append([s.text for s in cols])
            #SCHOOL[f"{s}"].append([s.text for s in cols])
            INSTITUTION[f"{p}_{b}"].append([s.text for s in cols])
            #INSTITUTION[f"{p}"].append([s.text for s in cols])
            
            
            driver.find_element(By.LINK_TEXT, "Next").click()
            driver.implicitly_wait(10)
    except:
        pass
        

"""
____________________________________________________________________________

transform into dataframe
____________________________________________________________________________
"""

sno = [element for sub in sno for element in sub]
surname = [element for sub in surname for element in sub] 
onames = [element for sub in onames for element in sub] 
gender = [element for sub in gender for element in sub]
course= [element for sub in course for element in sub]
status= [element for sub in status for element in sub]    

sno = np.array(sno)
surname = np.array(surname)
onames = np.array(onames)
gender = np.array(gender)
course = np.array(course)
status = np.array(status)

sno = sno.reshape(len(sno), 1)
surname = surname.reshape(len(surname), 1)
onames = onames.reshape(len(onames), 1)
gender = gender.reshape(len(gender), 1)
course = course.reshape(len(course), 1)
status = status.reshape(len(status), 1)


BATCH2 = []

INSTITUTION2 = [] 
SCHOOL2 = []

    
for i in BATCH:
    BATCH['{}'.format(i)] = [element for sub in BATCH['{}'.format(i)] for element in sub]

for i in SCHOOL:
    SCHOOL['{}'.format(i)] = [element for sub in SCHOOL['{}'.format(i)] for element in sub]

for i in INSTITUTION:
    INSTITUTION['{}'.format(i)] = [element for sub in INSTITUTION['{}'.format(i)] for element in sub]


for b in BATCH:
    BATCH2.append(np.repeat(b, len(BATCH["{}".format(b)])))
    
for b in INSTITUTION:
    INSTITUTION2.append(np.repeat(b, len(INSTITUTION["{}".format(b)])))
    
for b in SCHOOL:
    SCHOOL2.append(np.repeat(b, len(SCHOOL["{}".format(b)])))
    
    
INSTITUTION = [element for sub in INSTITUTION2 for element in sub]
BATCH = [element for sub in BATCH2 for element in sub]
SCHOOL = [element for sub in SCHOOL2 for element in sub]


INSTITUTION = np.array(INSTITUTION)
BATCH = np.array(BATCH)
SCHOOL = np.array(SCHOOL)


INSTITUTION = INSTITUTION.reshape(len(INSTITUTION), 1)
BATCH = BATCH.reshape(len(BATCH), 1)
SCHOOL = SCHOOL.reshape(len(SCHOOL), 1)



data = np.concatenate((sno,BATCH, INSTITUTION, SCHOOL, surname, onames, gender, course, status), axis = 1 )
df = pd.DataFrame(data, columns=("sno", "batch", "programme", "institution", "surname", "onames", "gender", "course", "status"))




"""
______________________________________________________________________________________
______________________________________________________________________________________
"""