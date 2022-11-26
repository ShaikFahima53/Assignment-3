def fn_up_lo(str):
    up_cnt=0
    lo_cnt=0
    for i in str:
        if i.isupper():
            up_cnt+=1
        else:
            lo_cnt+=1
    print(f'Upper case letters: {up_cnt}')
    print(f'Lower case letters: {lo_cnt}')
fn_up_lo('RTHsgYU')
