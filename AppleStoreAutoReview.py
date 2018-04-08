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
    -- Function for iTunes sign in
    property loginBtn : "登录…"
    property logoutBtn : "注销"
    -- Launch iTunes
    
    on openAppStore (appleId, passwd)
        tell application "App Store" to activate
        tell application "System Events"
            tell process "App Store"
                set frontmost to true
                
                try
                    click menu item loginBtn of menu "商店" of menu bar 1
                on error
                    click menu item logoutBtn of menu "商店" of menu bar 1
                    delay 2
                    click menu item loginBtn of menu "商店" of menu bar 1
                end try
                
                delay 1
                set value of text field 2 of sheet 1 of window "App Store" to appleId
                set value of text field 1 of sheet 1 of window "App Store" to passwd
                keystroke return      -- Press the return key "登陆"
                
                delay 10
                keystroke return      -- Click Review
                --click menu item 2 of sheet 1 of window "App Store"
                --click menu item "Review" --of sheet 1 of window "App Store"
                
                --keystroke appleId
                --keystroke tab
                delay 1
                --keystroke passwd
			
            end tell
        end tell
        
        return True
    end openAppStore
''')

user_email = "zhangtao001@protonmail.com"
user_password = "Apple_swr123"
print(scpt.call('openAppStore', user_email, user_password))