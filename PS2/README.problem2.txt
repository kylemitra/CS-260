COMPSCI 260 - Problem Set 2, Problem 2
Due: Fri 27 Sep 2019, 5pm

Name: Kyle Mitra
NetID: km423

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): TA Office Hours / Piazza / Google

My solutions and comments for this problem are below.
-----------------------------------------------------

a) You can organize this list to begin with the largest sublist and work backwards calculating the collective similarity until you reach a singular number. This method would most likely be faster for all cases except where a singular number is the largest similarity score you can get. 

b) A recursive divide-and-conquer algorithm breaks up the list into two equal length sublists. It then goes through and analyzes all collective similarity tests for each possible sublist on each half of the original list. The maximum sum on each half of the the original list is retained and then the two sums are added together. We are then able to identify the maximum collective similarity score by comparing the maximum scores on each half of the list and the max score of the two returned scores combined. 

c) To make this algorithm effective, you have to continuously update the MAX.SO.FAR and MAX.INCLUDING.HERE values throughout the scan. The MAX.SO.FAR value should be the highest value we have seen up until this point. At initialization, this value will simply be the first integer (whether it is positive or negative). Then, once moving to the next integer in the list, if adding the second integer to the first yields a larger value than just the first integer, MAX.SO.FAR will be updated. If adding the second integer yields a lower value then MAX.SO.FAR will simply remain the same. However, if this second integer value is higher than the sum of the first two integers, MAX.SO.FAR will only be the value of the second integer. This pattern will continue throughout the entire scan and keep track of the maximum sum which has been previously encountered. As MAX.SO.FAR continues to scan and update, MAX.INCLUDING.HERE retains maximum value for any sublist ends at the current position. As the scan moves further down the list, this value is replaced by the highest value of any sublist that ends in the current position. At each point, we can compare the MAX.SO.FAR and the MAX.INCLUDING.HERE and retain the highest collective similarity score at any point. MAX.INCLUDING.HERE accounts for the possibility that the highest score lies in a sublist which ends in the final value of the list so this method will guarantee you find the optimal region since every single possibility is checked. 

For a list that only contains one positive score, since adding two negative values would yield a lower score, the maximum value retained will simply be the highest of the negative numbers passed. Eventually, the scan will reach the singular positive value and retain this integer and the highest score. Since all values after this score are also negative, the max score will no change. The MAX.INCLUDING.HERE will continually change but the MAX.SO.FAR will remain the singular positive value and retaining the higher value of the two (the singular positive number) will ensure that this method works for this scenario. We also know this method works for positive sublists if multiple integers so this method is effective in all scenarios. 


d)
			10^2	   10^3	   10^4	     10^5    10^6   10^7   10^8Brute Force	      1.29-03   1.07E-01   10.39    1041.748   N/A    N/A    N/A				Divide & Conquer      2.95E-05  1.37E-04  1.45E-03   0.016   0.162  1.598   N/A  				Linear		      3.01E-05  2.54E-05  2.63E-03   0.029   0.291  2.914  29.369		

e)
			10^6	10^7	 10^8	    10^9    Brute Force	       ~1003  ~10,030  ~100,300  ~1,003,000			Divide & Conquer        N/A      N/A    ~15.98     ~159.8 				Linear		        N/A  	 N/A  	  N/A      ~293.7 	



f) 
Based on this data, I was able to make the following observations. 
For the Brute Force Algorithm, as the list length increases by factors of 10, the running time increases by roughly factors of 100. 
For the Divide and Conquer Algorithm, as the list length increase by factors of 10, the running time also increases roughly factors of 10.
For the Linear Algorithm, as the list length increase by factors of 10, the running time also increases roughly factors of 10.

