from selenium import webdriver
import unittest


class BasePage(unittest.TestCase):
    linkToImages = "https://the-internet.herokuapp.com"

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/maria_shukhter/Desktop/selenium/chromedriver')

    def tearDown(self):
        self.driver.close()


class TestPage(BasePage):


    def test_dynamic_content_has_10char(self):
        print("Test dynamic dext has 10 char word")
        self.driver.get(" https://the-internet.herokuapp.com/dynamic_content")

        element_list = self.driver.find_elements_by_css_selector(".large-10.columns:not(.large-centered)")
        texts_list = []
        for element in element_list:
            texts_list.append(element.text)

        max = 0
        longestWord = ""

        result = False
        for block in texts_list:
            str = block.replace(".", "")
            words_list = str.split()
            for word in words_list:
                if len(word) >= 10:
                    result = True
                    if len(word) > max:
                        max = len(word)
                        longestWord = word

        self.assertEqual(result, True)

        print('Longest word is ', longestWord, "\n")

    def test_punisher_image_doesnt_appear(self):
        print("Test Punisher Image doesnt appear ")

        map_Images = {}

        map_Images[self.linkToImages + "/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg"] = "Punisher"
        map_Images[self.linkToImages + "/img/avatars/Original-Facebook-Geek-Profile-Avatar-1.jpg"] = "Child"
        map_Images[self.linkToImages + "/img/avatars/Original-Facebook-Geek-Profile-Avatar-2.jpg"] = "Warrior"
        map_Images[self.linkToImages + "/img/avatars/Original-Facebook-Geek-Profile-Avatar-5.jpg"] = "Demon"
        map_Images[self.linkToImages + "/img/avatars/Original-Facebook-Geek-Profile-Avatar-6.jpg"] = "Soldier"
        map_Images[self.linkToImages + "/img/avatars/Original-Facebook-Geek-Profile-Avatar-7.jpg"] = "Jester"

        result = True
        self.driver.get(" https://the-internet.herokuapp.com/dynamic_content")
        image_list = self.driver.find_elements_by_css_selector(".large-2.columns >img")
        for image in image_list:
            print(map_Images[image.get_attribute("src")])
            if image.get_attribute(
                    "src") == 'https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg':
                result = False
        self.assertEqual(result, True)



unittest.main()