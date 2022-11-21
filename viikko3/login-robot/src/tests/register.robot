*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  emma  kilpikonna1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username is already in use

Register With Too Short Username And Valid Password
    Input Credentials  za  kalle123
    Output Should Contain  Username must contain at least 3 characters from [a-z]

Register With Valid Username And Too Short Password
    Input Credentials  maija13  kis2
    Output Should Contain  Password should contain at least one number and min lenght is 8"

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  minttu3  kilpikonna
    Output Should Contain  Password should contain at least one number and min lenght is 8"

*** Keywords ***
Input New Command And Create User
    Input New Command 
    Create User  kalle  kalle123