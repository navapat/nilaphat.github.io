import random as rd
def do_enhance(percent):
    pick = rd.random()*1000
    percent *= 10
    if pick <= percent:
        return "S -->{:.2f}:::{}%".format(pick, percent)
    else:
        return "F -->{:.2f}:::{:.0f}%".format(pick, percent)
def loop_enhance(percent, round):
    scrolls = 0
    flag = 'S'
    for i in range(round):
        status = do_enhance(percent)
        # print(status)
        scrolls += 1
        if status[0] == 'F':
            flag = 'F'
            scrolls+=1
            return flag, scrolls
    return flag, scrolls
def finish_one():
    all_status = 'F'
    round = 0
    scrolls = 0
    all_scrolls = 0    
    while all_status == 'F':
        round += 1
        status,scrolls = loop_enhance(24.2,enh_1)
        all_scrolls += scrolls
        if status == 'F':
            continue
        status,scrolls = loop_enhance(48.4,enh_2)
        all_scrolls += scrolls
        if status == 'F':
            continue
        status,scrolls = loop_enhance(72.6,enh_3)
        all_scrolls += scrolls
        if status == 'F':
            continue        
        status,scrolls = loop_enhance(96.8,enh_4)
        all_scrolls += scrolls
        if status == 'F':
            continue        
        
        all_status = 'S'
    return round, all_scrolls

if __name__ == "__main__":
    # target_enh = int(input("Target:"))
    enh_1 = 0
    enh_2 = 1
    enh_3 = 3
    enh_4 = 8


    max_e = -1
    min_e = 99999
    for i in range(10000):
        round, all_scrolls = finish_one()
        # print("Round",round)
        print("{}:".format(i), "{:,}".format(all_scrolls*90) ,"Baht", 
            "Re-scroll:",round - 1, "Scroll:", abs(round-1-all_scrolls))
        if all_scrolls < min_e:
            min_e = all_scrolls
        if  all_scrolls > max_e:
            max_e = all_scrolls
    print("*Min-Max price","{:,}".format(min_e*90),"--------- {:,}".format(max_e*90))
    print("option: "+str((enh_1*20)+(enh_2*15)+(enh_3*12)+(enh_4*9)))   