COMPSCI 260 - Problem Set 5, Problem 4
Due: Fri 8 Nov 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): None

My solutions and comments for this problem are below.
-----------------------------------------------------
a) We can view this situation as a probability problem with two events. The first event has two scenarios: either Murray has the disease, or Murray does not have the disease. The second event also has two scenarios: either the test returned positive or the test returned negative. Based on the results returned by Doctor Mel, we want to know the true probability that Murray is diseased GIVEN, the the test was positive. This is a Bayes Theory problem. We can use Bayes theory to get an equation which represents this true probability. 

P(Murray diseased | Test Positive) = (P(Test Positive|Murray diseased)*P(Murray diseased))/P(Test Positive)

Based on the news, the probability of having the disease is 1/50,000 = 0.002%.
The probability that the test returns positive no matter if you have the disease or not = 0.00396%
Lastly, the probability that the test returns positive, given you have the disease = 99.9%

Plugging these values in gives us P(Murray diseased | Test Positive) = ((0.999)*(0.00002))/(0.0000396) = 0.5045
This means the actual probability that Murray is sick is only 50.45%.

b) The test is 99.9% accurate given that you already know the patients diagnosis (whether or not they are diseased) ahead of time. Since Murray is not sure if he has the disease or not prior to that point, this is a probability problem with two different events and the test is not truly 99.9% accurate. In order to observe a more reasonable false positive rate, the diagnostic test would have to be 100% accurate at determining that the patient does not have the disease, given that the patient actually is not diseased. This change would reduce the overall probability that the test returns positive which in turn reduced the likelihood of the test returning a false positive. 

c) The conclusion from part a no longer holds since not all people in the population are equally likely to be diseased. Murray could have been part of an unfortunate few exposed to the specific environmental factor which brings on the disease while the majority of the population was not exposed and therefore does not have the disease. 