###################################################################################
######################### A SUPPORT VECTOR MACHINE PROGRAM ########################
###################################################################################

#Importando pacotes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'modules/')
import iplots as mfun 



###################################################################################
#--------------------------- LEITURA E VISUALIZAÇÃO ------------------------------#
###################################################################################

# lendo o dado:

bankdata = pd.read_csv("input/bill_authentication.csv")

# Avaliando a dimensão do dado:

print(bankdata.shape)

# Verificando algumas linhas do dado:

print(bankdata.head())

###################################################################################
#------------------------------ PRÉ-PROCESSAMENTO---------------------------------#
###################################################################################

# A etapa de pré-processamento consiste em duas etapas: a primeira delas consiste 
#em dividir o dado total em atributos classificáveis e em dados etiquetados, a se-
#gunda consiste em dividir o dado em dado de treinamento e validação.

X = bankdata.drop('Class', axis=1)
y = bankdata['Class']

# Nesta operação o dado foi dividido da seguinte maneira. Na variável "X", estão
#armazenadas as informações referente a aquisição dos dados (atributos). Na variá-
#vel "y", estão armazenados as informações sobre as classes do dado (etiquetas).

# Na segunda parte do pré-processamento, será utilizada a função "model_selection"
# do Scikit-Learn que contém o método de separação "train_test_split", que reali-
#zará a performace de separação do dado em um conjunto de treinamento e validação.

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)


###################################################################################
#-------------------------------- TREINAMENTO ------------------------------------#
###################################################################################


# Na etapa anterior, o dado foi divido em um subconjunto de validação e treinamento 
#o conjunto de treinamento será utilizado para treinar a SVM e o subconjunto de va-
#lidação será utilizado para avaliar o treinamento. 





from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)



###################################################################################
#-------------------------------- CLASSIFICAÇÃO ----------------------------------#
###################################################################################

# Nesta etapa, classifica o conjunto de entrada do dado a ser classificado com base 
#no modelo de SVM já treinado na fase anterior. O resultado da classificação é feita
#com base na matriz de confusão. 


y_pred = svclassifier.predict(X_test)


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))





# Visualização gráfica dos resultados:

# Plot non-normalized confusion matrix
mfun.plot_confusion_matrix(y_test, y_pred, classes=y,title='Confusion matrix, without normalization')

plt.show()

# Plot normalized confusion matrix
mfun.plot_confusion_matrix(y_test, y_pred, classes=y, normalize=True,title='Normalized confusion matrix')

plt.show()


