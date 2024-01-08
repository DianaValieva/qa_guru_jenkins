from selene.support.shared import browser
from selene import be, have, by
import os
import allure


def test_submit():
    with allure.step("Открываем demoqa"):
        browser.open('https://demoqa.com/automation-practice-form')

    with allure.step("Вводим данные"):
        browser.element('#firstName').should(be.blank).type("Diana")
        browser.element('#lastName').should(be.blank).type("Valieva")
        browser.element('#userEmail').should(be.blank).type("di7051@gmail.com")
        browser.element("#gender-radio-2").double_click()
        browser.element('#userNumber').should(be.blank).type("9874956293")
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text('December')).click()
        browser.element('.react-datepicker__year-select').click().element(by.text('1991')).click()
        browser.element('.react-datepicker__day--030').click()
        browser.element('#subjectsInput').should(be.blank).type("Maths").press_enter()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#currentAddress').should(be.blank).type("ufa")
        browser.element('#react-select-3-input').type('NCR').press_enter()
        browser.element('#react-select-4-input').type('Delhi').press_enter()
        browser.element('#uploadPicture').send_keys(os.path.abspath(
            'tests/files/dog.jpg'))

    with allure.step("Подтверждаем"):
        browser.element('#submit').press_enter()

    with allure.step("Проверяем данные"):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
        browser.all('.table').all('td')[1].should(have.exact_text('Diana Valieva'))
        browser.all('.table').all('td')[3].should(have.exact_text('di7051@gmail.com'))
        browser.all('.table').all('td')[5].should(have.exact_text('Female'))
        browser.all('.table').all('td')[7].should(have.exact_text('9874956293'))
        browser.all('.table').all('td')[9].should(have.exact_text('30 December,1991'))
        browser.all('.table').all('td')[19].should(have.exact_text('NCR Delhi'))
