''' Program 14: Write a Python program that uses Regular Expressions (re) to extract 
a specific block of text enclosed within a <div class="predefined"> and its closing 
</div> tag from a block of HTML code.'''

import re

HTML = """ 
    <html>
        <body>
            <div class ="Row">
                this is starting 
            </div>
            <div class ="predefined">
                this is the predefined text... 
                <div class ="row">
                    this is ending
                </div>
            </div>
        </body>
    </html>
"""

match = re.search(r'<div class ="predefined">(.*?)</div>', HTML, re.DOTALL)

if match:
    print(match.group(1))
else:
    print("No match found")
