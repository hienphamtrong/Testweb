
# from selenium.webdriver.remote.webelement import WebElement


def generate_xpath(element, current):
    child_tag = str(element.tag_name)
    if child_tag == "html":
        return "/html[1]" + current
    parentElements = element.find_element_by_xpath("..")
    childrenElements = parentElements.find_elements_by_xpath("*")
    count = 0
    for e in childrenElements:
        childrenElementTag = e.tag_name
        if child_tag == childrenElementTag:
            count = count + 1
        if element == e:
            return generate_xpath(parentElements, "/" + child_tag + "[" + str(count) + "]" + current)
