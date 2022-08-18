realtime_dreamer
==============================

This Realtime Dreamer project is to use real Ecommerce data to perform NLP for Vietnamese language and machine learning tasks in order to settle a real-world business challenge of a company in Vietnam. We split our project into four tasks:


1.	Customer review type classification

Suwasit Wittayaijug used customer reviews to train Phobert pre-trained BERT model and then classify review types such as delivery, product, quality, and service. Performed model evaluation and produce visualizations.


2.	Sentiment analysis for customer reviews

Yunhong He used the keyword search method to select positive and negative customer reviews and label them after an eye scan. And then used these selected reviews with labels to train trituenhantaoio/bert-base-vietnamese-uncased pre-trained BERT model which will label the customer reviews with emotions such as positive, neutral, and negative. Performed model evaluation and visualizations for 3 different pre-trained BERT models including trituenhantaoio/bert-base-vietnamese-uncased, NlpHUST/vibert4news-base-cased, and bert-base-uncased, as well as Supervised Machine Learning algorithms. Setup team GitHub with folder structures. Produced sentiment analysis Machine Learning pipeline. /realtime_dreamer/sentiment_analysis.sh file is used to run the sentiment analysis pipeline.

Model performance focus on the F1 macro score due to the imbalanced label for the negative class. The best BERT model is defined as the pre-trained BERT model with the highest F1 macro score at the best epoch among 10 epochs. It is found that trituenhantaoio pre-trained BERT model outperformed other pre-trained BERT models. Therefore model generated by trituenhantaoio at one of the 10 epochs with the highest F1 score macro is chosen as sentiment_analysis_best_bert_model.model. The size of each BERT model is over 432MB which exceeds the GitHub limit of 25MB. Therefore, the BERT model can not be uploaded to GitHub. Below are the links to the sentiment analysis BERT models generated.

Links:
(1) The link to /models/sentiment_analysis_best_bert_model.model is https://drive.google.com/file/d/1ndzGpSsbzQ5mYRXkPMmzzg6bJmLLlD3q/view?usp=sharing

(2) The link to /models/sentiment_analysis_trituenhantaoio_train_data_provided_by_Yunhong He_NLP_Epoch10.model is  https://drive.google.com/file/d/1ffLZd2jr5CGxGweuBq2bcM6lzIca66JB/view?usp=sharing

Sample files:

(1) Customer review label dataset at C:\Users\heyun\Capstone\realtime_dreamer\data\processed\sentiment_analysis_reviews_label.xlsx is the small sample of the file '/content/drive/MyDrive/Realtime Dreamer/train reviews.xlsx' used in notebooks\Sentiment_Analysis_BERT_Model_Evaluation.ipynb. Column "emotion" is labeled by Yunhong He using the keyword search method to select positive and negative customer reviews after an eye scan.

(2) Customer reviews dataset at C:\Users\heyun\Capstone\realtime_dreamer\data\processed\Git_mockup_reviews_processed.xlsx is the small sample of the customer review file 'drive/MyDrive/Realtime Dreamer/Tefal Lazada Product Reviews in TTL202207_Updated_Good_Bad.xlsx' used in notebooks\Sentiment_Analysis_BERT_Model_Evaluation.ipynb. Column "Comment classified Type 1" is labeled by the Vietnamese team.

BERT model evaluation files:

Below evaluation files are generated in Sentiment_Analysis_BERT_Model_Evaluation.ipynb and Sentiment_Analysis_BERT_Model_Evaluation.zip, and are used to produce BERT model evaluation visualizations:

model_info.csv, sentiment_analysis_...accuracy_per_class_df.csv, sentiment_analysis_...eval_df.csv, sentiment_analysis_...eval_VnEmoLex_validated_df.csv,  sentiment_analysis_...accuracy_per_class_VnEmoLex_validated_df.csv, sentiment_analysis_...eval_before_oversample_df.csv, and sentiment_analysis_...accuracy_per_class_before_oversample_df.csv.


3.	Recommendation system

Kensuke Suzuki used user id, product, and customer rating to train the Memory-Based Collaborative Filtering model which will then recommend items to the user. “Users who are similar to you also liked…” Conducted model evaluation.


4.	Machine Learning for Sales Prediction

Zheng Wei Lim used E-Commerce data to train Supervised ML algorithms and conducted feature engineering. Performed model evaluation of multiple Supervised ML algorithms, and produce visualizations. 


Project Organization
------------

    ├── LICENSE
    ├── Makefile                <- Makefile with commands like `make data` or `make train`
    ├── README.md               <- The top-level README for developers using this project.
    ├── data
    │   ├── external            <- Data from third party sources.
    |   └── final               <- File with final data of the project
    |       
    |
    │   ├── interim             <- Intermediate data that has been transformed. Files are used in sentiment analysis BERT model evaluation
    |   |   └── sentiment_analysis_reivew_emotion_predition.xlsx
    |   |   └── sentiment_analysis_trituenhantaoio_train_data_from_Yunhong He_Epoch1_accuracy_per_class_df.csv
    |   |   └── sentiment_analysis_trituenhantaoio_Epoch1_train_data_from_Yunhong He_eval_df.csv
    |   |   └── model_info.csv
    |   |   └── sentiment_analysis_trituenhantaoio_train_data_provided_by_Yunhong He_NLP_Epoch10_accuracy_per_class_df.csv
    |   |   └── sentiment_analysis_trituenhantaoio_train_data_provided_by_Yunhong He_NLP_Epoch10_accuracy_per_class_before_oversample_df.csv
    |   |   └── sentiment_analysis_trituenhantaoio_train_data_provided_by_Suwasit_NLP_Epoch10_accuracy_per_class_df.csv
    |   |   └── sentiment_analysis_trituenhantaoio_NLP_Epoch10_train_data_provided_by_Yunhong He_eval_df.csv
    |   |   └── sentiment_analysis_trituenhantaoio_NLP_Epoch10_train_data_provided_by_Yunhong He_eval_before_oversample_df.csv
    |   |   └── sentiment_analysis_trituenhantaoio_NLP_Epoch10_train_data_provided_by_Suwasit_eval_df.csv
    |   |   └── sentiment_analysis_NlpHUST_train_data_provided_by_Yunhong He_NLP_Epoch10_accuracy_per_class_df.csv
    |   |   └── sentiment_analysis_NlpHUST_train_data_provided_by_Suwasit_NLP_Epoch10_accuracy_per_class_VnEmoLex_validated_df.csv
    |   |   └── sentiment_analysis_NlpHUST_train_data_provided_by_Suwasit_NLP_Epoch10_accuracy_per_class_df.csv
    |   |   └── sentiment_analysis_NlpHUST_NLP_Epoch10_train_data_provided_by_Yunhong He_eval_df.csv
    |   |   └── sentiment_analysis_NlpHUST_NLP_Epoch10_train_data_provided_by_Suwasit_eval_VnEmoLex_validated_df.csv
    |   |   └── sentiment_analysis_NlpHUST_NLP_Epoch10_train_data_provided_by_Suwasit_eval_df.csv
    |   |   └── sentiment_analysis_bert-base-uncased_train_data_provided_by_Yunhong He_NLP_Epoch10_accuracy_per_class_df.csv
    |   |   └── sentiment_analysis_bert-base-uncased_train_data_provided_by_Suwasit_NLP_Epoch10_accuracy_per_class_df.csv
    |   |   └── sentiment_analysis_bert-base-uncased_NLP_Epoch10_train_data_provided_by_Yunhong He_eval_df.csv
    |   |   └── sentiment_analysis_bert-base-uncased_NLP_Epoch10_train_data_provided_by_Suwasit_eval_df.csv
    |   |   
    |   |   
    |   |   
    |   |   
    │   ├── processed           <- The final, canonical data sets for modeling.
    │   │   └── Git_mockup_reviews_processed.xlsx
    │   │   └── sentiment_analysis_reviews_label.xlsx
    │   │   └── sentiment_analysis_reviews_label_processed.csv
    |   |   └── sentiment_analysis_reviews_label_split.csv
    |   |
    │   └── raw                 <- The original, immutable data dump.
    │       └── Git_mockup_reviews.xlsx
    | 
    |
    ├── docs                    <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models                  <- Trained and serialized models, model predictions, or model summaries 
    |   └── sentiment_analysis_best_bert_model.model  <- link for this model: https://drive.google.com/file/d/1ndzGpSsbzQ5mYRXkPMmzzg6bJmLLlD3q/view?usp=sharing
    │   └── sentiment_analysis_trituenhantaoio_train_data_provided_by_Yunhong He_NLP_Epoch10.model  <- link for this model:   
    |        https://drive.google.com/file/d/1ffLZd2jr5CGxGweuBq2bcM6lzIca66JB/view?usp=sharing
    |
    ├── notebooks               <- Jupyter notebooks. A naming convention is a number (for ordering),
    │   |                          the creator's name, and a short `-` delimited description, e.g.
    │   |                          `1.0-jqp-initial-data-exploration.
    |   └── Sentiment_Analysis_Supervised_Machine_Learning_colab.ipynb   <- Complete Reviews label dataset is run in this python notebook which can be run in Colab.
    |   └── Sentiment_Analysis_Supervised_Machine_Learning_Model_Evaluation_local.ipynb <- Complete Reviews label dataset is run in this python notebook
    |   └── Sentiment_Analysis_BERT_Model_Evaluation.ipynb <- Complete Reviews label dataset is run in this notebook which generates BERT models and evaluation figures. 
    |   └── Sentiment_Analysis_BERT_Model_Evaluation.zip  <- Using zip file to preserve the visualizations generated in Sentiment_Analysis_BERT_Model_Evaluation.ipynb 
    │
    ├── references              <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures             <- Generated graphics and figures to be used in reporting
    |       └── sentiment analysis - model evaluation by individual class prediction accuracy - visualization.png
    |       └── sentiment analysis - model evaluation by metrics - visualization.png
    |       └── sentiment analysis - model evaluation by pre-trained bert model - visualization.png
    |       └── sentiment analysis - supervised ml model evaluation - visualization.png
    |       └── sentiment analysis - imbalanced classes before oversampling - visualization.png
    │
    ├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
    │                              generated with `pip freeze > requirements.txt`
    │
    |── sentiment_analysis.sh   <- The bash file to run the sentiment_analysis pipeline.
    |
    ├── setup.py                <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                     <- Source code for use in this project.
    │   ├── __init__.py         <- Makes src a Python module
    │   │
    │   ├── data                <- Scripts to download or generate data
    │   │   └── sentiment_analysis_data_utility_functions.py
    |   |   └── sentiment_analysis_predict_emotion.py
    |   |   └── sentiment_analysis_prepare_review_label.py
    |   |   └── sentiment_analysis_utility_functions.py
    │   │
    │   ├── features            <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models              <- Scripts to train models and then use trained models to make
    │   │   │                      predictions
    │   │   ├── sentiment_analysis_train_bert_model.py 
    │   │   └── sentiment_analysis_utility_functions.py
    │   │
    │   └── visualization       <- Scripts to create exploratory and results-oriented visualizations
    │       
    │
    └── tox.ini                 <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
