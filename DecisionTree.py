from sklearn.datasets import load_iris  
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree  
from sklearn.model_selection import train_test_split  
from sklearn.metrics import accuracy_score  
import matplotlib.pyplot as plt  
# Step 1: Load the data (Iris dataset)  
data = load_iris()  
X = data.data  # Features  
y = data.target  # Labels  
# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  
# Step 3: Train the Decision Tree Classifier  
clf = DecisionTreeClassifier()  # Default parameters  
clf.fit(X_train, y_train)  
# Step 4: Validate the model  
y_pred = clf.predict(X_test)  
accuracy = accuracy_score(y_test, y_pred)  
print(f"Accuracy of Decision Tree Classifier: {accuracy * 100:.2f}%")  
# Step 5: Print the decision tree as text  
tree_rules = export_text(clf, feature_names=data.feature_names)  
print("\nDecision Tree Rules:")  
print(tree_rules)  
# Step 6: Visualize the decision tree as a plot  
plt.figure(figsize=(12, 8))  
plot_tree(clf, feature_names=data.feature_names, class_names=data.target_names, filled=True)  
plt.show() 