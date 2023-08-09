import project

def main():
    test_tax()
    test_include_tax()
    test_without_tax()

def test_tax():
    assert project.tax("1000", "Nunavut") == (0.05, "GST(5%): $50.0")
    assert project.tax("1000", "Manitoba") == (0.12, "GST(7%): $70.0    PST(5%): $50.0")
    assert project.tax("1000", "Nova Scotia") == (0.15, "HST(15%): $150.0") 
    assert project.tax("1000", "Ontario") == (0.13, "HST(13%): $130.0")
    assert project.tax("1000", "Quebec") == (0.14975, "GST(9.975%): $99.75    QST(5%): $50.0")
    assert project.tax("1000", "Saskatchewan") == (0.11, "GST(6%): $60.0    PST(5%): $50.0")

def test_without_tax():
    assert project.without_tax("1000", "Nunavut") == 1050
    assert project.without_tax("1000", "Manitoba") == 1120
    assert project.without_tax("1000", "Nova Scotia") == 1150
    assert project.without_tax("1000", "Ontario") == 1130
    assert project.without_tax("1000", "Quebec") == 1149.75
    assert project.without_tax("1000", "Saskatchewan") == 1110

def test_include_tax():
    assert project.include_tax("1000", "Nunavut") == 950
    assert project.include_tax("1000", "Manitoba") == 880
    assert project.include_tax("1000", "Nova Scotia") == 850
    assert project.include_tax("1000", "Ontario") == 870
    assert project.include_tax("1000", "Quebec") == 850.25
    assert project.include_tax("1000", "Saskatchewan") == 890
    

if __name__ == "__main__":
    main()