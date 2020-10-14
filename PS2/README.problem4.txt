COMPSCI 260 - Problem Set 2, Problem 4
Due: Fri 27 Sep 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): TA Office Hours / Piazza / Google

My solutions and comments for this problem are below.
-----------------------------------------------------
a) Always selecting the activity of the shortest duration from those that are compatible with the ones already selected is not the optimal solution. This does not work if there is a large gap between the activities or the shortest duration activity overlaps two possible events. In the attached diagram, the optimal solution would be the top three events. However, due to this greedy algorithm, the bottom two events would be selected since they are shorter. This example shows that this algorithm is not always correct.

b) Always selecting the activity that overlaps the fewest activities remaining is also not the optical solution. There can be a time frame that offers multiple events with lots of overlap. However, if there are two events that are very short and can be done in the time span of a singular event, they would be components of the optimal schedule. If you did not choose them due to overlap though, you could not achieve the optimal solution. In the diagram attached, the optimal solution would be to choose the top four activities. However, since the activities numbered two and three have multiple overlaps, the activity numbered 5 would be selected in this algorithm for the middle time slot. This example shows that this greedy algorithm does not always yield the optimal solution.