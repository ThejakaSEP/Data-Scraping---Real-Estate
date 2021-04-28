from selenium import webdriver
import pandas as pd
import time


url = 'https://www.lankapropertyweb.com/land/index.php'
driver = webdriver.Chrome('/Users/thejakamahaulpatha/PycharmProjects/WebSraping1/chromedriver')

driver.get(url)



Price_array = []
Land_array=[]
Location_array=[]
Property_type_array=[]

properties = driver.find_elements_by_class_name("thumbnail")
x=0

def GetData():
    driver.get(driver.current_url)
    properties = driver.find_elements_by_class_name("thumbnail")
    x = 0
    for property in properties:
        x = x + 1
        try:
            price = property.find_element_by_xpath(
                '//*[@id="grids"]/div/section/article[' + str(x) + ']/div/div/ul/span[3]').text
            Land = property.find_element_by_xpath(
                '//*[@id="grids"]/div/section/article[' + str(x) + ']/div/div/ul/span[1]').text
            Location = property.find_element_by_xpath(
                '//*[@id="grids"]/div/section/article[' + str(x) + ']/div/a/div[3]').text
            PropertyType = property.find_element_by_class_name("property-type-wrapper").text

            Price_array.append(price)
            Land_array.append(Land)
            Location_array.append(Location)
            Property_type_array.append(PropertyType)

            # Creating a data frame using the arrays as columns

            df = pd.DataFrame()
            df['Price'] = Price_array
            df['Land'] = Land_array
            df['Location'] = Location_array
            df['Type'] = Property_type_array

            #Converting the Data frame to a CSV format and saving in the directory
            df.to_csv("RealEstateData.CSV")

        except:
            raise Exception
res=True

while (res == True):
    try:
        GetData()

    except Exception:
        # submit_button = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div[2]/div/ul/li[6]/a')
        submit_button = driver.find_element_by_css_selector("[aria-label=Next]")

        submit_button.click()
        print("2")
        continue
    except:
        break

    res=False


