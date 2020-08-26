# AutomateOnlineClass

## Run the script(Just Double click gmeetScript.py) and your online Lectures will be taken care of.

### What it does:

Run the code any time and you will be logged into google meet to the appropriate lectures via your college ID through out the day!

Begin running the script and it will log you in for the scheduled lecture automatically.
If you run the script before time or during a break it will pause and then login automatically when the next lecture is about to start.
#### Caution:
Do not kill the running script till the end of all lectures or it will kill the browser too. 
Works only for the google meet platform

### How to configure:
- Download both files and store them in the same folder.
- Make sure you have installed following libraries:
  - selenium
    - pip install selenium
  - pynput
    - pip install pynput
  - pytz
    - pip install pytz
- Make sure you are using the latest version of the _**Chrome Browser**_
- Works best with _**Python 3.6.x and Python 3.7.x**_

### THIS CODE IS WRITTEN FOR BE CMPN A TIMETABLE
#### YOU CAN EDIT IT FOR YOURSELF EASILY BY FOLLOWING THE INSTRUCTIONS GIVEN BELOW

## Adding Your Credentials:

![pic](https://github.com/amrutsavadatti/AutomateOnlineClass/blob/master/img.JPG)

- Put your Sfit email and password in place shown above in the code
- If Your Elective Subject is different replace it with **BEMIS** in that _classcodes_ list
- If your timetable is different then study the **timeTable** dict and update accordingly.
- And you are good to go for a _**Hassle Free Online Class Experience**_ 
