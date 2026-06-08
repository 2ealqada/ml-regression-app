import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
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
    original_rows = df.shape[0]
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()
    cleaned_rows = df.shape[0]
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
            
st.subheader("1. Random Forest Modell")

if st.button("Random Forest trainieren"):
    rf_base_model = RandomForestRegressor(random_state=42)

    param_grid = {
        "n_estimators": [50, 100, 200, 300],
        "max_depth": [None, 10, 20, 30, 40, 50],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    }

    rf_search = RandomizedSearchCV(
        estimator=rf_base_model,
        param_distributions=param_grid,
        n_iter=50,
        cv=10,
        scoring="neg_mean_absolute_error",
        random_state=42,
        n_jobs=-1
    )

    with st.spinner("Random Forest Modell wird trainiert und optimiert..."):
        rf_search.fit(X_train, y_train)

    best_rf_model = rf_search.best_estimator_

    y_pred_rf = best_rf_model.predict(X_test)

    mae_rf = mean_absolute_error(y_test, y_pred_rf)
    rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
    r2_rf = r2_score(y_test, y_pred_rf)

    st.success("Random Forest Modell erfolgreich trainiert!")

    st.subheader("Beste Hyperparameter")
    st.write(rf_search.best_params_)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="MAE", value=round(mae_rf, 2))

    with col2:
        st.metric(label="RMSE", value=round(rmse_rf, 2))

    with col3:
        st.metric(label="R²", value=round(r2_rf, 2))
st.subheader("2. kNN Modell")

if st.button("kNN trainieren"):
    knn_pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("knn_model", KNeighborsRegressor())
    ])

    knn_param_grid = {
        "knn_model__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 30],
        "knn_model__weights": ["uniform", "distance"],
        "knn_model__metric": ["euclidean", "manhattan"]
    }

    knn_search = GridSearchCV(
        estimator=knn_pipeline,
        param_grid=knn_param_grid,
        cv=10,
        scoring="neg_mean_absolute_error",
        n_jobs=-1
    )

    with st.spinner("kNN Modell wird trainiert und optimiert..."):
        knn_search.fit(X_train, y_train)

    best_knn_model = knn_search.best_estimator_

    y_pred_knn = best_knn_model.predict(X_test)

    mae_knn = mean_absolute_error(y_test, y_pred_knn)
    rmse_knn = np.sqrt(mean_squared_error(y_test, y_pred_knn))
    r2_knn = r2_score(y_test, y_pred_knn)

    st.success("kNN Modell erfolgreich trainiert!")

    st.subheader("Beste Hyperparameter")
    st.write(knn_search.best_params_)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="MAE", value=round(mae_knn, 2))

    with col2:
        st.metric(label="RMSE", value=round(rmse_knn, 2))

    with col3:
        st.metric(label="R²", value=round(r2_knn, 2))
st.header("4. Modellvergleich")

if st.button("Beide Modelle trainieren und vergleichen"):

    # Random Forest
    rf_base_model = RandomForestRegressor(random_state=42)

    rf_param_grid = {
        "n_estimators": [50, 100, 200, 300],
        "max_depth": [None, 10, 20, 30, 40, 50],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    }

    rf_search = RandomizedSearchCV(
        estimator=rf_base_model,
        param_distributions=rf_param_grid,
        n_iter=50,
        cv=10,
        scoring="neg_mean_absolute_error",
        random_state=42,
        n_jobs=-1
    )

    # kNN
    knn_pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("knn_model", KNeighborsRegressor())
    ])

    knn_param_grid = {
        "knn_model__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 30],
        "knn_model__weights": ["uniform", "distance"],
        "knn_model__metric": ["euclidean", "manhattan"]
    }

    knn_search = GridSearchCV(
        estimator=knn_pipeline,
        param_grid=knn_param_grid,
        cv=10,
        scoring="neg_mean_absolute_error",
        n_jobs=-1
    )

    with st.spinner("Beide Modelle werden trainiert und optimiert..."):
        rf_search.fit(X_train, y_train)
        knn_search.fit(X_train, y_train)

    best_rf_model = rf_search.best_estimator_
    best_knn_model = knn_search.best_estimator_

    y_pred_rf = best_rf_model.predict(X_test)
    y_pred_knn = best_knn_model.predict(X_test)

    mae_rf = mean_absolute_error(y_test, y_pred_rf)
    rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
    r2_rf = r2_score(y_test, y_pred_rf)

    mae_knn = mean_absolute_error(y_test, y_pred_knn)
    rmse_knn = np.sqrt(mean_squared_error(y_test, y_pred_knn))
    r2_knn = r2_score(y_test, y_pred_knn)

    results_df = pd.DataFrame({
        "Modell": ["Random Forest", "kNN"],
        "MAE": [mae_rf, mae_knn],
        "RMSE": [rmse_rf, rmse_knn],
        "R²": [r2_rf, r2_knn]
    })

    st.success("Modellvergleich wurde erfolgreich erstellt.")

    st.subheader("Vergleich der Modelle")
    st.dataframe(results_df.round(3))
    
    st.subheader("Beste Hyperparameter")

    st.write("Random Forest:")
    st.write(rf_search.best_params_)

    st.write("kNN:")
    st.write(knn_search.best_params_)

    st.subheader("5. Prediction vs. Real")

    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred_rf, label="Random Forest", alpha=0.7)
    ax.scatter(y_test, y_pred_knn, label="kNN", alpha=0.7)

    min_value = min(y_test.min(), y_pred_rf.min(), y_pred_knn.min())
    max_value = max(y_test.max(), y_pred_rf.max(), y_pred_knn.max())

    ax.plot([min_value, max_value], [min_value, max_value], linestyle="--")

    ax.set_xlabel("Reale Werte")
    ax.set_ylabel("Vorhergesagte Werte")
    ax.set_title("Prediction vs. Real")
    ax.legend()

    st.pyplot(fig)
