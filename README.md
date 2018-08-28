# Question & Answer

A simple game of Questions & Answers, in which you click on a panel to receive 
a question, which you answer and submit by clicking a button.

Questions will cover various subjects like javascript python html css.

You will see how both you and others online are doing as both you and others scores
will be displayed.

You will also see in a mini leaderboard on the page who has answered the most questions correctly
and in a full leaderboard on another page all users and scores.

## UX

This website is for everybody who enjoys trying to complete quiz/challange

As a user I would like to pick a username to display in the game. This is achieved on the landing page, and username is displayed on
the game page, it is also kept in the input on landing page so when you come back again you dont have to remember it.
As a user I should be able to click a panel and receive a question to be answered  
As a user I should be able to see whether my answer is correct or wrong, This is achieved by the border of the panel changing to
green for correct answers and red for wrong answers.  
As a user I should be able to see my score, This is achieved by a display showing username and score  
As a user I should be able to see how others who are online are doing, This is achieved by a display showing
other user scores  
As a user I should be able to see how I did compared to other users. This is achieved both by a mini leaderboard on the page, and a 
full leaderboard ascessed by a link.
As a user I would like to know who is online and when they leave. This is achieved by a display.

## Features

While i dont sketch out desing ideas i generally try out layouts ideas in replit or elsewhere below are links to my test layouts.
These would be ideas that are either going to be used or adjusted and then used.

1. landing page test layout https://johnl3.github.io/layout-test/
2. game page test layout https://johnl3.github.io/layout-test/game.html
3. https://repl.it/@JohnL3/practiceleaderboard

1. Choose username with length up to 12 characthers. User can choose there username on the landing page. This 
will remain visible in the input so even when the navigate to game page or leaderboard page when the come back to the
landing page it is still there so as they dont forget what username they picked.
2. Leaderboard: A link to a full leaderboard is on both the landing page and the game page. Anyone can visit the leaderboard,
even those who have not choosen a username. A mini leaderboard is also available on gamepage only users who choose a username and
visit game page will see this.
3. Username display: Your username will be displayed on the game page.
4. Online Users: An online users display will show all users as they arrive/leave the game page.
5. Score: Scores for both you and others will also be displayed in the online users section.
6. Insturctions: A brief instructions panel explaining what to do will appear each time you visit the game page.
7. Restrictions: Only those that choose a username will be permitted to visit the game page, typing game into browser at end
of web address will redirect back to landing page.

## Future Features

1. DATABASE: As in memory storage is used for game it would be nice to add a database for pernament storage.
2. Harder: Make the game more challenging either by adding lifes that could be lost when you get a question wrong, or levels
where if you complete one set of questions you would go to next level and get more questions.


## Technologies Used

1. cloud9
 * Recommended by course
 * https://ide.c9.io/
2. jQuery
 * Used as it simplifies Dom manipulation
 * https://api.jquery.com/
3. Flask SocketIO
 * Used so i could show in real time users joining/leaving game ... when there score changes.
 * https://flask-socketio.readthedocs.io/en/latest/





























