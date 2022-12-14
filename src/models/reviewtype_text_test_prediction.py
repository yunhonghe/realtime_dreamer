# -*- coding: utf-8 -*-
"""reviewType_text_test_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sxHEcAsuURY0KUikQ4q5bmxbhJxt4VgO
"""

import reviewtype_utility_functions as rcuf
import pandas as pd
import torch
from transformers import BertTokenizer, logging
from transformers import AutoModel, AutoTokenizer

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

hidden_dropout_prob = 0.4
attention_probs_dropout_prob = 0.1
pre_trained_model = 'vinai/phobert-base'
model_type = pre_trained_model.split('/')[0]
batch_size = 8
epochs = 20
Ir = 1e-5
eps = 1e-8
tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")

label_dict={'Product':0, 'Quality':1, 'Logistic':2, 'Sale':3, 'Service':4}
label_dict_inverse = {v: k for k, v in label_dict.items()}

model = rcuf.build_Bert_model(pre_trained_model, attention_probs_dropout_prob, hidden_dropout_prob)


def predict_text(input_text):
  inputs = tokenizer(input_text.lower(), return_tensors = "pt").to(device)
  with torch.no_grad():
      logits = model(**inputs).logits

  predicted_class_id = logits.argmax().item()
  return label_dict_inverse[predicted_class_id]



model_path = 'data/final/reviewtype_phobert_model.pt'
model = torch.load(model_path)
model.eval()



def prepare_review_data(review_df):
    review_df = review_df.reset_index()
    review_df_1 = review_df[['index', 'Review Content', 'Rating']].dropna(how='any')
    print("raw review dataset after dropping null value:", review_df_1.shape)
    return review_df, review_df_1

def generate_predition_data(df):
    review_df, review_df1 = prepare_review_data(df)
    review_df1['emotion'] = review_df1['Review Content'].apply(predict_text)
    review_emotion_prediction = pd.merge(review_df, review_df1[['index', 'emotion']], how='left', on='index')
    return review_emotion_prediction

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Test.')
    parser.add_argument('text', action='store', type=str, help='The text to parse.')
    args = parser.parse_args()
    input_text = args.text
    print("Predict review type : ",predict_text(input_text ))
