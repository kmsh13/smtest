import csv
import time,calendar
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def validate(cur_time,type=0):
    try:
        if type == 0:
            return time.strptime(cur_time, '%H:%M:%S')
        if type == 1:
            print('3333333333333')
            print(time.strptime(cur_time, '%A %H:%M:%S'))
            return time.strptime(cur_time, '%A %H:%M:%S')
    except ValueError:
        return False




def mynormalproject():
    while(True):
        cur_time = input('Enter Current Time: ')
        if False == validate(cur_time):
            print('Invalid Input !!!!')
            continue
        else:
            break

    print("-------------- Now fetching configration ------------------------")
    with open('conf.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print("Configration : ",row['type'],"-",row['user'],row['type'],"-",row['cnt'],row['st'],"-",row['et']," | Current Time :",cur_time)

            if((row['st'] > cur_time) & (row['et'] > cur_time) ):
                print("True")
            elif ((row['st'] <= cur_time) & (row['et'] >= cur_time)) :
                print(cur_time)
            else:
                print("False")

def myenhancedproject():
    cur_time = 'Wednesday 10:34:44'
    cur_day = time.strptime(cur_time, '%A %H:%M:%S').tm_wday

    with open('conf_enhanced.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dayString = row['day']
            dayList = dayString.split(" and ")
            dayIndexLIst = list(map(lambda d: week.index(d),dayList))
            print(dayIndexLIst)
            print("Configration : ",
                  row['type'],
                  "-",row['user'],
                  row['type'],
                  "-",
                  row['cnt'],
                  row['st'],
                  "-",
                  row['et'],
                  row['day'],
                  " | Current Time :",
                  cur_time
                  )
            if cur_day in dayIndexLIst:
                print('i m in current date')
                if((row['st'] > cur_time) & (row['et'] > cur_time) ):
                    print(cur_time,"(Schedual Today)")
                elif ((row['st'] <= cur_time) & (row['et'] >= cur_time)) :
                    print('True')
                else:
                    tempDayList = dayList[:]
                    tempDayList.remove('Wednesday') # deep copy for temporary next date

                    print(tempDayList[0],row['st'])

            else :
                if((row['st'] > cur_time) & (row['et'] > cur_time) ):
                    print("True")
                elif ((row['st'] <= cur_time) & (row['et'] >= cur_time)) :
                    print(cur_time)
                else:
                    print("False")
if __name__ == "__main__":
    myenhancedproject()