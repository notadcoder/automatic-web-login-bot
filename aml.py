from selenium import webdriver


def start_bot(username, password, url):
    path = "c:\\download\\chromedriver"

    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)

    # opening the website in chrome
    driver.get(url)

    # find the username input field by name
    driver.find_element_by_name("username").send_keys(username)

    # find the password input field by name
    driver.find_element_by_name("password").send_keys(password)

    # click on the login button by name
    driver.find_element_by_name("login").click()


# Driver code
# Enter below your login credentials
user_name = "username"
user_password = "password"

# URL of the login page of site
# which you want to automate login.
user_url = "https://www.example.com/login"

# Call the function
start_bot(user_name, user_password, user_url)
