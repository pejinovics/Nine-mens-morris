# Creating a table to show temporary state


# https://www.youtube.com/watch?v=l-hh51ncgDI&ab_channel=SebastianLague


import hashmap as h

positions = h.LinearHashMap()
positions['1'] = '1'
positions['2'] = '2'
positions['3'] = '3'
positions['4'] = '4'
positions['5'] = '5'
positions['6'] = '6'
positions['7'] = '7'
positions['8'] = '8'
positions['9'] = '9'
positions['10'] = '10'
positions['11'] = '11'
positions['12'] = '12'
positions['13'] = '13'
positions['14'] = '14'
positions['15'] = '15'
positions['16'] = '16'
positions['17'] = '17'
positions['18'] = '18'
positions['19'] = '19'
positions['20'] = '20'
positions['21'] = '21'
positions['22'] = '22'
positions['23'] = '23'
positions['24'] = '24'


def clean_letter(let):
    if len(let) < 2:
        let += ' '
    return let


def table():

    print('\n')
    print('     ','=' *10, ' TABLE ', '=' *10)
    print('\n')
    print(f"1     {positions['1']}-------------{positions['2']}-------------{positions['3']}\n"
          f"      |             |             |\n"
          f"2     |   {positions['4']}---------{positions['5']}---------{positions['6']}   |\n"
          f"      |   |         |         |   |\n"
          f"3     |   |   {positions['7']}-----{positions['8']}-----{positions['9']}   |   |\n"
          f"      |   |   |           |   |   |\n"
          f"4     {clean_letter(positions['10'])}--{clean_letter(positions['11'])}--{clean_letter(positions['12'])}          "
          f"{clean_letter(positions['13'])}--{clean_letter(positions['14'])}--{clean_letter(positions['15'])}\n"
          f"      |   |   |           |   |   |\n"
          f"5     |   |   {clean_letter(positions['16'])}----{clean_letter(positions['17'])}----"
          f"{clean_letter(positions['18'])}  |   |\n"
          f"      |   |         |         |   |\n"
          f"6     |   {clean_letter(positions['19'])}--------{clean_letter(positions['20'])}--------"
          f"{clean_letter(positions['21'])}  |\n"
          f"      |             |             |\n"
          f"7     {clean_letter(positions['22'])}------------{clean_letter(positions['23'])}------------"
          f"{clean_letter(positions['24'])}\n"
          f"\n      a   b   c     d     e   f   g\n\n")



# table()