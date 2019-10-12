# ginger_django
A simple project with Python 3.7 and Django 2.0.* to see what's the logic of Django.
This question and solution is created by Ahmet Gungor.


Purpose -> Imagine a website that an online ATM with works only with cash money.
User inputs his money amount (we can assume that it's dollar $). 
This ATM website should give count of moneys for each cash and MINIMUM count of cash.

Such as; Imagine user inputs 273;

2 => 100 $
1 =>  50 $
1 =>  20 $
1 =>   2 $
1 =>   1 $

So website should give this output and 2 + 1 + 1 + 1 + 1 = The total count of cash is 6.

(Note: Dollar cash moneys are: $1, $2, $5, $10, $20, $50, $100)
