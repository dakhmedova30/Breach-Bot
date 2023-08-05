#Breach Bot Starter Code
breachYear = 2019


#Greets user
print("Hello! I'm Breach Bot.\n")
userName = input("What is your name?\n")
print("\nNice to meet you " + userName + "!")


#Recounts year of breach
todaysYear = input("\nWhat year is it?\n")
timePassed = int(todaysYear) - breachYear
print("\nWow! That means it has been " + str(timePassed) + " years since the Facebook Data Breach.")


#Introduces breach
print("\nWould you like to learn about the Facebook 2019 Breach?")
giveInfo = input("Type 'yes' or 'no.'\n")


#Explains breach
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("\nPersonal information of 533 million people was stolen from Facebook including phone numbers, full names, locations, some email addresses, and other details from user profiles. The data breach was conducted by \"malicious actors\" who scraped the data by exploiting a vulnerability on the platform that allowed users to find each other by phone number.")
  
  elif topic.lower() == "b":
    print("\nFacebook said it found and fixed the issue in August 2019 and is confident the same route can no longer be used to scrape that data. However, a Facebook spokesman stated that the company did not have plans to notify users individually about the data breach, as it does not have complete confidence in knowing which users would need to be notified. The spokesman also said that in deciding whether to notify users, Facebook weighed the fact that the information was publicly available and that it was not an issue that users could fix themselves.")
  
  elif topic.lower() == "c":
    break
 
  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue.")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no.'\n")


#Shares my take
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("\nThis data breach connects to integrity because Facebook did not have plans to notify users individually about the data breach.")
  
  elif topic.lower() == "b":
    print("\nI disagree with the organization's response because I think Facebook should have let users know that there was a data breach immediately so users could take prompt action.")
  
  elif topic.lower() == "c":
    print("\nI would convince victims to take action by showing what was stolen in the Facebook data breach and how phone numbers can be used as a universal identification. My advice would be to change the password of any accounts that use the same email or password and to use HaveIBeenPwnd to find out if personal information was leaked in the breach.")

  elif topic.lower() == "d":
    break
 
  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue.")

  
#Chatbot ends conversation
print("\nThanks for chatting with me, and I hope you learned something new!")