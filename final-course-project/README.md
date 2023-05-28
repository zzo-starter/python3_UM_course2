### PART1 Twitter Tweet Sentiment Classifier
We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)



# NOTICE
 !!!! files where copied from browser; and in incorrect format; thus not functional here; files need reformatting.



### PART 2
Instructions for Submission: 
Using the resulting .csv file from your answers to part one of the Sentiment Classifier project, create a scatterplot of the Number of Retweets vs the Net Score using Excel, Google Sheets, or another software package of your choosing. Review the Introductory video for this project if you are unsure of how the graph should look, approximately. Be sure to correctly label your axes and give it a meaningful title! You will upload a screenshot of your scatterplot for submission, and review 3 other submissions to check other students work.

Review criteria
Instructions for Grading: You will be reviewing other students’ submissions to make sure that they have correctly constructed the scatterplot of Number of Retweets vs Net Score. 

For the scatterplot that your peer submitted, you will check to see if the following characteristics are true:

1 The X axis represents the Net Score. 
2 The Y axis represents the Number of Retweets.
3 The data appear as expected.

