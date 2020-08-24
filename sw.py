import csv

file_name = 'sw.csv'
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

print(f'{platform} Version : ')
OSversion = str(input())

print(f'Secure Web Version : ')
scverdefine = str(input())

IOS_ver = []
IOSSH_ver = []
Android_ver = []
AndroidSH_ver = []
TotalDevice = 0
platform_device = 0
sc_version = 0

with open(file_name, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader: 
        if line_count == 0:
            line_count += 1
        if row["OS"] == platform:
            platform_device +=1
            ver = row['OS Version']
            checkver = ver.startswith(OSversion)
            if checkver:
                scver = row['App Version']
                checkscver = scver.startswith(scverdefine)
                if checkscver:
                    sc_version += 1
        line_count += 1

    print(f'Processed {line_count} lines.')
    print(f'{platform} { platform_device } Device')
    print(f'{platform} version { OSversion } ')
    print(f'Secure Web Version { scverdefine } ')
    print(f'Number of Device { sc_version } ')


        


 