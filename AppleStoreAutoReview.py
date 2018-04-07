#coding=utf-8
##############################################
#
# Author:       Shen Wenrui
# Date:         20180407
# Description:
#
##############################################

import applescript

scpt = applescript.AppleScript('''
    on run {arg1, arg2}
        say arg1 & " " & arg2
    end run

    on foo()
        return "bar"
    end foo

    on Baz(x, y)
        return x * y
    end bar
''')

print(scpt.run('Hello', 'World')) #-> None
print(scpt.call('foo')) #-> "bar"
print(scpt.call('Baz', 3, 5)) #-> 15