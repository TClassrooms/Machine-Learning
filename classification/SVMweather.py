import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



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




y_pred = svclassifier.predict(X_test)


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))













#contains 
def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plot_confusion_matrix(y_test, y_pred, classes=y,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plot_confusion_matrix(y_test, y_pred, classes=y, normalize=True,
                      title='Normalized confusion matrix')


