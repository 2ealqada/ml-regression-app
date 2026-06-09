

# ML Regression App

Eine Streamlit-Web-App zum Vergleich von Random Forest und k-Nearest Neighbor für Regressionsaufgaben.

Das Projekt basiert auf meiner Bachelorarbeit zum Vergleich verschiedener Regressionsverfahren auf dem Concrete Compressive Strength Dataset.

## Ziel des Projekts

Die App zeigt, wie Machine-Learning-Modelle für eine Regressionsaufgabe trainiert, optimiert und bewertet werden können.

Der Fokus liegt auf dem Vergleich von:

Random Forest Regressor
k-Nearest Neighbor Regressor


## Funktionen

- Concrete-Datensatz aus Excel laden
- Datenvorschau anzeigen
- fehlende Werte prüfen
- Duplikate erkennen und entfernen
- Train/Test Split durchführen
- Random Forest mit RandomizedSearchCV optimieren
- kNN mit GridSearchCV optimieren
- MAE, RMSE und R² berechnen
- Modellvergleich als Tabelle anzeigen
- Prediction vs. Real Diagramm anzeigen
- Feature Importance für Random Forest anzeigen
- Metriken als Balkendiagramm darstellen
- kurze Interpretation der Ergebnisse anzeigen

## Technologien

- Python
- Streamlit
- Pandas
- scikit-learn
- Matplotlib
- openpyxl
- NumPy

## Machine-Learning-Workflow
1. Datensatz laden
2. Daten prüfen
3. Duplikate entfernen
4. Features und Zielvariable trennen
5. Train/Test Split durchführen
6. Random Forest trainieren und optimieren
6. kNN trainieren und optimieren
7. Modelle bewerten
8. Ergebnisse visualisieren
9. Ergebnisse interpretieren


## Modelle

### Random Forest
Random Forest wird mit RandomizedSearchCV optimiert.

Getestete Hyperparameter:

- n_estimators
- max_features
- max_depth
- min_samples_split
- min_samples_leaf

### kNN
kNN wird mit einer Pipeline trainiert.

Die Pipeline besteht aus:

StandardScaler
KNeighborsRegressor

kNN wird mit GridSearchCV optimiert.

Getestete Hyperparameter:

- n_neighbors
- weights
- metric

## Bewertungsmetriken
Die Modelle werden mit folgenden Metriken bewertet:

- MAE
- RMSE
- R²

## Projektstruktur
```text
ml-regression-app/
   ├── app.py 
   ├── requirements.txt
   ├── data/
   │ └── Concrete_Data.xlsx 
   ├── images/ 
   ├── models/ 
   └── docs/ 
         ├── use-cases.md 
         ├── app-flow.md 
         └── requirements.md
        

```
## App starten
Zuerst die virtuelle Umgebung aktivieren:

.\venv\Scripts\activate

Dann die App starten:

python -m streamlit run app.py

## Status
Version 1 ist fertig.

Enthalten sind:

- Datenladen
- Datenprüfung
- Train/Test Split
- Random Forest Training
- kNN Training
- Modellvergleich
- Visualisierungen
- Feature Importance
- Ergebnisinterpretation
