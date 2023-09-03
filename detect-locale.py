import win32api
import yaml

result={
    #"GetSystemDefaultUILanguage": win32api.GetSystemDefaultUILanguage(),
    #"GetUserDefaultUILanguage": win32api.GetUserDefaultUILanguage(),
    #"GetThreadUILanguage": win32api.GetThreadUILanguage(),
    "GetKeyboardLayout": win32api.GetKeyboardLayout(),
    "GetKeyboardLayoutList": list(win32api.GetKeyboardLayoutList()),
    "GetKeyboardLayoutName": win32api.GetKeyboardLayoutName(),
    "GetSystemDefaultLangID": win32api.GetSystemDefaultLangID(),
    "GetSystemDefaultLCID": win32api.GetSystemDefaultLCID(),
    "GetThreadLocale": win32api.GetThreadLocale(),
    "GetUserDefaultLangID": win32api.GetUserDefaultLangID(),
    "GetUserDefaultLCID": win32api.GetUserDefaultLCID(),
}

print(yaml.dump(result))