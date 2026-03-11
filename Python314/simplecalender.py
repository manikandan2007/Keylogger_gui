def is_leap_year(year):
    return year %4==0
def get_first_day_of_month(year,month):
    if month<3:
        month+=12
        year-=1
    k=year%100
    j=year//100
    day_code=(1+(13*(month+1)))//5+k+(k//4)+(j//4)-(2*j)%7
    return(day_code+6)%7
def display_calender(year,month):
    """display the calender for agiven year and month"""
    days=["sun","mon","tue","wed","thu","fri","sat"]
    month_days=[31,28,31,30,31,30,31,3130,31,30,31]
    if is_leap_year(year):
        month_days[1]=29
    days_in_month=month_days[month-1]
    first_day=get_first_day_of_month(year,month)
    print(f"(n{year}-{month:02}")
    print("".join(days))
    print(""*first_day,end="")
    for day in range(1,days_in_month+1):
        print(f"{day:3}",end="")
        if(first_day+day)%7==0:
         print()
year=int(input("enter the year:"))
month=int(input("enter the month(1-12):"))
display_calender(year,month)
