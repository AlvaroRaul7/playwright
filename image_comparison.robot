*** Settings ***
Documentation    Practica Compare Images
Library  SeleniumLibrary
Library    ./img/comparison.py
Library    DataDriver   /Users/alvaro/Documents/hotglue/playwright/Data1.xlsx    sheet_name=Hoja4

Test Template    CompareImagesExample

*** Variables ***

*** Test Cases ***

Prueba Compare Images using      ${link}     ${locator}

*** Keywords ***

CompareImagesExample
    [Documentation]    Comparando Imagenes
    [Arguments]    ${link}      ${locator}
    ${Result}=    Compare Images    ${link}      ${locator}
    # log to console        ${Result}
    IF    $Result == 0.0   
        Pass Execution    It's a perfect match! (0% Error)
    ELSE IF    $Result < 0.04
        Pass Execution    It's not a perfect match, but close! (<4% Error)
    ELSE
        Fail    No good matches in the directory. (>5% Error)
    END
    