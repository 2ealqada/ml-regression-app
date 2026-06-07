import streamlit as st 
import pandas as pd
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
    st.subheader("Datenüberprüfung")
    Fehlende_werte = df.isnull().sum().sum()
    Duplikate = df.duplicated().sum()
    col1,col2 = st.columns(2)
    with col1:
        st.metric(label="Fehlende Werte",value= int ( Fehlende_werte))

        
    with col2:
        st.metric(label="Duplikate",value= int ( Duplikate))

    st.write("Zielvariable:")
    st.code("Concrete compressive strength(MPa, megapascals)")

