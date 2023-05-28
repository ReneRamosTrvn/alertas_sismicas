<<<<<<< HEAD
# Importar librerias
import pandas as pd
import streamlit as st
import pickle

# Extrae archvio pickle
with open('ML\model_K-Means.pkl', 'rb') as en:
    modelo = pickle.load(en)

# Funcion para clasificar peligrosidad del sismo
def clasificar(num):
    if num == 0:
        return 'Peligrosidad Baja'
    elif num == 1:
        return 'Peligrosidad Media'
    else:
        return 'Peligrosidad Alta'

def main():
    st.title('Clasificador de peligrosidad de un sismo')
    st.sidebar.header('Caracteristicas de entrada')

    def input_parametros():
        depth = st.sidebar.slider('Profundidad', 0, 25, 120)
        mag = st.sidebar.slider('Magnitud', 1, 4, 8)
        rms = st.sidebar.slider('Amplitud de onda', 0, 20, 40)

        data ={'depth': depth,
               'mag': mag,
               'rms': rms}
        
        feature = pd.DataFrame(data, index=[0])
        return feature
    df = input_parametros()


    st.write(df)
    st.button('RUN')
    st.success(clasificar(modelo.predict(df)[0]))

if __name__ == '__main__':
    main()


# Importar librerias
import pandas as pd
import streamlit as st
import pickle

# Extrae archvio pickle
with open('ML\model_K-Means.pkl', 'rb') as en:
    modelo = pickle.load(en)

# Funcion para clasificar peligrosidad del sismo
def clasificar(num):
    if num == 0:
        return 'Peligrosidad Baja'
    elif num == 1:
        return 'Peligrosidad Media'
    else:
        return 'Peligrosidad Alta'

def main():
    st.title('Clasificador de peligrosidad de un sismo')
    st.sidebar.header('Caracteristicas de entrada')

    def input_parametros():
        depth = st.sidebar.slider('Profundidad', 0, 25, 120)
        mag = st.sidebar.slider('Magnitud', 1, 4, 8)
        rms = st.sidebar.slider('Amplitud de onda', 0, 20, 40)

        data ={'depth': depth,
               'mag': mag,
               'rms': rms}
        
        feature = pd.DataFrame(data, index=[0])
        return feature
    df = input_parametros()


    st.write(df)
    st.button('RUN')
    st.success(clasificar(modelo.predict(df)[0]))

if __name__ == '__main__':
    main()

>>>>>>> a6014168fa101215e69423c5d098eaf0a4b35d5b
