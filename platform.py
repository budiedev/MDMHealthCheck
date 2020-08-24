import csv
# print(f'Enter File Name: ')
# file_name = str(input())
file_name = 'device.csv'

print(f'Select Platform: ')
print(f' [ 1 ] IOS ')
print(f' [ 2 ] Android ')

input_platform = int(input())
platform = ""
if input_platform > 2:
    print(f'Please select correct option ')
elif input_platform == 1 :
    platform = 'iOS'
elif input_platform == 2:
    platform = "Android"

platform_ios = 0
no_device = 0
print(f'{platform} Version : ')
OSversion = str(input())

with open(file_name, mode='r',encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    l = 0
    for row in reader:
        if l == 0:
             l += 1
        if row[4] == platform:
            platform_ios += 1
            ver = row[5]
            checkver = ver.startswith(OSversion)
            if checkver:
                no_device += 1
        l += 1

print(f'{ platform } { platform_ios } Device')
print(f'{ platform } Version { OSversion } : { no_device } Device')
        


 