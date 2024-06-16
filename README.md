# ids2017-anomaly-detection
Wykrywanie anomalii sieciowych z użyciem uczenia maszynowego 2024

## O zestawie danych
Zbiór danych IDS2017 zawiera najbardziej powszechne w 2017 roku ataki, które przypominają prawdziwe dane ze świata rzeczywistego. Zawiera również wyniki analizy ruchu sieciowego.

Dane w zestawie zostały podzielone na kolejne dni tygodnia, w których występują różne ataki. Wybrane przez nas próbki to:

- Środa (Różne ataki DoS)
- Piątek (Atak DDoS)
- Połączone dane z atakami typu DoS (Poniedziałek + Środa + Piątek)

[Prezentacja zestawu](/statistics.ipynb)

## Przygotowanie danych
Oryginalnie dane miały format plików CSV, ze wględu na oszczędność zasbów działaliśmy głównie na formacie parquet.

Zaczęliśmy od downsizingu, usunięcia wartości NaN i zduplikowanych wierszy. 

[Czyszczenie danych](./Data_Cleaning/raw_to_clean.ipynb)

Następnie użyliśmy metody Recursive Feature Elimination w celu zmiejszenia ilości cech do 10 (oryginalnie 79). Kolumny były wybierane na podstawie zestawu z połączonymi danymi o atakach DoS (combined.parquet).

[Wybór cech](./Data_Cleaning/clean_to_final.ipynb)

## Podejście z uczeniem nadzorowanym
Ze względu na charakter danych (każdy rekord oznaczony jako normalny ruch lub jako atak), naszym głównym podejściem było podejście z uczeniem nadzorowanym.

Użyte przez nas modele to:
- [Random Forest Classifier](/RandomForest.ipynb)
- [Logistic Regression](/LogisticRegression.ipynb)
- [K-Nearest Neighbours](/K-NN.ipynb)
- [Naive Bayes](/Bayes.ipynb)

### Podsumowanie
Tabelki i wnioski

## Podejście z uczeniem nienadzorowanym




