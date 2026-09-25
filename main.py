from src.data_loader import load_housing_data


def main():
    df = load_housing_data()

    print("Dimensions du dataset :", df.shape)
    print("\nPremières lignes :")
    print(df.head())

    print("\nInformations sur les colonnes :")
    print(df.info())

    print("\nStatistiques descriptives :")
    print(df.describe())

    print("\nValeurs manquantes :")
    print(df.isna().sum())


if __name__ == "__main__":
    main()