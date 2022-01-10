#  project name:
NEWS-WEB-APPLICATION


# AUTHOR
EDWIKE NYAUNCHO

## Setup Instructions and Installation
For the application to run, you have to install:

-python3.8
-pip
-virtual environment
-Flask

- open terminal
- git clone this repository https://github.com/Edwike12/News-Web-Application
- open News-Web-Application directory
- use a code editor


## Project description
This is a news application that allows a user to view news from different networks in different parts of the world. It has a list of all news sources from which the user can pick and read news directly from the site. A user can also search for any news.


## Technologies used
-python3.8
-Flask


## Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug


## Development 
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request


### Setting up the API Key
-To be able to gather article info from the News API you will need an API Key.

-Visit https://newsapi.org/ and register for an API key.

-In the root directory of the project folder create a file: start.sh

-Insert the following info into it:

        -export NEWS_API_KEY=''
        -python3.6 manage.py server
        -Insert the API Key you received from News Api where is.

-Run the application:

        -$ chmod a+x start.sh
        -$ ./start.sh


### Testing Application
-To run the tests for the class files:

    -$ python3.6 manage.py test



### contact information
Feel free to reach out:

Email: nyaunchoedwike@gmail.com


### License

*MIT*
Copyright (c) 2021 **EDWIKE NYAUNCHO**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

