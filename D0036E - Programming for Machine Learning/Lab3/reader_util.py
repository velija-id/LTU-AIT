
def read_file():

    with open("inc_vs_rent.csv") as f:
        rows = f.readlines()
        header = [ val.strip() for val in rows[0].split(",")]
        rows = [
            (_idx, int(year), region, int(rent), float(inc))
            for row in rows[1:]
            for _idx, year, region, rent, inc in  [row.strip().split(",")]]

    return header, rows

    return cleaned_data