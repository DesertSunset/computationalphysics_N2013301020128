#coding=utf-8
char_ = {
'C':('    #### ',
     '   #    #',
     '  #      ',
     ' #       ',
     ' #####  '),
'P':('    #### ',
     '   #    #',
     '  #####  ',
     ' #       ',
     '#        '),
'T':(' ########',
     '    #    ',
     '   #     ',
     '  #      ',
     ' #       ' ),}
input_word = 'CPT'              #可以是C,P,T的任意组合 
for i in range(5):              #逐行扫描，共五行  
    for z in range(3):          #逐个字母扫描，共三个字母 
        for j in input_word[z]:   
            print char_ [j][i], #加逗号表示不换行，同行显示每个字母的同一行	
    print ""  			#通过在行末打印空白字符实现换行 
