# Project Overview
A fun GUI that displays famous quotes from Kanye West. 


# Objectives
- Get quotes from the Kanye West Rest API
- Create User Interface
- Create a button to refresh quotes

# Results
![image](https://github.com/frantzalexander/kanye_app/assets/128331579/4cee4751-937e-4de2-9f51-f3b78fc56bb1)


# Process
```mermaid
flowchart TD
start(((START)))
ui[Create UI]
button[Create Refresh Button]
connect[Connect to API]
display[Display Quote]
finish(((END)))
start --> ui
ui --> button
button --> connect
connect --> display
display --> finish
