# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-
'''
Created on May 15, 2016

@author: Built_In_Automation Solutionz Inc.
'''
from Framework.Built_In_Automation.Web.Selenium import BuiltInFunctions






def test1():
    dependency = {'Browser': 'chrome'}
    gotoweb = [ [ ( 'web_page' , '' , 'http://qa-factory.assetscience.com/totalanalysis/devicesearch/show/1637187' , False , False ) ] ]
    login = [ [ ( 'id' , 'element parameter' , 'username' , False , False ) , ( 'text' , 'action' , 'automationadmin' , False , False ) ]  , [ ( 'id' , 'element parameter' , 'password' , False , False ) , ( 'text' , 'action' , 'password' , False , False ) ]  , [ ( 'id' , 'element parameter' , 'submit' , False , False ) , ( 'click' , 'action' , 'click' , False , False ) ]  , [ ( 'sleep' , 'action' , '5' , False , False ) ] ]
    global selenium_driver
    BuiltInFunctions.Open_Browser(dependency)
    selenium_driver = BuiltInFunctions.get_driver()
    
    BuiltInFunctions.Go_To_Link(gotoweb)
    BuiltInFunctions.Sequential_Actions(login)
    
    # tag, partial matching class name, exact text
    # field =tag ;  sub field = element parameter; value = span
    # field =text ;  sub field = element parameter; value = Tests
    # field =*class;  sub field = element parameter; value = category_header 
        
    xpath_code = '//span[contains(@class, "category_header")][text()= "Tests"]'
    
    
    
    a = selenium_driver.find_elements_by_xpath(xpath_code)
    print a
    # tag, partial matching class name, partial matching text
    # field =tag,*class,*text ;  sub field = element parameter; value =|'|span|'|category_header|'|Tests|'|
    b = selenium_driver.find_elements_by_xpath('//span[contains(@class, "category_header")][contains(text(), "Tests")]')
    
    # any tag, partial matching class name, partial matching text
    # Note: for tag, if not defined, we always assume it is all tag.  So users have two ways to enter data here
    # field =*class,*text ;  sub field = element parameter; value =|'|category_header|'|Tests|'|
    c = selenium_driver.find_elements_by_xpath('//*[contains(@class, "category_header")][contains(text(), "Tests")]')
    
    # any tags, partial matching class name, partial matching text
    # field =*class,*text ;  sub field = element parameter; value =|'|category_header|'|Advanced Information|'|
    d = selenium_driver.find_elements_by_xpath('//*[contains(@class, "category_header")][contains(text(), "Advanced Information")]')
    
    # any tags, partial matching href, partial matching text
    # field =*href,*text ;  sub field = element parameter; value =|'|/showxml/1637187|'|View XML|'|
    e = selenium_driver.find_elements_by_xpath('//*[contains(@href, "/showxml/1637187")][contains(text(), "View XML")]')
    
    # tag
    # field = tag ;  sub field = element parameter; value = |'|span|'|
    f = selenium_driver.find_elements_by_xpath('//span')
    
    # try to locate a table that has child reference 
    # reference as child 
    # field = *class; sub field =element parameter ; value =|'|container_material print_section_container|'|
    # field = class, text   sub field = child parameter;  value =|'|category_header|'|Tests|'|

    g1 = selenium_driver.find_elements_by_xpath('//*[contains (@class, "container_material print_section_container") and .//*[@class= "category_header"][text()= "Tests"]]')
    
    g2 = selenium_driver.find_elements_by_xpath('//*[contains (@class, "container_material print_section_container") and .//*[@class= "category_header"][text()= "Tests"]]')
    # NOTE: make sure you are on the home page for these calls to work 
    # try to locate a button that has parent as reference 
    # reference as parent
    # example 1:
    # field = *href; sub field = element parameter; value = |'|report|'|
    # field = class; sub field = parent parameter; value = |'|panel panel-default|'|
    # example 2:
    # in the second example, we provided two parameters for our element. Note the parent goes inside the first or second parameter.. 
    # the word Report has space infront of it.  So we need to make sure we dont strip any empty spaces when collecting the data.  
    # field = *class, text; sub field = element parameter; value =|'|btn btn-default|'| Reports|'|
    # field = class, text; sub field = parent parameter; value =|'|panel-body|'|
    h1 = selenium_driver.find_elements_by_xpath('.//*[ contains(@href, "report")   and //*[@class= "panel panel-default"]]')
    h2 = selenium_driver.find_elements_by_xpath('.//*[contains(@class, "btn btn-default")   and //*[@class= "panel-body"]] [text()= " Reports"]')
 
    # include index with the element or reference element 
    # if - is used, that means we go from back.  If we found 4 items and user puts -1 it means we have to take the last item example a = [1,2,3,4]; a[-1] = 4.  The reason is we may have a situation where going from bottom is always constant 
    # field = *href,index; sub field = element parameter; value = |'|report|'|0|'|
    # field = class; sub field = parent parameter; value = |'|panel panel-default|'|
    # need a little more investigation if we want to provide index to parent parameter as well (which we should)
    
    i = selenium_driver.find_elements_by_xpath('//*[@class= "category_header"][position()=8]')
    
    # siblings
    # //*[@type='submit']//following-sibling::input
    j = selenium_driver.find_elements_by_xpath('//*[@href="/totalanalysis/testsuite"]/following-sibling::a[contains(text(), "Configuration names")]')
    

def construct_xpath (step_data_set): 
    
    child_ref_exits = any("child parameter" in s for s in step_data_set)
    parent_ref_exits = any("parent parameter" in s for s in step_data_set)
    child_parameter_list = filter(lambda x: 'child parameter' in x, step_data_set) 
    element_parameter_list = filter(lambda x: 'element parameter' in x, step_data_set) 
    parent_parameter_list = filter(lambda x: 'parent parameter' in x, step_data_set) 
    
    if child_ref_exits == False and parent_ref_exits == False :
        '''  If  there are no child or parent as reference, then we construct the xpath differently'''
        #first we collect all rows with element parameter only 
        xpath_element_list = (construct_xpath_list(element_parameter_list))
        return construct_xpath_string_from_list(xpath_element_list) 
    elif child_ref_exits == True and parent_ref_exits == False:
        '''  If  There is child but making sure no parent'''
        xpath_child_list =  construct_xpath_list(child_parameter_list,True)
        child_xpath_string = construct_xpath_string_from_list(xpath_child_list) 
        xpath_element_list = construct_xpath_list(element_parameter_list)
        #Take the first element, remove ]; add the 'and'; add back the ]; put the modified back into list. 
        xpath_element_list[1] = (xpath_element_list[1]).replace("]","") + ' and ' + child_xpath_string + "]"
        return construct_xpath_string_from_list(xpath_element_list) 
    if child_ref_exits == False and parent_ref_exits == True:
        '''  If  There is parent but making sure no child'''
        xpath_parent_list =  construct_xpath_list(parent_parameter_list)
        parent_xpath_string = construct_xpath_string_from_list(xpath_parent_list) 
        xpath_element_list = construct_xpath_list(element_parameter_list,True)
        #Take the first element, remove ]; add the 'and'; add back the ]; put the modified back into list. 
        xpath_element_list[1] = (xpath_element_list[1]).replace("]","") + ' and ' + parent_xpath_string + "]"
        return construct_xpath_string_from_list(xpath_element_list) 

def construct_xpath_list(parameter_list,add_dot=False):
        element_main_body_list = []
        excluded_attribute = ["*text", "text", "tag", "css", "index","xpath"]
        for each_data_row in parameter_list:
            attribute = (each_data_row[0].strip()).lower()
            attribute_value = each_data_row[2]
            if "xpath" in "test":
                print "bl"
            
            elif attribute == "text":
                text_value = '[text()="%s"]'%attribute_value
                element_main_body_list.append(text_value)
            elif attribute == "*text":
                text_value = '[contains(text(),"%s")]'%attribute_value    
                element_main_body_list.append(text_value)
            elif attribute not in excluded_attribute and '*' not in attribute:
                other_value = '[@%s="%s"]'%(attribute,attribute_value)
                element_main_body_list.append(other_value)
            elif attribute not in excluded_attribute and '*' in attribute:
                other_value = '[contains(@%s,"%s")]'%(attribute.split('*')[1],attribute_value)
                element_main_body_list.append(other_value)
                #we do the tag on its own  
        tag_was_given = any("tag" in s for s in parameter_list)
        if tag_was_given == True:
            tag_item = "//"+ filter(lambda x: 'tag' in x, parameter_list)[0][2]
        else:
            tag_item = "//*"
        if add_dot != False:
            tag_item = '.'+tag_item
        element_main_body_list.append(tag_item)
        return list(reversed(element_main_body_list))

def construct_xpath_string_from_list(xpath_list): 
    xpath_string_format = ""
    for each in xpath_list:
        xpath_string_format = xpath_string_format+each   
    return  xpath_string_format
    
def get_xpath_elements(xpath_string_format,index=False):  
    all_matching_elements = selenium_driver.find_elements_by_xpath(xpath_string_format)
    if len(all_matching_elements)== 0:
        return "Failed"
    elif len(all_matching_elements)==1 and index == False:
        return all_matching_elements[0]
    elif len(all_matching_elements)>1 and index == False:
        print "Warning: found more than one element with given condition.  Returning first item.  Consider providing index"
        return all_matching_elements[0]  
    elif len(all_matching_elements)==1 and abs(index) >0:
        print "Warning: we only found single element but you provided an index number greater than 0.  Returning the only element"  
        return all_matching_elements[0]
    elif len(all_matching_elements) >1 and index != False:
        if (len(all_matching_elements)-1) < abs(index):
            print "Warning: your index exceed the the number of elements found. Check again"
            return "Failed"
        else:
            return all_matching_elements[index]        

def step_data_validate(step_data):
    #element parameter must exist
    all_middle_row = [(item[1].strip()).lower() for item in step_data_set]
    if 'element parameter' not in all_middle_row:
        print "Error, at least one element parameter must be provided"
        return "Failed"
 
def get_element_by_xpath(step_data):
    print ""

def get_element_by_css(step_data):    
    print ""

def get_element(step_data):
    print ""    
# step_data_set = [ ( 'tag' , 'element parameter' , 'span' , False , False ) , ( '*text' , 'element parameter' , 'Tests' , False , False ) , ( '*class' , 'element parameter' , 'category_header' , False , False ) , ( 'text' , 'chil d parameter' , 'password' , False , False )] 
# 
# print filter(lambda x: 'child parameter' in x, step_data_set)    
step_data_set = [ ( ' tag ' , ' element parameter' , 'span' , False , False ) , ( '*text' , 'element parameter' , 'Tests' , "xpath" , False ) , ( '*class' , 'element parameter' , 'category_header' , False , False ) , ( 'text' , 'parent parameter' , 'password' , False , False )] 
    

#print construct_xpath (step_data_set)
#lst = [['a','b','c'], [1,2,3], ['x','y','z']]
lst2 = [(item[1].strip()).lower() for item in step_data_set]
print lst2

#step_data_set = [x.strip(' ') for x in step_data_set]

#print step_data_set
#test1()

