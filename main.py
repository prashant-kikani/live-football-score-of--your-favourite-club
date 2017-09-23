import bs4 as bs
from selenium import webdriver
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
msg = MIMEMultipart()
fromadd = "SOURCE_EMAIL_ID_HERE"
frompwd = "SOURCE_EMAIL_ID_PASSWORD_HERE"
toadd = "TARGET_EMAIL_ID_HERE"
msg['From'] = fromadd
msg['To'] = toadd

# TITLE OF YOUR MAIL
msg['Subject'] = "Live Football score of your FAVOURITE clubs for you"

server.login(fromadd, frompwd)

# WEBSITE FOR LIVE FOOTBALL SCORE
url = 'http://www.livescore.com/soccer/live/'

# LIST OF USER'S FAVOURITE CLUB HERE
favourite = ["Barcelona", "Real Madrid", "Bayern Munich"]
# favourite = ["Nice", "Mainz 05 II", "Paris FC", "Nimes", "Bayern Munich", "Monaco", "Znicz Pruszkow"]

#PREVIOUS SCORE ARRAY
precl1 = []
precl2 = []
len = favourite.__len__()
for j in range(len):
    precl1.append(0)
    precl2.append(0)


while True:
    # print(precl1, precl2)
    ok = 0
    body = "Hey, check out the latest football scores of your FAVOURITE clubs....\n\n"
    
    browser = webdriver.Chrome()
    browser.get(url)
    sauce = browser.page_source
    browser.quit()
    soup = bs.BeautifulSoup(sauce, 'lxml')


    with open("scores.txt", "w") as file:
        for div in soup.find('div', attrs={'data-type': 'container'}).find_all('div'):
            print("{}".format(div.text), file=file)
    

    with open("scores.txt", "r") as file:
        for l in file:
            l = str(l)
            if (l.__contains__("coverage")):
                s = l.split(" ")
                for c in s:
                    if c == '':
                        s.remove(c)
                if s.__len__() > 3:
                    # print(s)
                    mins = s[0]
                    min = mins[:2]
                    # print(min)
                    s = s[2:]
                    if s.__len__() != 0:
                        i = 0
                        club1 = ""
                        club2 = ""
                        # print(s)
                        while s[i] != "\n" and s[i] != "-":
                            ss = s[i]
                            if ss != "" and not (57 >= ord(ss[0]) >= 48):
                                club1 = club1 + s[i] + " "
                            i += 1
                        i -= 1
                        club1s = s[i]
                        # print(club1, " ", club1s)
                        i = 0
                        while s[i] != "\n" and s[i] != "-":
                            i += 1
                        i += 1
                        club2s = s[i]
                        i += 1
                        while s[i] == "":
                            i += 1
                        while s[i] != "":
                            club2 = club2 + s[i] + " "
                            i += 1
                        # print(s)
                        club1 = club1.strip()
                        club2 = club2.strip()
                        # print(club1, " ", club2)

                        for j in range(len):
                            if club1 == favourite[j] or club2 == favourite[j]:
                                # print("inside favourite....")
                                # print(club1, club1s, "-", club2s, club2)
                                # body += "minutes : " + min + "  Scores : " + club1 + " " + club1s + "  -  " + club2s + " " + club2 + "\n\n"

                                if precl1[j] != int(club1s) or precl2[j] != int(club2s):
                                    ok = 1
                                    print("modified......   j = ", j, "precl1[j] ", precl1[j], "precl2[j] ", precl2[j], "club1s ", int(club1s), "club2s", int(club2s))
                                    precl1[j] = int(club1s)
                                    precl2[j] = int(club2s)
                                    body += "minutes : " + min + "  Scores : " + club1 + " " + club1s + "  -  " + club2s + " " + club2 + "\n\n"

        if ok == 1:
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromadd, frompwd)
            text = msg.as_string()
            server.sendmail(fromadd, toadd, text)
            server.quit()
            print("email sent")
			
		# SLEEP FOR HALF A MINUTE
        time.sleep(30)
