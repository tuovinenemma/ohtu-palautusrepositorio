
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset App And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  emma
    Set Password  emma1234
    Set Password Confirmation  emma1234
    Click Button  Register
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  za
    Set Password  emma1234
    Set Password Confirmation  emma1234
    Click Button  Register
    Page Should Contain  Username min length is 3

Register With Valid Username And Too Short Password
    Set Username  emma
    Set Password  e1
    Set Password Confirmation  kal123
    Click Button  Register
    Page Should Contain  Password min lenght is 8

Register With Nonmatching Password And Password Confirmation
    Set Username  emma
    Set Password  emma1234
    Set Password Confirmation  emmi1234
    Click Button  Register
    Page Should Contain  Password does not match with Password confirmation



    
*** Keywords ***

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Reset App And Go To Register Page
    Reset Application
    Go To Register Page

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}