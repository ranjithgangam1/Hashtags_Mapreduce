# Hashtags_Mapreduce
# Hashtags_Mapreduce

##This map reduce program runs on twitter data collected for last one year. This program do the following thing
##For each day of the week, what was the most mentioned hashtag? Hour of the day?

###Approach:

I chose streaming-mode. I have done Map and Reduce jobs in python. I have used two maps and two reducers to find the required output. To find each day of the week, I wrote map_twit.py and red_twit.py and to find hour of the day, I wrote map_hr.py and red_hr.py files.

###Mapper explanation:

Mapper reads each tweet from HDFS file system and checks for “created at” key and also for “hashtags” which is in “entities”. One map takes the day and other takes the hour from the datetime package and send it to corresponding reducers where here both reducers are same.

###Mapper output:

First Map job output: &lt;day&gt;\t&lt;hashtag&gt;

Example mapper output:

Wed MG3

Tue OTR

Second Map job output: &lt;hour&gt;\t&lt;hashtag&gt;

Example mapper output:

02 winning

21 blackfish

###Reducer explanation:

Reducer will get the input of day/hour along with hashtag of the day/hour in two different reducers and then they count which hashtag repeats more times for each day/hour and for the day/hour which hashtag has highest count will get displayed.

Reducer output &lt;day/hour&gt; &lt;’hashtag\n’, count&gt;

Output:

Created a run6.sh file to run the application using the mentioned commands in the lecture in

it.

Reducer output from HDFS is stored in the “output6” and “output62” folders.

Example output:

Wed (‘dog\n’, 21401)

02 (‘winning\n’ 5997)

Note: Two different reducers are used for this program, it can also be done using single reducer. Passing two map jobs to a single reduce job.
