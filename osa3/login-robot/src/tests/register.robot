*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallee  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  username too short.

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kal1  kalle123
    Output Should Contain  username invalid.

Register With Valid Username And Too Short Password
    Input Credentials  kal  kalle12
    Output Should Contain  password not valid.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kal  kalleeeeeeee
    Output Should Contain  password not valid.

*** Keywords ***
Input New Command And Create User
    Create User     kalle     kalle123
    Input New Command
