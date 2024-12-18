from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Flask app
app = Flask(__name__)

# Load and preprocess data
df1 = pd.read_csv("books.csv", on_bad_lines='skip')
df1['tags'] = df1['title'] + ' ' + df1['authors'] + ' ' + df1['language_code'] + ' ' + df1['publisher']

# Initialize vectorizer and calculate similarity
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df1['tags'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

@app.route('/')
def home():
    books = df1['title'].tolist()
    return render_template('home.html', books=books)

@app.route('/recommend', methods=['POST'])
def recommend_books():
    data = request.json
    book_title = data.get('title', '').strip()
    
    if not book_title or book_title not in df1['title'].values:
        return jsonify({"error": "Book not found in the dataset."})

    idx = df1[df1['title'] == book_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    
    recommendations = df1.iloc[book_indices][['title', 'authors', 'publisher']].to_dict('records')
    return jsonify(recommendations)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
