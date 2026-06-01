# Requirements

## Ziel

Diese Datei beschreibt die wichtigsten Anforderungen an die ML Regression App.

Die App soll Random Forest und kNN für eine Regressionsaufgabe vergleichen.

## Funktionale Anforderungen

### F1: Beispieldatensatz laden

Die App soll den Concrete-Datensatz automatisch laden.

### F2: Datensatz anzeigen

Die App soll die ersten Zeilen des Datensatzes als Tabelle anzeigen.

### F3: Dateninformationen anzeigen

Die App soll einfache Informationen zum Datensatz anzeigen.

Dazu gehören:

* Anzahl der Zeilen
* Anzahl der Spalten
* fehlende Werte
* Zielvariable

### F4: Train/Test Split durchführen

Die App soll den Datensatz in Trainingsdaten und Testdaten aufteilen.

Standard:

* 80 % Training
* 20 % Test
* random_state = 42

### F5: Random Forest trainieren

Die App soll ein Random-Forest-Modell trainieren.

### F6: kNN trainieren

Die App soll ein kNN-Modell trainieren.

Für kNN soll eine Skalierung mit StandardScaler verwendet werden.

### F7: Metriken berechnen

Die App soll folgende Metriken berechnen:

* MAE
* RMSE
* R²

### F8: Ergebnisse vergleichen

Die App soll die Ergebnisse von Random Forest und kNN in einer Tabelle anzeigen.

### F9: Diagramme anzeigen

Die App soll Diagramme zur Modellbewertung anzeigen.

Zum Beispiel:

* Prediction vs. Real
* Vergleich von MAE und RMSE
* Vergleich von R²

### F10: Feature Importance anzeigen

Die App soll die Feature Importance des Random-Forest-Modells anzeigen.

## Nicht-funktionale Anforderungen

### N1: Einfache Bedienung

Die App soll leicht verständlich sein.

### N2: Reproduzierbarkeit

Die Ergebnisse sollen durch `random_state = 42` reproduzierbar sein.

### N3: Übersichtliches Design

Die App soll klar strukturiert sein.

### N4: Portfolio-Tauglichkeit

Das Projekt soll auf GitHub gut verständlich sein.

### N5: Erweiterbarkeit

Die App soll später erweitert werden können.

Mögliche Erweiterungen:

* CSV-Datei hochladen
* Zielvariable auswählen
* Modellparameter einstellen
* Ergebnisse exportieren
