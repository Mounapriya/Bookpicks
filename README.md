# Bookpicks
# Book Recommendation System

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.x+-green)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x+-orange)](https://scikit-learn.org/stable/)
[![pandas](https://img.shields.io/badge/pandas-1.x+-blueviolet)](https://pandas.pydata.org/)

![Demo of the Book Recommendation App](https://github.com/Mounapriya/Bookpicks/blob/main/Img.gif)

This project is a web-based book recommendation system built using Python, Flask, and machine learning techniques. It allows users to enter a book title and receive a list of similar books based on content analysis.

## Table of Contents

-   [Features](#features)
-   [Usage](#usage)
-   [Technical Details](#technical-details)
-   [Data Source](#data-source)
-   [Future Enhancements](#future-enhancements)
-   [Contributing](#contributing)


## Features

*   **Book Search:** Users can search for books by title using an auto-complete search box.
*   **Recommendation Engine:** The system uses TF-IDF vectorization and cosine similarity to recommend similar books.
*   **User-Friendly Interface:** A clean and intuitive web interface built with Flask and Bootstrap.
*   **Error Handling:** Provides informative error messages if a book is not found in the dataset.

## Usage

1.  Run the Flask application:

    ```bash
    python app.py
    ```

2.  Open your web browser and navigate to `http://127.0.0.1:5000/`.
3.  Enter a book title in the search box and click "Get Recommendations".

## Technical Details

This project uses a combination of frontend and backend technologies:

*   **Frontend:** The user interface is built using HTML for structure, CSS for styling, and client-side JavaScript for interactive elements like the auto-complete search box. Bootstrap is used for responsive design and styling.
*   **Backend:** The backend logic, including data loading, preprocessing, recommendation engine, and API endpoints, is implemented in Python using the Flask framework.
*   **Recommendation Engine:**
    1.  **Data Preprocessing:** The book data (title, author, publisher, language code) is combined into a single "tags" field.
    2.  **TF-IDF Vectorization:** The TF-IDF (Term Frequency-Inverse Document Frequency) algorithm is used to convert the text data into numerical vectors.
    3.  **Cosine Similarity:** Cosine similarity is calculated between the vectors to determine the similarity between books.
    4.  **Recommendations:** The top 5 most similar books are returned as recommendations.

## Data Source

The book data is sourced from the [Goodreads-Books dataset on Kaggle](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks). This dataset contains information about books from Goodreads, including titles, authors, ISBNs, ratings, and other metadata.

## Future Enhancements

*   Improve the recommendation algorithm (e.g., using collaborative filtering or other advanced techniques).
*   Add user authentication and personalized recommendations.
*   Implement a more visually appealing user interface.
*   Expand the dataset to include more books or other book-related information (e.g., genres, reviews).
*   Implement fuzzy matching for book titles to handle typos and partial matches.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

