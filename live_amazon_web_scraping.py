import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


#link to the webpage your webpage is on
site_url = ("https://www.amazon.com/Sony-WH-1000XM5-Canceling-Headphones-Hands-Free/dp/B09XS7JWHH/ref=sr_1_1_sspa"
            "?crid=RQK95AHV7W3U&dib=eyJ2IjoiMSJ9.3WsHXw5IKX8zh6PbdrakcxdH1zA7vK1vXVpgQD4nxdVLe4MIkA"
            "-pHXG9xx9McLgLmWDtdEV-6jwIE33VmXICnH0Um4S-Pducx6YSPzQEmKOusw"
            "-ScFj7T1XiFGrqKDbUlAUqBBBbeMawcXli3TgV54qMoxjmUWRjEJlvNb7mti4CNT5g4fJmZVGO-W5dEMrw5Gjmih-rnAgZm_M8LqYfns"
            "-EXiKs1NJ9cIGt1eKMni0.jcPg3TBicIzN1Us1_6S_dwacU_cwyuy61BPGdeArAZ8&dib_tag=se&keywords=sony+headphones"
            "&qid=1724606045&sprefix=sony+%2Caps%2C1271&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")


headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en;q=0.9",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"
                      " (KHTML, like Gecko) "
                      "Version/17.5 Safari/605.1.15",
}
soup = BeautifulSoup(requests.get(site_url).text, "html.parser")
name = soup.find(id="productTitle").text
price = soup.find_all(class_="a-price-whole")
get_price = price[1].text
message = f"{name.strip()} \n price: ${get_price} \n link:{site_urlf}"


#send email
smtp_server = "smtp.gmail.com"
port = 587
receiver_email = "korededavid03@gmail.com"

sender_email = "feranmidavid427@gmail.com"
password = 'mtoc rvfk mume umln'

# Email content
subject = "Sony Headset on Amazon"
body = message

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

server = smtplib.SMTP(smtp_server, port)
server.starttls()  # Secure the connection
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message.as_string())
print("Email sent!")
