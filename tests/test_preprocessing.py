from my_project.preprocessing import clean_data
import pandas as pd

def test_clean_data_removes_nans():
    # Arrange: Create a messy dataframe
    df = pd.DataFrame({"val": [1, 2, None]})
    
    # Act: Run your code
    cleaned = clean_data(df)
    
    # Assert: Check if it worked
    assert cleaned["val"].isnull().sum() == 0