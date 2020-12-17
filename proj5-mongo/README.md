# Project 5: Brevet time calculator with Ajax and MongoDB

Simple list of controle times from project 4 stored in MongoDB database.

## Functionalities

This program will take provided python brevet calculator with minor editting.

Any input with at most extra 5% or brevet distance will be accepted.

If any changes occur, this program will still check for you (ex. if you entered 10 50 100 150 and change 50 to other number, still will be checked)

As long as user inserts new numbers under at most 5% of brevet distance, this program will give you time calculation.

If any numbers reentered, it's fine, no reocurring input will be accepted


Once you fill the blanks with no notes on and submit, this program will save it to database

If you made changes, then previous data in database will be deleted, and store fresh

Once you hit the display button, this program will present sorted schedule according to whay you submitted

## Corner Cases

Submit and Display when there are no entries : Since all are null it will submit nothing and print html with nothing on

Empty spaces between inputs : it's fine, this program checks multiple same inputs anywhere and, at the end, database will collect all and sort it before we see.
