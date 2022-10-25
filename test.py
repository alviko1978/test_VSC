busd = 500
n = 1
while n <= 365:
    busd = busd + busd * 8 / 100 / 365
    print(f'день {n} сумма {busd}')
    n+=1
    