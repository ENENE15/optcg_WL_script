OPTCG Win/Loss and Ranking tracker using Bandai TCG+ 

How to use:

1. Download the optcg_WL_script from code -> Download ZIP
   
<img width="645" height="254" alt="image" src="https://github.com/user-attachments/assets/01dee39b-d46e-4481-bbce-96a351b059d6" />

2. Unzip and locate dist -> OPTCG_WL_Tracker.exe and open the exe file. DO NOT CLOSE THE TERMINAL/COMMAND PROMPT SCREEN!

<img width="791" height="85" alt="image" src="https://github.com/user-attachments/assets/10c6f060-8b82-43fa-bb98-fdd69116562b" />

<img width="795" height="53" alt="image" src="https://github.com/user-attachments/assets/0557f62c-3f7f-4793-a067-041763c9f96b" />

3. A browser should launch once you execute the exe file. Log in using Bandai TCG+ ID and make sure to close all pop-up windows (Cookies, password warning, password saver, etc...)
<img width="923" height="902" alt="image" src="https://github.com/user-attachments/assets/b5ae0569-4b74-469c-a8f1-814f098838a8" />


<img width="470" height="203" alt="image" src="https://github.com/user-attachments/assets/e70c856c-08be-4393-b0d1-f14612462ba1" />


<img width="427" height="310" alt="image" src="https://github.com/user-attachments/assets/c753835a-3394-4a3f-8de8-a2b692b5064d" />


4. Once logged in you will be sent to the event history page. Feel free to adjust the event dates, locations, etc... to get the range of winrate data you want

<img width="868" height="653" alt="image" src="https://github.com/user-attachments/assets/8aa9cb30-13f7-4688-a0ef-10e38dccbbf2" />

5. Once you are done with logging in and on the history page as shown above, go back to the terminal/command prompt and press ENTER key once

6. It should automatically start going through match history for Win/Loss counts and ranking

<img width="536" height="164" alt="image" src="https://github.com/user-attachments/assets/ffe934d7-2a1a-4fa7-92d6-6b9bde39cd87" />

7. After it's done going through all the valid events on Bandai TCG+, it will save it in match_history.csv in the same dist folder (optcg_WL_script\dist)

<img width="413" height="710" alt="image" src="https://github.com/user-attachments/assets/0e04b18b-29be-40ad-baf1-cda5a77d1403" />

8. Once you have the match_history.csv, you can play around it using excel/google sheets to see your data and winrates

<img width="52" height="23" alt="image" src="https://github.com/user-attachments/assets/406c1478-3f6f-4f70-9123-51a36da1bed4" />

<img width="92" height="19" alt="image" src="https://github.com/user-attachments/assets/124edd5a-a395-451e-b98a-6253f52f326d" />

<img width="214" height="41" alt="image" src="https://github.com/user-attachments/assets/27758399-f521-49a3-bf8f-a054cb2e9732" />

NOTE:
For Total # of wins/losses/matches: Use =SUM() function on the row of wins/loss and for total # of matches, use =SUM() of total # of wins + total # of loss
For Total winrate: (total # of wins) / (total # of matches)
For Total # of 1st place rankings, on the rankings row use the function =COUNTIF(D2:D108,"=1") to see how many 1st places you got
For other excel/google sheets operations, ask chatGPT or google
