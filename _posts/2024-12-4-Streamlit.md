---
layout: post
title:  "Utah NHL: Further Analysis"
date: 2024-02-05
description: A further look into Utah HC with the Streamlit app.   
image: "/assets/img/image5.jpg"
display_image: false  # change this to true to display the image below the banner 
---
<p class="intro"><span class="dropcap">T</span>his post discuss some futher analysis of Utah HC data as well as the introduction of a Streamlit app. </p>

### Introdction and Recap

<p>In my last post we started to look into some hockey data to get a sense of who the best players might be. As a reminder here's there charts I made for the beginnning of my analysis. This first one is to get a demographic of the players.</p>

![Fig Name](https://raw.githubusercontent.com/brachel1/myblog/main/assets/img/thumbnail_image004.png)

<p>The second one shows who leads in goals for last season.</p>

![Fig Name](https://raw.githubusercontent.com/brachel1/myblog/main/assets/img/thumbnail_image002.png)

<p>For reference here is a list of all the terms.</p>
<p>GP - Games Played</p>
<p>G - Goals</p>
<p>A - Assists</p>
<p>P - Points (a point is awarded for each goal or assist)</p>
<p>+/- - Plus-Minus (they get 1 point for every point score while they are on the ice and -1 for goals scored on them)</p>
<p>PIM - Penalties in Minute</p>
<p>PPG - Power Play Goals</p>
<p>PPP - Power Play Points</p>
<p>SHG - Shorthanded Goals</p>
<p>SHP - Shorthanded Points</p>
<p>GWG - Game Winning Goals</p>
<p>OTG - Overtime Goals</p>
<p>S - Shots on Goal</p>
<p>S% - Shooting Percentage</p>
<p>FO% - Face-Off Percentage</p>

<p>Positions:</p>
<p>C - Center</p>
<p>D - Defense</p>
<p>G - Goalie</p>
<p>LW - Left Wing</p>
<p>RW - Right Wing</p>
<p>(C, LW, and RW are all forward positions)</p>

### New Analysis

<p>For the next metric I did my own calculation. I divided the number of goals, by the number of games for goals per game (GPG). This chart shows the average GPG for each player. Considering goals and games played are highly correlated, I expected the results to be much the same. Dylan Guenther was who I took the most note of. I've heard a lot about him, he signed an 8 year contract, so I knew he must be a pretty good player. I'd been surprised that he was more in the middle of the pack for goals last season, but looking at GPG helped to understand why they wanted to sign him for such a long contract.</p>

![Fig Name](https://raw.githubusercontent.com/brachel1/myblog/main/assets/img/thumbnail_image001.png)

<p>A second metric I decided to look at is shooting percentage, which also gave some surprising results. I was surprised to see that the leader was a defenseman, with a percentage almost double the next highest defenseman. Dylan Guenther and Clayton Keller were farther down the list than I expected, and some players we haven't yet taken note of were in the top.It makes sense why shooting percentage wasn't highly correlated with any of the other metrics.</p>

![Fig Name](https://raw.githubusercontent.com/brachel1/myblog/main/assets/img/thumbnail_image003.png)

### Streamlit App

<p>To help with further analysis I decided to build a an app with <a href="https://streamlit.io/cloud">Streamlit</a>. 
In Tableau I had to make separate pages to look at different metrics, but with streamlit I can look at different metrics much more easily. 
On the first tab I made and interactive bar chart where you can customize pretty much everthing in the chart. You can look at a specific season, 
career, or average of any of the stats from the dataset. I also included a slider to choose the number of players to look at.</p>

![Fig Name](https://raw.githubusercontent.com/brachel1/myblog/main/assets/img/streamlit1.jpeg)

<p>The second page shows player demographics. A scatterplot of height and weight, but you can choose between using position or handedness. Handedness refers to if they use a left or right stick. In hockey it's fairly common to use the opposite stick of your dominant hand, which is why you will see a lot of players using left sticks.</p>

![Fig Name](https://raw.githubusercontent.com/brachel1/myblog/main/assets/img/streamlit2.jpeg)

<p>The last page allows you to choose a player and see all of their career stats in a table, as well as their personal information. You can find access my <a href="https://hockeyapp-ukuwtpptzyszsyp5wmgynr.streamlit.app">here</a>.  </p>

![Fig Name](https://raw.githubusercontent.com/brachel1/myblog/main/assets/img/streamlit3.jpeg)

<p>There are so many things to explore and learn from this dataset! Determining who the best players are cannot be based on
just one statistic. There are a lot of different things to look at especially on the first page, play around with the data and see what you can learn.
With so many metrics it can sometimes be difficult to identify patterns, so I'd encourage picking a few metrics that you think  
would be the most important for strong players. You can also take this as inspiration to build your own app. If you'd like to see how I made the Streamlit app, here's the link to the code 
 in my <a href="https://github.com/brachel1/hockey_streamlit"> GitHub repo</a>.</p>
