from textblob import TextBlob

# Example text
text = input("Type the sentence one wants to analyze its sentiment")

# Create TextBlob object
blob = TextBlob(text)

print("The sentence '{}' has a polarity score of {:.2f}".format(text, blob.sentiment.polarity))
print("The sentence '{}' has a subjectivity score of {:.2f}".format(text, blob.sentiment.subjectivity))

# Get polarity and subjectivity scores
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

# Classify sentiment based on scores
if polarity > 0:
    if subjectivity > 0.5:
        print("The sentence is Positive and subjective")
    else:
        print("The sentence is Positive and objective")
elif polarity < 0:
    if subjectivity > 0.5:
        print("The sentence is Negative and subjective")
    else:
        print("The sentence is Negative and objective")
else:
    print("The sentence is Neutral")


text1 = "Polarity is typically measured on a scale from -1 to 1"
text2 = "-1 represents the most negative sentiment and 1 represents the most positive sentiment."
text3 = "Subjectivity is typically measured on a scale from 0 to 1"
text4 = "0 represents the most objective text and 1 represents the most subjective text"

print("VOCAB NOTES:\n{} \n{} \n{} \n{}".format(text1, text2, text3, text4))
