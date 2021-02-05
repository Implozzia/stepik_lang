link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_availability_basket_button(driver):
    driver.get(link)
    add_to_basket = driver.find_element_by_css_selector('.btn-add-to-basket')
    assert add_to_basket, 'Basket not found'
