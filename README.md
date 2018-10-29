# Weather-Text

This simple app scrapes the National Weather Service Website for the current temperature and forecast for the day. It then sends a text message to my daughter's phone using Twilio everyday at 6:30 am using the Tasks Scheduler from PythonAnywhere.com. 

I used the NWS website because it was much simpler than non-government websites and I assume will be updated less requiring less maintenance of the scraper. I had previously used the Weather Underground API but that is being discontinued in December of 2018. I used the included urllib package and BeautifulSoup, and of course the Twilio package. 

I was motivated to write the app by my daughter, who would routinely dress herself for school in the morning without having any idea what the weather was going to be. In North Carolina, like in other parts of the country, the weather can change rapidly during the day, with many days having a temperature difference of 30 degrees. Rather than just sign her up for a push notification I used this as an opportunity to get her involved in programming and also for myself to learn more. 
