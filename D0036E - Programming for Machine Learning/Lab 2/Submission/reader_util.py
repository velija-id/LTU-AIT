
def read_subset_file() -> list[tuple]:
    data = open("inc_subset.csv").readlines()
    # Prepare the data with a list and comprehension
    cleaned_data = [ (int(age), float(income))
                    for row in data[1:]
                     for _, age, income in [row.strip().split(",")]]
    return cleaned_data

def read_all_data_file() -> list[tuple]:
    data = open("inc_utf.csv").readlines()
    # Prepare the data with a list and comprehension
    cleaned_data = [(int(region[:2]), int(age.replace(" years", "").replace("+", "")), float(income))
                    for row in data[1:]
                    for _, region, age, income in [row.strip().split(",")]]
    return cleaned_data
