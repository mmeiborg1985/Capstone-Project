# Capstone-Project
Capstone Project
https://github.com/mmeiborg1985/Capstone-Project

This project is a python based site based around data from the Fantasy Football Calculator API found at https://fantasyfootballcalculator.com/api/v1/adp. 
The user will be required to register for the site using their email and password. After their credentials are saved they will directed to login using their email and password. If their user name is stored in the session they will be directed to /list which is a table containing the top 50 fantasy football players by ADP or Average Draft Position. If the user clicks on each individual Player_name they will be directed to the personal site of that player containing all relevant information from the Players table. The user can click on the link "View my roster" and enter in the individual players on his roster by Name and Postition. 

How to run:
1. Clone repository
2. Create virtual environment(not required)
3. install dependencies from requirements.txt
4. seed Players database by running seed.py
5. run app.py with python3 version
