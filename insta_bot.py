from selenium import webdriver
import time



def followers():
    time.sleep(2)
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(2)
        ht = driver.execute_script("""
                    arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                    return arguments[0].scrollHeight;
                    """, scroll_box)
    links = scroll_box.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']
    # close button
    driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
    return names


def following():
    time.sleep(2)
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(2)
        ht = driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)
    links = scroll_box.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']
    # close button
    driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
    return names


driver_path = r'C:\Users\lakshya\PycharmProjects\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('https://www.instagram.com/')
time.sleep(5)

username=input("Enter username: ")
password=input("Enter Password: ")


driver.find_element_by_xpath("//input[@name = 'username']").send_keys(username)       #Enters username
driver.find_element_by_xpath("//input[@name = 'password']").send_keys(password)       #Enters password
driver.find_element_by_xpath("//button[@type='submit']").click()                      #LogIn Button
time.sleep(10)

driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()   #Not Now Button

driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
time.sleep(10)

driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()            #followers
time.sleep(5)
list_followers=[]
list_followers=followers()


driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
time.sleep(1.5)
list_following=[]
list_following=following()


while 1 :
    print("\n1.FOLLOWERS")
    print("2.FOLLOWING")
    print("3.WHO DON'T FOLLOW YOU")
    print("4.WHOM YOU DON'T FOLLOW")
    print("5.EXIT!!")
    print(" ")

    n=int(input("Enter your choice:"))
    if n==1:
        print(" ")
        print("YOUR FOLLOWERS:")
        for name in list_followers:
            print(name)
    elif n==2:
        print(" ")
        print("PEOPLE WHOM YOU ARE FOLLOWING:")
        for name in list_following:
            print(name)
    elif n==3:
        print(" ")
        print("PEOPLE WHO DON'T FOLLOW BACK:")
        t=[]
        t=list(set(list_following)-set(list_followers))
        for name in t:
            print(name)
    elif n==4:
        print(" ")
        print("PEOPLE WHOM YOU DON'T FOLLOW BACK:")
        t=[]
        t = list(set(list_followers)-set(list_following))
        for name in t:
            print(name)
    elif n==5:
        print("THANKS FOR USING!!")
        exit()
