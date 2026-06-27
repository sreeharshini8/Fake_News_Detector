📰 Fake News Detection Using Machine Learning

📌 Project Overview

Fake News Detection is a Machine Learning-based application developed to classify news headlines as Real News or Fake News. The system uses Natural Language Processing (NLP) techniques and a Logistic Regression model to analyze the given news text and predict its authenticity.

---

🎯 Objective

The main objective of this project is to identify and classify fake news articles by analyzing textual content using Machine Learning techniques.

---

🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- TF-IDF Vectorizer
- Logistic Regression

---

📂 Project Structure

FakeNewsDetector/
│
├── app.py
├── train.py
├── model.pkl
├── vectorizer.pkl
├── README.md


---

📊 Dataset

Dataset used:

Fake and Real News Dataset

Source:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

The dataset contains:

- Fake News Articles
- Real News Articles

Labels:

- 0 → Fake News
- 1 → Real News

---

⚙️ Methodology

Step 1: Data Collection

The Fake and Real News dataset was collected from Kaggle.

Step 2: Data Preprocessing

The dataset was cleaned and prepared for training.

Step 3: Feature Extraction

TF-IDF Vectorizer was used to convert textual data into numerical feature vectors.

Step 4: Model Training

A Logistic Regression classifier was trained using the processed dataset.

Step 5: Model Saving

The trained model and vectorizer were saved as:

- model.pkl
- vectorizer.pkl

Step 6: Web Application Development

A user-friendly Streamlit interface was developed for prediction.

---

🚀 How to Run the Project


Train the Model

python train.py

Run the Application

streamlit run app.py

---

🖥 Application Workflow

User enters a news headline

↓

TF-IDF Vectorizer converts text into numerical features

↓

Logistic Regression Model predicts the result

↓

Output displayed as:

- ✅ Real News
- ❌ Fake News

---

📈 Results

The application successfully predicts whether a news headline is real or fake using Machine Learning techniques and NLP-based text processing.
<img width="789" height="332" alt="image" src="https://github.com/user-attachments/assets/264df083-4228-404f-b701-7c4a6ca9325d" />

---

🔮 Future Enhancements

- Deep Learning Models
- Real-time News Verification
- News URL Analysis
- Multilingual News Detection
- Enhanced User Interface

---

👩‍💻 Developed By
JAGARLAMUDI SREE HARSHINI

B.Tech – Artificial Intelligence and Data Science

---

📜 Conclusion

This project demonstrates the use of Machine Learning and Natural Language Processing techniques for identifying fake news. The developed system provides a simple and efficient way to classify news content and helps users identify potentially misleading information.
