from main import load_data # Import the function to test

def test_load_data():
    df = load_data()  # Call the function you want to test
    assert not df.empty  # Assert that the dataframe is not empty