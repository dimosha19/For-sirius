import pandas as pd
import matplotlib.pyplot as plt
import category_encoders as ce
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = 'cars_dataset.csv'

df = pd.read_csv(data, delimiter=',')


def plot_maker():
    counts = {'unacc': df['car'].value_counts()["unacc"],
              'acc': df['car'].value_counts()["acc"],
              'good': df['car'].value_counts()["good"],
              'vgood': df['car'].value_counts()["vgood"]}

    plt.bar(counts.keys(), counts.values())
    plt.title(label='Зависимость количества машин от значения целевого признака')
    plt.show()


def decision_tree():

    x = df.drop(['car'], axis=1)
    y = df['car']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

    encoder = ce.one_hot.OneHotEncoder()

    x_train = encoder.fit_transform(x_train)

    x_test = encoder.transform(x_test)

    model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)
    model.fit(x_train, y_train)

    y_pred_model = model.predict(x_test)
    print("Model accuracy => ", accuracy_score(y_test, y_pred_model))

    print('Training set score => ', model.score(x_train, y_train))

    print('Test set score => ', model.score(x_test, y_test))


plot_maker()
decision_tree()
