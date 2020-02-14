"""
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
Valid smiley face examples:
:) :D ;-D :~)
Invalid smiley faces:
;( :> :} :]

Example cases:

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
"""


def count_smileys(arr):
    eyes = [':', ';']
    nose = ['-', '~']
    mouth = [')', 'D']
    smiley_faces = 0
    
    for i in arr:
        if i[0] in eyes and i[1] in mouth:
            smiley_faces += 1
        elif i[0] in eyes and i[1] in nose and i[2] in mouth:
            smiley_faces += 1
    return smiley_faces
