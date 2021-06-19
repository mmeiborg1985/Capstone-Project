db.session.create_all()
   
player1= Players(player_id=2434, name='Christian McCaffrey', position='RB', team='CAR', adp=1.2, high=1, low=4, stdev=0.5,bye=13)

player2= Players(player_id=2432, name= 'Dalvin Cook', position= 'RB', team= 'MIN', adp= 2.6, high= 1, low= 5, stdev= 0.7, bye= 7)

player3= Players(player_id=2350, name= 'Derrick Henry', position= 'RB', team= 'TEN', adp= 4.1, high= 1, low= 8, stdev= 1.3, bye= 13)

player4= Players(player_id=2860, name= 'Saquon Barkley', position= 'RB', team= 'NYG', adp= 4.2, high= 1, low= 8, stdev= 1.3, bye= 10)

player5= Players(player_id=2439, name= 'Alvin Kamara', position= 'RB', team= 'NO', adp= 4.5, high= 1, low= 9, stdev= 1.3, bye= 6)

player6= Players(player_id=4864, name= 'Jonathan Taylor', position= 'RB', team= 'IND', adp= 6.7, high= 2, low= 12, stdev= 1.6, bye= 14)

player7=Players(player_id=2343, name= 'Ezekiel Elliott', position= 'RB', team= 'DAL', adp= 7.1, high= 2, low= 15, stdev= 1.7, bye= 7)

player8=Players(player_id=2863, name= 'Nick Chubb', position= 'RB', team= 'CLE', adp= 8.0, high= 3, low= 14, stdev= 1.9, bye= 13)

player9=Players(player_id=2125, name= 'Davante Adams', position= 'WR', team= 'GB', adp= 8.5, high= 1, low= 15, stdev= 2.6, bye= 13)

player10=Players(player_id=1989, name= 'Travis Kelce', position= 'TE', team= 'KC', adp= 9.1, high= 3, low= 16, stdev= 2.1, bye= 12)

player11=Players(player_id=2390, name= 'Tyreek Hill', position= 'WR', team= 'KC', adp= 11.0, high= 5, low= 17, stdev= 2.2, bye= 12)

player12=Players(player_id=2507, name= 'Aaron Jones', position= 'RB', team= 'GB', adp= 11.0, high= 5, low= 19, stdev= 2.1, bye= 13)

player13=Players(player_id=2625, name= 'Austin Ekeler', position= 'RB', team= 'LAC', adp= 11.9, high= 5, low= 19, stdev= 2.4, bye= 7)

player14=Players(player_id=2316, name= 'Stefon Diggs', position= 'WR', team= 'BUF', adp= 13.2, high= 6, low= 19, stdev= 2.5, bye= 7)

player15=Players(player_id= 4881, name= 'Cam Akers', position= 'RB', team= 'LAR', adp= 15.0, high= 7, low= 23, stdev= 2.7, bye= 11)

player16=Players(player_id= 1975, name= 'DeAndre Hopkins', position= 'WR', team= 'ARI', adp= 15.2, high= 8, low= 22, stdev= 2.6, bye= 12)

player17=Players(player_id= 5008, name= 'Antonio Gibson', position= 'RB', team= 'WAS', adp= 16.1, high= 10, low= 22, stdev= 2.3, bye= 9)

player18=Players(player_id= 3239, name= 'D.K. Metcalf', position= 'WR', team= 'SEA', adp= 17.2, high= 9, low= 27, stdev= 3.1, bye= 9)

player19=Players(player_id= 2866, name= 'Calvin Ridley', position= 'WR', team= 'ATL', adp= 19.7, high= 12, low= 29, stdev= 2.7, bye= 6)

player20=Players(player_id= 2499, name= 'George Kittle', position= 'TE', team= 'SF', adp= 20.3, high= 12, low= 29, stdev= 3.2, bye= 6)

player21=Players(player_id= 2322, name= 'Darren Waller', position= 'TE', team= 'LV', adp= 21.1, high= 12, low= 29, stdev= 3.1, bye= 8)

player22=Players(player_id= 2462, name= 'Pat Mahomes', position= 'QB', team= 'KC', adp= 21.1, high= 8, low= 32, stdev= 5.0, bye= 12)

player23=Players(player_id= 4862, name= "D'Andre Swift", position= 'RB', team= 'DET', adp= 21.7, high= 11, low= 32, stdev= 3.9, bye= 9)

player24=Players(player_id= 3247, name= 'A.J. Brown', position= 'WR', team= 'TEN', adp= 22.1, high= 12, low= 32, stdev= 3.5, bye= 13)

player25=Players(player_id= 2438, name= 'Joe Mixon', position= 'RB', team= 'CIN', adp= 23.3, high= 9, low= 36, stdev= 5.2, bye= 10)

player26=Players(player_id= 1992, name= 'Keenan Allen', position= 'WR', team= 'LAC', adp= 24.8, high= 16, low= 34, stdev= 3.3, bye= 7)

player27=Players(player_id= 2357, name= 'Michael Thomas', position= 'WR', team= 'NO', adp= 25.8, high= 16, low= 37, stdev= 3.8, bye= 6)

player28=Players(player_id= 3255, name= 'Josh Jacobs', position= 'RB', team= 'LV', adp= 26.7, high= 14, low= 37, stdev= 4.8, bye= 8)

player29=Players(player_id= 4888, name= 'J.K. Dobbins', position= 'RB', team= 'BAL', adp= 27.0, high= 15, low= 38, stdev= 4.4, bye= 8)

player30=Players(player_id= 4876, name= 'Justin Jefferson', position= 'WR', team= 'MIN', adp= 27.0, high= 18, low= 37, stdev= 3.4, bye= 7)

player31=Players(player_id= 5162, name= 'James Robinson', position= 'RB', team= 'JAX', adp= 27.9, high= 1, low= 49, stdev= 11.0, bye= 7)

player32=Players(player_id= 4889, name= 'Clyde Edwards-Helaire', position= 'RB', team= 'KC', adp= 28.5, high= 17, low= 40, stdev= 4.4, bye= 12)

player33=Players(player_id= 3252, name= 'Miles Sanders', position= 'RB', team= 'PHI', adp= 30.5, high= 20, low= 40, stdev= 3.9, bye= 14)

player34=Players(player_id= 3238, name= 'David Montgomery', position= 'RB', team= 'CHI', adp= 31.8, high= 20, low= 42, stdev= 4.2, bye= 10)

player35=Players(player_id= 2130, name= 'Allen Robinson', position= 'WR', team= 'CHI', adp= 34.5, high= 25, low= 47, stdev= 3.6, bye= 10)

player36=Players(player_id= 2518, name= 'Chris Carson', position= 'RB', team= 'SEA', adp= 36.0, high= 27, low= 47, stdev= 3.3, bye= 9)

player37=Players(player_id= 3449, name= 'Terry McLaurin', position= 'WR', team= 'WAS', adp= 36.1, high= 25, low= 46, stdev= 3.9, bye= 9)

player38=Players(player_id= 2885, name= 'Josh Allen', position= 'QB', team= 'BUF', adp= 36.3, high= 22, low= 53, stdev= 5.4, bye= 7)

player39=Players(player_id= 2111, name= 'Mike Evans', position= 'WR', team= 'TB', adp= 37.3, high= 26, low= 51, stdev= 4.0, bye= 9)

player40=Players(player_id= 1796, name= 'Julio Jones', position= 'WR', team= 'ATL', adp= 37.9, high= 26, low= 48, stdev= 4.2, bye= 6)

player41=Players(player_id= 2277, name= 'Amari Cooper', position= 'WR', team= 'DAL', adp= 40.3, high= 28, low= 53, stdev= 4.5, bye= 7)

player42=Players(player_id= 2450, name= 'Kareem Hunt', position= 'RB', team= 'CLE', adp= 40.7, high= 29, low= 51, stdev= 4.1, bye= 13)

player43=Players(player_id= 3299, name= 'Kyler Murray', position= 'QB', team= 'ARI', adp= 41.3, high= 27, low= 58, stdev= 5.4, bye= 12)

player44=Players(player_id= 2465, name= 'Chris Godwin', position= 'WR', team= 'TB', adp= 43.2, high= 33, low= 56, stdev= 3.9, bye= 9)

player45=Players(player_id= 2737, name= 'Raheem Mostert', position= 'RB', team= 'SF', adp= 43.9, high= 30, low= 59, stdev= 5.2, bye= 6)

player46=Players(player_id= 1981, name= 'Robert Woods', position= 'WR', team= 'LAR', adp= 44.3, high= 34, low= 56, stdev= 3.6, bye= 11)

player47=Players(player_id= 4869, name= 'CeeDee Lamb', position= 'WR', team= 'DAL', adp= 44.8, high= 33, low= 59, stdev= 4.2, bye= 7)

player48=Players(player_id= 2872, name= 'Mark Andrews', position= 'TE', team= 'BAL', adp= 45.4, high= 26, low= 61, stdev= 7.3, bye= 8)

player49= Players(player_id= 2431, name= 'Adam Thielen', position= 'WR', team= 'MIN', adp= 46.6, high= 34, low= 61, stdev= 4.6, bye= 7)

player50= Players(player_id=3258, name= 'Myles Gaskin', position='RB', team='MIA', adp=47.6, high=31, low=63, stdev=6.0, bye=14)


db.session.add_all([player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12, player13, player14, player15, player16, player17, player18, player19, player20, player21, player22, player23, player24, player25, player26, player27, player28, player29, player30, player31, player32, player33, player34, player35, player36, player37, player38, player39, player40, player41, player42, player43, player44, player45, player46, player47, player48, player49, player50])

db.session.commit()
