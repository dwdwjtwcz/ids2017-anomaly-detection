# ids2017-anomaly-detection

Wykrywanie anomalii sieciowych z użyciem uczenia maszynowego 2024

## Uruchomienie

```bash
git clone https://github.com/dwdwjtwcz/ids2017-anomaly-detection
cd ids2017-anomaly-detection/IDS2017/Raw
wget http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/CSVs/MachineLearningCSV.zip
unizip MachineLearningCSV.zip
cd ..
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```
## O zestawie danych

Zbiór danych IDS2017 zawiera najbardziej powszechne w 2017 roku ataki, które przypominają prawdziwe dane ze świata rzeczywistego. Zawiera również wyniki analizy ruchu sieciowego.

Dane w zestawie zostały podzielone na kolejne dni tygodnia, w których występują różne ataki. Wybrane przez nas próbki to:

- Poniedziałek (Większa próbka ruchu benign)
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
- [Multi Layer Percerptron](/MLP.ipynb)

### Podsumowanie

| Nazwa                    | accuracy | Komentarz                                                    |
|--------------------------|----------|--------------------------------------------------------------|
| Random Forest Classifier | 99%      | Zestaw cech pozwala na wysoką jakość modelu |
| Logistic Regression      | 93%    | Dobry model do dyskryminacji binarnej                        |
| K-NN                     | 99%      | Wysokie accuracy wynika z charakteru datasetu                |
| Naive Bayes              | 22%      |                                                              |
| MLP                      | 96%      |                                                              |

## Podejście z uczeniem nienadzorowanym

Po wyrzuceniu kolumny danych oznaczających je jako atak/ruch normalny można też przetestować działanie algorytmów uczenia nienadzorowanego. Uzyskane efekty jednak wskazują na to, że ten konkretny zbiór lepiej radzi sobie z uczeniem z nadzorem.

Użyte modele to:
- [K-Means](/K-Means.ipynb)
- [PCA](/PCA.ipynb)
- [Autoencoder](/auto_encode.ipynb)
- [Isolation Forest](/iso_forest.ipynb)

### Podsumowanie

| Nazwa                    | accuracy | Komentarz                                                    |
|--------------------------|----------|--------------------------------------------------------------|
| K-Means                  | -        |                                                              |
| PCA                      | -        |                                                              |
| Isolation Forest         | 67%      |                                                              |
| Autoencoder              | 88.9%    |                                                              |





