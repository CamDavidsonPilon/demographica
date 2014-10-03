demographica
============

Analyse US name distributions and create age profiles.

    names = open('sample_first_names.tsv').readlines()
    name_distribution = compute_name_frequencies(names)
    age_distribution = age_calculator(name_distribution)
    sex_distribution = sex_calculator(name_distribution)
    print sex_distribution
    pplot(age_distribution)
