import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def analyze_data(data):
    """Perform basic data analysis."""
    if data is not None:
        # Display summary statistics
        print("Summary Statistics:")
        print(data.describe())

        # Plot histograms for numeric columns
        print("Histograms:")
        for col in data.select_dtypes(include=['int', 'float']):
            data[col].plot(kind='hist', bins=10)
            plt.title(col)
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
        
        # Plot bar plot for the class label (string type)
        class_label_counts = data['Class'].value_counts()
        class_label_counts.plot(kind='bar')
        plt.title('Class Label Distribution')
        plt.xlabel('Class Label')
        plt.ylabel('Count')
        plt.show()

# Applying one hot encoding

def one_hot_encode(data, column):
    """
    Perform one-hot encoding on a categorical column of a DataFrame.

    Parameters:
        data (pandas.DataFrame): The DataFrame containing the categorical column.
        column (str): The name of the categorical column to be encoded.

    Returns:
        pandas.DataFrame: The DataFrame with the categorical column replaced by one-hot encoded columns.
    """
    # Perform one-hot encoding
    one_hot_encoded = pd.get_dummies(data[column], prefix=column)
    
    # Drop the original categorical column
    data_encoded = data.drop(columns=[column])
    
    # Concatenate the encoded columns with the original dataframe
    data_encoded = pd.concat([data_encoded, one_hot_encoded], axis=1)
    
    return data_encoded


def main():
    data = load_data('dlops_activity/DryBeanDataset/Dry_Bean_Dataset.xlsx')
    data = one_hot_encode(data, 'Class')
    analyze_data(data)

if __name__ == "__main__":
    main()
