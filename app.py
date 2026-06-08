import streamlit as st 
import pandas as pd
from sklearn.model_selection import train_test_split 
st.set_page_config(page_title = "ML Regression App", page_icon = "🤖",layout= "wide")
st.title("ML Regression App")
st.subheader("Random Forest vs. kNN")
st.write("Diese App vergleicht zwei Machine-Learning-Modelle "
    "für eine Regressionsaufgabe.")
st.info("Projekt basiert auf dem praktischen Teil meiner Bachelorarbeit.")
st.header("1.Datensatz laden")
@st.cache_data
def load_data():
    data_path = "data/Concrete_Data.xlsx"
    df =pd.read_excel(data_path,sheet_name= "data")


    # Placeholder for actual data loading logic
    return df
df = load_data()
st.success("Datensatz erfolgreich geladen!")
st.write(" Datenvorschau:")
st.dataframe(df.head(5))
st.write("Datensatz-Informationen:")
col1,col2 = st.columns(2)

with col1:
    st.metric("Zeilen",value = df.shape[0])
    with col2:
        st.metric("Spalten",value = df.shape[1])


    st.write("Spaltennamen:")
    st.write(df.columns.tolist())
    #datenüberprufung 
    st.subheader("2.Datenüberprüfung")
    Fehlende_werte = df.isnull().sum().sum()
    Duplikate = df.duplicated().sum()
    col1,col2 = st.columns(2)
    with col1:
        st.metric(label="Fehlende Werte",value= int ( Fehlende_werte))

        
    with col2:
        st.metric(label="Duplikate",value= int ( Duplikate))

    st.write("Zielvariable:")
    st.code("Concrete compressive strength(MPa, megapascals)")
    st.header("3.Train-Test-Split")
    target_column = df.columns[-1]

    X = df.drop(columns=[target_column])
    y = df[target_column]

    st.write("Verwendete Zielvariable:")
    st.code(target_column)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size= 0.2,random_state= 42)
    col1,col2 = st.columns(2)
    with col1: 
        st.metric(label = "Trainingsdaten",value= X_train.shape[0])
        with col2:
            st.metric(label = "Testdaten",value= X_test.shape[0])
            st.success("Train/Test Split wurde erfolgreich durchgeführt.")


