import json
import win32api
import yaml


#load lcid.json
with open('lcid.json', 'r', encoding="utf-8") as f:
    lcid = json.load(f)



KeyboardLayout = win32api.GetKeyboardLayout()
KeyboardLayoutList = list(win32api.GetKeyboardLayoutList())
KeyboardLayoutName = win32api.GetKeyboardLayoutName()
SystemDefaultLangID = win32api.GetSystemDefaultLangID()
SystemDefaultLangTag = lcid[str(SystemDefaultLangID)]
SystemDefaultLCID = win32api.GetSystemDefaultLCID()
ThreadLocale = win32api.GetThreadLocale()
ThreadLocaleTag = lcid[str(ThreadLocale)]
UserDefaultLangID = win32api.GetUserDefaultLangID()
UserDefaultLangTag = lcid[str(UserDefaultLangID)]
UserDefaultLCID = win32api.GetUserDefaultLCID()

result={
    "KeyboardLayout": KeyboardLayout,
    "KeyboardLayoutList": KeyboardLayoutList,
    "KeyboardLayoutName": KeyboardLayoutName,
    "SystemDefaultLangID": SystemDefaultLangID,
    "SystemDefaultLangTag": SystemDefaultLangTag,
    "SystemDefaultLCID": SystemDefaultLCID,
    "ThreadLocale": ThreadLocale,
    "ThreadLocaleTag": ThreadLocaleTag,
    "UserDefaultLangID": UserDefaultLangID,
    "UserDefaultLangTag": UserDefaultLangTag,
    "UserDefaultLCID": UserDefaultLCID,
}

print(yaml.dump(result))