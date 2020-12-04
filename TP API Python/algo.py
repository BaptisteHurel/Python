df = pd.read_csv("./data/labels.csv", usecols=['class', 'tweet'])
df['tweet'] = df['tweet'].apply(lambda tweet: re.sub('[^A-Za-z]+', ' ', tweet.lower()))

#labels du fichier tweets
# 0 - hate speech 1 - offensive language 2 - neither

@app.route(/predict)

def predict()

return {class1: p1,class2:p2,class3:p3}
