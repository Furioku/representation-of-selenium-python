# representation-of-selenium-python
This repo contains automated e2e tests for facebook messenger in selenium python

# To open project we need:
1. python
2. pip
3. selenium ( pip install selenium )
4. beahve ( pip install behave )
5. chrome browser + chromedriver

# To run all tests
behave

# To run specific feature
behave features/about.feature

# To re-run failing features
behave "@rerun_failing.features"  
To use the RerunFormatter all you need to do is put it in your behave configuration file (behave.ini):  
"# -- file:behave.ini  
[behave]  
format   = rerun  
outfiles = rerun_failing.features"
