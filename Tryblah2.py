

import sys
import os
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score,recall_score
def usage():
    print("Usage:")
    print("python %s <data_dir>" % sys.argv[0])

if __name__ == '__main__':

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    data_dir = sys.argv[1]
    classes = ['pos', 'neg']

    # Read the data
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    person=input('DO You want to give custom Input? Input 1 for Yes, 0 for No')
    label=raw_input('Is Input positive or negative?Input neg for negative and pos for positive')
    if person==1:
    	for curr_class in classes:
        	dirname = os.path.join(data_dir, curr_class)
        	for fname in os.listdir(dirname):
            		with open(os.path.join(dirname, fname), 'r') as f:
                		content = f.read()
                		if fname.startswith('cv999_14636'):
					if curr_class=='neg':
                    				test_data.append(content)
                    				test_labels.append(label)
					else:
						train_data.append(content)
                    				train_labels.append(curr_class)3
						
                		else:
                    			train_data.append(content)
                    			train_labels.append(curr_class)
    else:
    	for curr_class in classes:
        	dirname = os.path.join(data_dir, curr_class)
        	for fname in os.listdir(dirname):
            		with open(os.path.join(dirname, fname), 'r') as f:
                		content = f.read()
                		if fname.startswith('cv9'):
                    			test_data.append(content)
                    			test_labels.append(curr_class)
                		else:
                    			train_data.append(content)
                    			train_labels.append(curr_class)
    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf=True,decode_error='ignore')
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)

    # Perform classification with SVM, kernel=rbf
   
    t0 = time.time()
   
    t1 = time.time()
    
    classifier_rbf = KNeighborsClassifier()
    classifier_rbf.fit(train_vectors, train_labels)
    prediction_rbf = classifier_rbf.predict(test_vectors)
    
    t2 = time.time()
    time_rbf_train = t1-t0
    time_rbf_predict = t2-t1


    # Print results in a nice table
    print("Results for K Nearest Neighbours")
    print("Training time: %fs; Prediction time: %fs" % (time_rbf_train, time_rbf_predict))
    print(classification_report(test_labels, prediction_rbf))
    if accuracy_score(test_labels,prediction_rbf)==1:
	print("Negative!")
    if accuracy_score(test_labels,prediction_rbf)==0:
	print("Positive")
