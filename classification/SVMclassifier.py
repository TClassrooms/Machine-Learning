# SVM como uma máquina da classificação

from sklearn import svm
from sklearn import datasets
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split


#Importando o conjunto de dados

iris= datasets.load_iris()

#print(type(iris))

#visualiza as classes dos dados de entrada
print(iris.feature_names)
#visualiza os dados de entrada
print(iris.data)
#Visualiza o alvo de treinamento
print(iris.target)
#Visualiza os nomes dos alvos de treinamento
print(iris.target_names)


# seleciona a propriedade de trabalho (dado de entrada):

X = iris.data[:,2]

# Seleciona o alvo da predição (atributo):

y=iris.target

# Divide o dado em dois subconjutos: o primeiro de validação e o segundo de treinamento

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2)#, radom_state=42)

# Cria o modelo

model = svm.SVC(kernel='linear')

# Ajusta o modelo

#model.fit(X_train, y_train)

