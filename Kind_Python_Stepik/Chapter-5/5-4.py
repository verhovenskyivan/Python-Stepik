s=input()
if s[0]=='+' and s[1] =='7' and s[2]=='(' and s[6]==')' and len(s)==16 and s[3:6].isdigit() and s[7:9].isdigit() and s[10]=='-' and s[11:12].isdigit() and s[13]=='-' and s[14:15].isdigit():
    print('ДА')
else:
    print('НЕТ')
#----------------------------
