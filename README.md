# Debloater for Android devices
_An easy way to get rid of the bloatware from your Android device._

## Starting 🚀

_The following instructions will allow you to use this script on your computer._

### Prerequisites 📋

+ [ADB Drivers](https://developer.android.com/studio/releases/platform-tools)
+ [F-Droid](https://f-droid.org/es/)
+ [Developer settings on your device](https://developer.android.com/studio/debug/dev-options)

_Also, you **must** change the path of the ADB drivers inside the quotes, **don't delete the r**._
```
os.chdir(r"YOUR ADB DRIVERS LOCATION")
```

## Defining packages to uninstall
Install App Manager from F-Droid and look for the apps you want to uninstall. Note the package of each app on the .csv file, for example com.google.android.play.games, which is Play Games.

## Running the script
To uninstall the apps, just connect your phone to the PC and run the script.
