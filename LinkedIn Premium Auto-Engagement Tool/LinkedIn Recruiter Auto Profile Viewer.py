
#LinkedIn Recruiter Auto Page Viewer

#After you identify recruiters that have LinkedIn Premium,
#input their URL into this tool.
#The tool will log in to your profile and view their page.
#With Premium, they recieve a notification that you viewed their profile.
#You can add dozens of URLs to view at once so you don't have to manually search!
#Run the tool twice per week to keep the recruiters thinking about you.

#Mass Engagement

#Install Selenium, then install a webdriver. 

from selenium import webdriver


#Navigates to LinkedIn.com
driver = webdriver.Firefox()
driver.get('https://www.linkedin.com/login')

#Username
usernameField = driver.find_element_by_xpath('//*[@id="username"]')
usernameField.send_keys('insert login email address here')

#Password
passwordField = driver.find_element_by_xpath('//*[@id="password"]')
passwordField.send_keys('insert password here')

#Logs into LinkedIn
loginButton = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
loginButton.click()




###############Recruiters#######################################################################

#'Recruiter' Name - 'Job Title' at 'Company Name'
driver.get('insert profile URL including https:// here')


#Copy and paste this line for as many recruiters as you want to engage with. 
#It will iterate through all of them.