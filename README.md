# Python Scripts

## Tools

### Python Documentation

Is anyone else a documentation geek like me? Here's [a link to Python's documentation page](https://docs.python.org/3.10/index.html). There's even a great [tutorial](https://docs.python.org/3.10/tutorial/index.html) if you want to jump in and learn.

### Google Colaboratory

I've been using [Google Colabs](https://colab.research.google.com/?utm_source=scs-index) and it's a great way to run python when I'm not on my normal device or don't want to run it locally.

[This is the introduction that first got me to try it](https://codingandfun.com/how-to-use-python-on-ipad/), and it works great on my iPad.

## Index

| Script | Link | Notes |
|:---:|:---:|:---:|
| Rochambeau - a simple game of Rock, Paper, Scissors | [/rochambeau.py](https://github.com/stevie170/python-scripts/blob/main/rochambeau.py) | user input, while loop, conditionals, and Python's *random* module |
| Password Generator - user is prompted for a password length and given a password of that length | [/password-generator.py](https://github.com/stevie170/python-scripts/blob/main/password-generator.py) | user input, strings, and Python's *random* module |
| Story Generator - a Python script to generate a random story each time it's run | [/story-generator.py](https://github.com/stevie170/python-scripts/blob/main/story-generator.py) | needs refining; strings, arrays, and Python's *random* module |
| Website Alert - a Python script to alert on any change to a website | [/website-alert.py](https://github.com/stevie170/python-scripts/blob/main/website-alert.py) | incomplete / work in progress; still trying to figure out a few things in this one; hashing, while loops, try/except, and Python's *time* and *hashlib* modules |
| Wikipedia API - a Python script that prompts the user for a topic and gives the user options for what to learn about the topic, then presents the relevant information from Wikipedia about that topic | [/wiki-api.py](https://github.com/stevie170/python-scripts/blob/main/wiki-api.py) | user input, Python's *wikipedia* module |
||||

## Future script ideas

| Idea | What it would be | Why it sounds fun |
|:---:|:---:|:---:|
| Public CVE Watcher | Query the NVD API for recent CVEs in specific products or vendors. Build a `CVETracker` class and normalize CVE data into a dataframe. Generate outputs like "top affected products this week" and export CSV. | To stay on top of security vulnerabilities in tools I use to help me prioritize what to patch, especially because it's easy to forget. Like shadow IT but personal instead of corporate haha. |
| Home Network Risk Dashboard | Scan local devices and combine results with public IP lookup APIs. Use a `DeviceInventory` class and a `RiskScorer` class. Produce a dataframe of devices, open ports, and reputation scores. | A simple way to do quick checks of my home network security. |
| GitHub Security Status Reporter | Use GitHub's public API to report repo security alerts, dependency warnings, and issue trends. Build a `GitHubSecurityReporter` class and present findings in a dataframe. Demonstrates OAuth token handling, REST API calls, and GitHub metadata. | Monitor my repos for security issues. |
| Malware/Threat Feed Reader | Fetch public threat feeds like MalwareBazaar, AlienVault OTX, or AbuseIPDB. Build a `ThreatFeed` class and normalize items into `pandas`. Create summaries like top malware families, new indicators, or IOC counts. | See what's trending in the wild. |
| Weather + Alert Assistant | Combine OpenWeatherMap or WeatherAPI with public emergency alert data. Build classes for forecast retrieval and alert ingestion. Show a dataframe of forecast risk and alert notifications for home prep. | Get weather forecasts plus emergency alerts in one place, useful for planning trips or staying safe. |
| Personal Security Scorecard | Combine multiple public signals like HaveIBeenPwned, GitHub, and IP geolocation. Build a `SecurityScorecard` class that computes a consolidated risk score. Present per-signal dataframes and a unified dashboard. | Like a credit score but for online safety. |
