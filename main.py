from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from credentials import sender_email, sender_password
from config import book_my_show_link, date, email_notif_receiver, mail_message, loop_time

def send_email(receiver_email):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, mail_message)

def check_website(url):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)

    wait = WebDriverWait(driver, 20)
    date_numeric_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "date-numeric")))
    
    if date_numeric_div.text.strip() == date:
        print("Available")
        driver.quit()
        return True

    print("Not Available")
    driver.quit()
    return False

def main():
    while True:
        if check_website(book_my_show_link):
            send_email(email_notif_receiver)
            break
        time.sleep(loop_time)

if __name__ == "__main__":
    main()
