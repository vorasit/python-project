def numBer(cal1,cal2):
    row = 0
    while row <= 12:
        title = cal1
        while title <= cal2:
            if row == 0:
                print('สูตรคูณแม่ {} \t'.format(title),end="")
            else:
                print(title,'x',row, '=', title*row,'\t',end="")
            title+=1
        print('')
        row+=1
    

cal1 = int(input('สูตรคูณแม่ : '))
cal2 = int(input('ถึงแม่ : '))
numBer(cal1,cal2)