# Text-Summarization

Clone Project

git clone https://github.com/joey234/Text-Summarization.git

cd Text-Summarization


Pre-trained model link: 

Download pre-trained model and put it inside 

Text-Summarization/log

How to run

Python version 3.x

Install Python packages:

pip install -r requirements.txt


Install CUDA and CuDNN

-CUDA 8.0

-CuDNN 5.1

Install Standford CoreNLP

_ Download Standford CoreNLP

wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip

_ Extract the .zip file to Text-Summarization folder
 
Install Spacy model

run the following commands

python -m spacy download en

python -m spacy link en_core_web_sm en


Please put test set (including text files) into the folder Text-Summarization/stories/

Run

python TextSummarization.py ./stories

Result is in folder Text-Summarization/output
