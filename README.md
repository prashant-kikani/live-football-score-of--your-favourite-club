# live-football-score-of--your-favourite-club
Notifies you when your favourite football team scores or faces a Goal... <br />
<br />
I used selenium web-driver (http://www.seleniumhq.org/projects/webdriver/) to fetch data from this site : http://www.livescore.com/soccer/live/ <br />

It fetches data from this site every after 30 seconds then checks if one of your favourite football team has scored or faced a goal or not. <br />
If that happens, it sent you an email notification instantly.<br />

I used BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for scrap the data. <br />

# limitations
The source email id need to change it's security level to low. <br />
So, my code can login into it, and send notifications to target email id. 

