# Machine-learning
Problem 1 Write a web scraping script which takes an input of any film actor and gives the output of filmography of that actor in descending order. Use web scraping method Eg : input [Leonardo DiCaprio] Output : Films done by Leonardo DiCaprio in descending order.
Time Limit:1 Day 
Problem 2 Given a list of planets discovered by KEPLER. Kepler Data: https://drive.google.com/drive/folders/1GwqC4STc_KgVPofacQUzKHBMHQsmflvY?usp=sha ring Create an ML algorithm to classify the planets as Candidate/False positive/Confirmed etc based on the column “koi_disposition”. 
Time Limit:1 Day
Sub-questions for Problem 2 Why did you choose the particular algorithm?
What are the different tuning methods used for the algorithm? 
Did you consider any other choice of algorithm?Why or why not? 
What is the accuracy? 
What are the different types of metrics that can be used to evaluate the model?
------------------------------------------------------solution-----------------------------------------------------------------------------------------------------------
Why did you choose the particular algorithm?
I have chosen Random Forest Classifier for many reasons:

1.)Flexibility: Random forests can be used for both classification and regression tasks which make it versatile.

2.)Accuracy: Random forests usually perform well in practice and it is less likely to overfit compared to decision trees.

3.)Feature Importance: Random forests can provide a feature importance score, which can be useful for feature selection.

4.)Ensemble Method: Random forests are an ensemble learning method, which combines multiple decision trees to produce a more robust and accurate model.

What are the different tuning methods used for the algorithm?

For RandomForestClassifier, there are several tuning parameters that can be adjusted to optimize the model:

n_estimators: The number of trees in the forest. Increasing this number generally improves the model's performance but also increases the computation time.
max_depth: The maximum depth of the tree. Increasing this parameter can make the model more complex and may lead to overfitting.
min_samples_split: The minimum number of samples required to split an internal node.
min_samples_leaf: The minimum number of samples required to be at a leaf node.
max_features: The number of features to consider when looking for the best split.
In the provided code, I used n_estimators=100 and random_state=42 as initial tuning parameters. However, these parameters can be further optimized using techniques like grid search or random search.

Did you consider any other choice of algorithm? Why or why not?
Yes, other algorithms could have been considered for this classification task:

Logistic Regression: A simple and interpretable algorithm suitable for binary classification tasks. However, it might not perform as well as RandomForest for complex datasets.
Support Vector Machine (SVM): A powerful algorithm for classification tasks, especially for high-dimensional data. SVM can capture complex relationships in the data but may require more computational resources.
Gradient Boosting Machines: Ensemble learning methods that can provide higher accuracy compared to Random Forests but are more prone to overfitting and require careful tuning.
I chose RandomForest for its balance of simplicity, interpretability, and performance.

What is the accuracy?
The accuracy score of the RandomForestClassifier on the test set is printed at the end of the code using accuracy_score(y_test, y_pred).

What are the different types of metrics that can be used to evaluate the model?

Various metrics can be used to evaluate the performance of a classification model:

1.)Accuracy: The ratio of correctly predicted instances to the total instances.
2.)Precision: The ratio of true positives to the sum of true positives and false positives. It measures the model's ability to correctly identify positive samples.
3.)Recall (Sensitivity): The ratio of true positives to the sum of true positives and false negatives. It measures the model's ability to capture all positive samples.
4.)Confusion Matrix: A table used to describe the performance of a classification model on a set of test data, which can be used to calculate various metrics.

In the provided code, I used classification_report, confusion_matrix, and accuracy_score from scikit-learn, which provide detailed information on precision, recall and accuracy.






