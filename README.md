demographica
============

Analyse US name distributions and create age profiles.


    from demographica import TOTALS
  
`TOTAL` is a Pandas dataframe with a 3d multi-index. The first argument is the first-name, the second argument is the gender (`"M"` or `"F"`) and the third argument is the age bin:
    
    TOTALS.ix['Jennifer', 'F', '60 to 64 years']
    # 16613
  
  
If you leave the last arugment variable, you can get the distribution: 

    TOTALS.ix['Jennifer', 'F', :]
    """
                    occurrences
    age_bin
    04 and under           8420
    05 to 09 years        22450
    10 to 14 years        40925
    15 to 19 years        57540
    20 to 24 years        90453
    25 to 29 years       163395
    30 to 34 years       277423
    35 to 39 years       289646
    40 to 44 years       292110
    45 to 49 years       112215
    50 to 54 years        52210
    55 to 59 years        26424
    60 to 64 years        16613
    65 to 69 years         9147
    70 to 74 years         1225
    75 to 79 years           55
    80 to 84 years           21
  """
  
But why read numbers when you can plot! 

    TOTALS.ix['Jennifer', 'F', :].plot()
  
![jen](https://i.imgur.com/UB5MC3zl.png)

### Age inference



