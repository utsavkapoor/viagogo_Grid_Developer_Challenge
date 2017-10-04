How to run the Project:
1. Download both the files.
2. Run "grid_developer.py" using the following command:
python grid_developer.py
3. The console will ask you to input the coordinate separated by a single comma.
for example: 4,2
4. The Program will output the results.
5. file "grid_developer_same_distance.py" can be run the same way which shows the result

Assumptions:

1. Input given is separated only by a comma and nothing else.
2. Seed data generated only in between [-10,-10] to [10,10].
3. Seed data is generated only in JSON Format where each object contains coordinates of events, event id and Prices of tickets available. All the ticket Prices are between $10 to $100.
4. There are maximum of 10 tickets available at an event.
5. Only Events which have tickets available will be shown in the result. No event with 0 tickets available will be shown.

How might you change your program if you needed to support multiple events at the same location?

The Program grid_developer_same_distance.py handles the case of events with same distance and same location. If a location has multiple events, distance of events is same from User's position. Also, in this the dictionaries created will have event id as the key instead of coordinates. 
The answer produces the result where if the distance is same, events with cheapest ticket is shown.
This can be done by adding ticket prices as sorting parameter as done in line 62 [sorted(min_dist_keys, key=itemgetter(0,1))].

How would you change your program if you were working with a much larger world size?

In case of a larger world, we can change the method by which we are selecting the nearest 5 events. In both the cases we have to traverse the whole input once. which makes both the codes as O(n). Now in case we have to return 5 nearest elements we can just simple sort the list which we are using to maintain the nearest elements thus making its run time as O(klog(k)) where k is the number of elements which we have to return making the total run time to O(nklog(k)).
In case of larger worlds, we can use algorithms such as K- nearest Neighbours (kNN) which has the time complexity of O(nk) thus reducing the log(k) factor from the initial basic algorithm. Also if we increase k significatly we have to switch to K-nearest Neighbours algorithm.
