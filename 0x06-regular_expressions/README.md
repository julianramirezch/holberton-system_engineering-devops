<H1 align="center"> 0x06. Regular expression </H1>

<p align="center">
   <a href="https://www.linux.org/"><img src="https://cdn.pixabay.com/photo/2013/07/13/13/41/bash-161382_960_720.png" width="170" height="170"/></a>

<p align="center"> 
   <b>Holberton School Bogotá D.C</b>
                
----
<H3> General </H3>
   
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

    sylvain@ubuntu$ cat example.rb
    #!/usr/bin/env ruby
    puts ARGV[0].scan(/127.0.0.[0-9]/).join
    sylvain@ubuntu$
    sylvain@ubuntu$ ./example.rb 127.0.0.2
    127.0.0.2
    sylvain@ubuntu$ ./example.rb 127.0.0.1
    127.0.0.1
    sylvain@ubuntu$ ./example.rb 127.0.0.a


### Tasks:

| Name | Description                    |
| ------------- | ------------------------------ |
| `0-simply_match_holberton.rb`      |  Simply matching Holberton    |
| `1-repetition_token_0.rb`      |    Repetition Token #0 |
| `2-repetition_token_1.rb`   |  Repetition Token #1  |
| `3-repetition_token_2.rb`      | Repetition Token #2|
| `4-repetition_token_3.rb`      | Repetition Token #3 |
| `5-beginning_and_end.rb`      | Not quite HBTN yet |
| `6-phone_number.rb`      | Call me maybe  |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb`      | OMG WHY ARE YOU SHOUTING?   |


## Author: 
### Julian Ramirez <julianramirezch1@gmail.com>
----
[![Twitter Follow](https://img.shields.io/twitter/follow/JulianR_30.svg?style=social&label=Follow)](https://twitter.com/JulianR_30)

2020