
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
    Submit Credentials
    Register should succeed

Register With Too Short Username And Valid Password
    Set Username  za
    Set Password  emma1234
    Set Password Confirmation  emma1234
    Submit Credentials
    Register Should Fail With Message  Username min length is 3

Register With Valid Username And Too Short Password
    Set Username  emma
    Set Password  e1
    Set Password Confirmation  e1
    Submit Credentials
    Register Should Fail With Message  Password min lenght is 8

Register With Nonmatching Password And Password Confirmation
    Set Username  emma
    Set Password  emma1234
    Set Password Confirmation  emmi1234
    Submit Credentials
    Register Should Fail With Message  Password does not match with Password confirmation

Login After Successful Registration
    Set Username  emma
    Set Password  emma1234
    Set Password Confirmation  emma1234
    Submit Credentials
    Go To Login Page
    Set Username  emma
    Set Password  emma1234
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Go to Login Page
    Set Username  emma
    Set Password  emmi1234
    Click Button  Login
    Login Should Fail With Message  Invalid username or password
    
*** Keywords ***

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

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

Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

