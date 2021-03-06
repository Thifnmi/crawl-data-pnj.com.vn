from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
from random import randint
from datetime import datetime

browser = None
ring_list = None
id = 1
id_image = 1

def crawl_rings():
    global id, id_image
    print("start crawl ring")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")

    header_product = ['id', 'product_code', 'image', 'name', 'price', 'category_id', 'supplier_id', 'quantity', 'collection', 'main_stone_type', 'main_stone_color', 'stone_shape', 'sub_stone_type', 'secondary_stone_color', 'gender', 'gift_giving_occasions', 'gift_for', 'weight_of_gold', 'gold_age', 'style', 'wire_size', 'face_size', 'machine_thickness', 'brand_origin', 'origin_of_the_apparatus', 'assembled_at', 'watch_movement_type', 'glass_type', 'wire_material', 'shell_material', 'face_shape', 'water_resistance', 'needle_number', 'watch_stones_attached', 'chronometer_certification', 'main_function']
    header_image = ['id','product_id','url']

    with open("Result\products.csv", "a+", encoding='utf-8', newline='') as product:
        writer_product = csv.writer(product)
        writer_product.writerow(header_product)
        with open("Result\images.csv", "a+", encoding='utf-8', newline='') as image:
            writer_image = csv.writer(image)
            writer_image.writerow(header_image)
            for page_number in range(1,12):
                url = "https://www.pnj.com.vn/nhan/page-"+ str(page_number)+"/"
                print(url)
                browser = webdriver.Chrome(executable_path='.\Driver\chromedriver.exe', chrome_options=options)
                browser.get(url)
                browser.maximize_window()

                data_product = []
                links = [link.get_attribute("href") for link in browser.find_elements_by_class_name("product-title")]
                i = 1
                for link in links:
                    browser.get(link)
                    name = browser.find_element_by_class_name("ty-product-block-title").text
                    product_code = browser.find_element_by_class_name("product_code_w").text
                    img = browser.find_elements_by_xpath("//img[@class='ty-pict cm-image']")
                    for image in img[1:]:
                        data_image = [id_image,id,image.get_attribute("src")]
                        writer_image.writerow(data_image)
                        id_image += 1
                    if len(img) < 2:
                        print(f"Page:{page_number} ignore item {i}")
                        i += 1
                        continue
                    url_image = img[1].get_attribute('src')
                    category_id = 1
                    collection = ""
                    main_stone_type = ""
                    main_stone_color = ""
                    stone_shape = ""
                    sub_stone_type = ""
                    secondary_stone_color = ""
                    gender = ""
                    gift_giving_occasions = ""
                    gift_for = ""
                    weight_of_gold = ""
                    gold_age = ""
                    style=""
                    wire_size=""
                    face_size=""
                    machine_thickness = ""
                    brand_origin = ""
                    origin_of_the_apparatus = ""
                    assembled_at = ""
                    watch_movement_type = ""
                    glass_type = ""
                    wire_material = ""
                    shell_material = ""
                    face_shape = ""
                    water_resistance = ""
                    needle_number = ""
                    watch_stones_attached = ""
                    chronometer_certification = ""
                    main_function = ""
                    product_info = browser.find_elements_by_class_name("ty-product-feature")
                    for detail in product_info:
                        info = detail.find_element_by_class_name("ty-product-feature__label").text
                        if info == "Th????ng hi???u:":
                            supplier_id = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "B??? s??u t???p:":
                            collection = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ph??? (n???u c??):":
                            sub_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ph??? (n???u c??):":
                            secondary_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ch??nh:":
                            main_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info =="H??nh d???ng ????:":
                            stone_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ch??nh:":
                            main_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Gi???i t??nh:":
                            gender = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "D???p t???ng qu??:":
                            gift_giving_occasion = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_giving_occasionn = gift_giving_occasion.split("\n")
                            for item in gift_giving_occasionn[:]:
                                if item == gift_giving_occasionn[-1]:
                                    gift_giving_occasions = gift_giving_occasions + item
                                else:
                                    gift_giving_occasions = gift_giving_occasions + item + ','
                        if info == "Qu?? t???ng cho ng?????i th??n:":
                            gift_for_who = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_for_x = gift_for_who.split("\n")
                            for item in gift_for_x[:]:
                                if item == gift_for_x[-1]:
                                    gift_for = gift_for + item
                                else:
                                    gift_for = gift_for + item + ','
                        if info == "Tr???ng l?????ng v??ng tham kh???o (ph??n v??ng):":
                            weight_of_gold = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Tu???i v??ng:":
                            gold_age = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Phong c??ch:":
                            style = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c d??y:":
                            wire_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c m???t:":
                            face_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? d??y v??? m??y:":
                            machine_thickness = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t X??? Th????ng Hi???u:":
                            brand_origin = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t x??? b??? m??y:":
                            origin_of_the_apparatus = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "L???p r??p t???i:":
                            assembled_at = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m??y ?????ng h???:":
                            watch_movement_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m???t k??nh:":
                            glass_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u d??y:":
                            wire_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u v???:":
                            shell_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "H??nh d???ng m???t:":
                            face_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? ch???u n?????c:":
                            water_resistance = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "S??? Kim:":
                            needle_number = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "???? G???n K??m ?????ng H???:":
                            watch_stones_attached = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???ng nh???n Chronometer:":
                            chronometer_certification = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???c n??ng ch??nh:":
                            main_function = detail.find_element_by_class_name("ty-product-feature__value").text
                    quantity = randint(5,10)
                    price = browser.find_element_by_class_name("ty-price-num").text
                    item = (id,product_code,url_image,name,price,category_id,supplier_id,quantity,collection,main_stone_type,main_stone_color,stone_shape,sub_stone_type,secondary_stone_color,gender,gift_giving_occasions,gift_for,weight_of_gold,gold_age,style,wire_size,face_size,machine_thickness, brand_origin,origin_of_the_apparatus,assembled_at,watch_movement_type,glass_type,wire_material,shell_material,face_shape,water_resistance,needle_number,watch_stones_attached,chronometer_certification,main_function)
                    print(f"Nh???n Page:{page_number} get item {i} with data: {item}")
                    data_product.append(item)
                    i += 1
                    id += 1
                    if i == 17:
                        browser.close()
                    sleep(2)
                writer_product.writerows(data_product)
                # print(f"Data page {page_number} is: {data_product}")
    id = id
    id_image = id_image
    sleep(2)
    print("done crawl ring")

def crawl_earring():
    global id, id_image
    print("start crawl earring")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")

    with open("Result\products.csv", "a+", encoding='utf-8', newline='') as product:
        writer_product = csv.writer(product)
        
        with open("Result\images.csv", "a+", encoding='utf-8', newline='') as image:
            writer_image = csv.writer(image)
            for page_number in range(1,12):
                url = "https://www.pnj.com.vn/bong-tai/page-"+ str(page_number)+"/"
                print(url)
                browser = webdriver.Chrome(executable_path='.\Driver\chromedriver.exe', chrome_options=options)
                browser.get(url)
                browser.maximize_window()

                data_product = []
                links = [link.get_attribute("href") for link in browser.find_elements_by_class_name("product-title")]
                i = 1
                for link in links:
                    browser.get(link)
                    name = browser.find_element_by_class_name("ty-product-block-title").text
                    product_code = browser.find_element_by_class_name("product_code_w").text
                    img = browser.find_elements_by_xpath("//img[@class='ty-pict cm-image']")
                    for image in img[1:]:
                        data_image = [id_image,id,image.get_attribute("src")]
                        writer_image.writerow(data_image)
                        id_image += 1
                    if len(img) < 2:
                        print(f"Page:{page_number} ignore item {i}")
                        i += 1
                        continue
                    url_image = img[1].get_attribute('src')
                    category_id = 2
                    collection = ""
                    main_stone_type = ""
                    main_stone_color = ""
                    stone_shape = ""
                    sub_stone_type = ""
                    secondary_stone_color = ""
                    gender = ""
                    gift_giving_occasions = ""
                    gift_for = ""
                    weight_of_gold = ""
                    gold_age = ""
                    style=""
                    wire_size=""
                    face_size=""
                    machine_thickness = ""
                    brand_origin = ""
                    origin_of_the_apparatus = ""
                    assembled_at = ""
                    watch_movement_type = ""
                    glass_type = ""
                    wire_material = ""
                    shell_material = ""
                    face_shape = ""
                    water_resistance = ""
                    needle_number = ""
                    watch_stones_attached = ""
                    chronometer_certification = ""
                    main_function = ""
                    product_info = browser.find_elements_by_class_name("ty-product-feature")
                    for detail in product_info:
                        info = detail.find_element_by_class_name("ty-product-feature__label").text
                        if info == "Th????ng hi???u:":
                            supplier_id = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "B??? s??u t???p:":
                            collection = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ph??? (n???u c??):":
                            sub_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ph??? (n???u c??):":
                            secondary_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ch??nh:":
                            main_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info =="H??nh d???ng ????:":
                            stone_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ch??nh:":
                            main_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Gi???i t??nh:":
                            gender = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "D???p t???ng qu??:":
                            gift_giving_occasion = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_giving_occasionn = gift_giving_occasion.split("\n")
                            for item in gift_giving_occasionn[:]:
                                if item == gift_giving_occasionn[-1]:
                                    gift_giving_occasions = gift_giving_occasions + item
                                else:
                                    gift_giving_occasions = gift_giving_occasions + item + ','
                        if info == "Qu?? t???ng cho ng?????i th??n:":
                            gift_for_who = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_for_x = gift_for_who.split("\n")
                            for item in gift_for_x[:]:
                                if item == gift_for_x[-1]:
                                    gift_for = gift_for + item
                                else:
                                    gift_for = gift_for + item + ','
                        if info == "Tr???ng l?????ng v??ng tham kh???o (ph??n v??ng):":
                            weight_of_gold = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Tu???i v??ng:":
                            gold_age = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Phong c??ch:":
                            style = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c d??y:":
                            wire_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c m???t:":
                            face_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? d??y v??? m??y:":
                            machine_thickness = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t X??? Th????ng Hi???u:":
                            brand_origin = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t x??? b??? m??y:":
                            origin_of_the_apparatus = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "L???p r??p t???i:":
                            assembled_at = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m??y ?????ng h???:":
                            watch_movement_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m???t k??nh:":
                            glass_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u d??y:":
                            wire_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u v???:":
                            shell_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "H??nh d???ng m???t:":
                            face_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? ch???u n?????c:":
                            water_resistance = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "S??? Kim:":
                            needle_number = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "???? G???n K??m ?????ng H???:":
                            watch_stones_attached = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???ng nh???n Chronometer:":
                            chronometer_certification = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???c n??ng ch??nh:":
                            main_function = detail.find_element_by_class_name("ty-product-feature__value").text
                    quantity = randint(5,10)
                    price = browser.find_element_by_class_name("ty-price-num").text
                    item = (id,product_code,url_image,name,price,category_id,supplier_id,quantity,collection,main_stone_type,main_stone_color,stone_shape,sub_stone_type,secondary_stone_color,gender,gift_giving_occasions,gift_for,weight_of_gold,gold_age,style,wire_size,face_size,machine_thickness, brand_origin,origin_of_the_apparatus,assembled_at,watch_movement_type,glass_type,wire_material,shell_material,face_shape,water_resistance,needle_number,watch_stones_attached,chronometer_certification,main_function)
                    print(f"B??ng tai Page:{page_number} get item {i} with data: {item}")
                    data_product.append(item)
                    i += 1
                    id += 1
                    if i == 17:
                        browser.close()
                    sleep(2)
                writer_product.writerows(data_product)
                # print(f"Data page {page_number} is: {data_product}")
    id = id
    id_image = id_image
    sleep(2)
    print("done crawl earring")

def crawl_shake_bracelet():
    global id, id_image
    print("start crawl shake, bracelet")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")

    with open("Result\products.csv", "a+", encoding='utf-8', newline='') as product:
        writer_product = csv.writer(product)
        
        with open("Result\images.csv", "a+", encoding='utf-8', newline='') as image:
            writer_image = csv.writer(image)
            for page_number in range(1,12):
                url = "https://www.pnj.com.vn/lac-vong-tay/page-"+ str(page_number)+"/"
                print(url)
                browser = webdriver.Chrome(executable_path='.\Driver\chromedriver.exe', chrome_options=options)
                browser.get(url)
                browser.maximize_window()

                data_product = []
                links = [link.get_attribute("href") for link in browser.find_elements_by_class_name("product-title")]
                i = 1
                for link in links:
                    browser.get(link)
                    name = browser.find_element_by_class_name("ty-product-block-title").text
                    product_code = browser.find_element_by_class_name("product_code_w").text
                    img = browser.find_elements_by_xpath("//img[@class='ty-pict cm-image']")
                    for image in img[1:]:
                        data_image = [id_image,id,image.get_attribute("src")]
                        writer_image.writerow(data_image)
                        id_image += 1
                    if len(img) < 2:
                        print(f"Page:{page_number} ignore item {i}")
                        i += 1
                        continue
                    url_image = img[1].get_attribute('src')
                    category_id = 3
                    collection = ""
                    main_stone_type = ""
                    main_stone_color = ""
                    stone_shape = ""
                    sub_stone_type = ""
                    secondary_stone_color = ""
                    gender = ""
                    gift_giving_occasions = ""
                    gift_for = ""
                    weight_of_gold = ""
                    gold_age = ""
                    style=""
                    wire_size=""
                    face_size=""
                    machine_thickness = ""
                    brand_origin = ""
                    origin_of_the_apparatus = ""
                    assembled_at = ""
                    watch_movement_type = ""
                    glass_type = ""
                    wire_material = ""
                    shell_material = ""
                    face_shape = ""
                    water_resistance = ""
                    needle_number = ""
                    watch_stones_attached = ""
                    chronometer_certification = ""
                    main_function = ""
                    product_info = browser.find_elements_by_class_name("ty-product-feature")
                    for detail in product_info:
                        info = detail.find_element_by_class_name("ty-product-feature__label").text
                        if info == "Th????ng hi???u:":
                            supplier_id = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "B??? s??u t???p:":
                            collection = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ph??? (n???u c??):":
                            sub_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ph??? (n???u c??):":
                            secondary_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ch??nh:":
                            main_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info =="H??nh d???ng ????:":
                            stone_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ch??nh:":
                            main_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Gi???i t??nh:":
                            gender = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "D???p t???ng qu??:":
                            gift_giving_occasion = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_giving_occasionn = gift_giving_occasion.split("\n")
                            for item in gift_giving_occasionn[:]:
                                if item == gift_giving_occasionn[-1]:
                                    gift_giving_occasions = gift_giving_occasions + item
                                else:
                                    gift_giving_occasions = gift_giving_occasions + item + ','
                        if info == "Qu?? t???ng cho ng?????i th??n:":
                            gift_for_who = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_for_x = gift_for_who.split("\n")
                            for item in gift_for_x[:]:
                                if item == gift_for_x[-1]:
                                    gift_for = gift_for + item
                                else:
                                    gift_for = gift_for + item + ','
                        if info == "Tr???ng l?????ng v??ng tham kh???o (ph??n v??ng):":
                            weight_of_gold = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Tu???i v??ng:":
                            gold_age = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Phong c??ch:":
                            style = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c d??y:":
                            wire_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c m???t:":
                            face_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? d??y v??? m??y:":
                            machine_thickness = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t X??? Th????ng Hi???u:":
                            brand_origin = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t x??? b??? m??y:":
                            origin_of_the_apparatus = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "L???p r??p t???i:":
                            assembled_at = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m??y ?????ng h???:":
                            watch_movement_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m???t k??nh:":
                            glass_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u d??y:":
                            wire_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u v???:":
                            shell_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "H??nh d???ng m???t:":
                            face_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? ch???u n?????c:":
                            water_resistance = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "S??? Kim:":
                            needle_number = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "???? G???n K??m ?????ng H???:":
                            watch_stones_attached = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???ng nh???n Chronometer:":
                            chronometer_certification = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???c n??ng ch??nh:":
                            main_function = detail.find_element_by_class_name("ty-product-feature__value").text
                    quantity = randint(5,10)
                    price = browser.find_element_by_class_name("ty-price-num").text
                    item = (id,product_code,url_image,name,price,category_id,supplier_id,quantity,collection,main_stone_type,main_stone_color,stone_shape,sub_stone_type,secondary_stone_color,gender,gift_giving_occasions,gift_for,weight_of_gold,gold_age,style,wire_size,face_size,machine_thickness, brand_origin,origin_of_the_apparatus,assembled_at,watch_movement_type,glass_type,wire_material,shell_material,face_shape,water_resistance,needle_number,watch_stones_attached,chronometer_certification,main_function)
                    print(f"L???c, V??ng tay Page:{page_number} get item {i} with data: {item}")
                    data_product.append(item)
                    i += 1
                    id += 1
                    if i == 17:
                        browser.close()
                    sleep(2)
                writer_product.writerows(data_product)
                # print(f"Data page {page_number} is: {data_product}")
    id = id
    id_image = id_image
    sleep(2)
    print("done crawl shake, beacelet")

def crawl_clock():
    global id, id_image
    print("start crawl clock")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")

    with open("Result\products.csv", "a+", encoding='utf-8', newline='') as product:
        writer_product = csv.writer(product)
        
        with open("Result\images.csv", "a+", encoding='utf-8', newline='') as image:
            writer_image = csv.writer(image)
            for page_number in range(1,12):
                url = "https://www.pnj.com.vn/dong-ho/page-"+ str(page_number)+"/"
                print(url)
                browser = webdriver.Chrome(executable_path='.\Driver\chromedriver.exe', chrome_options=options)
                browser.get(url)
                browser.maximize_window()

                data_product = []
                links = [link.get_attribute("href") for link in browser.find_elements_by_class_name("product-title")]
                i = 1
                for link in links:
                    browser.get(link)
                    name = browser.find_element_by_class_name("ty-product-block-title").text
                    product_code = browser.find_element_by_class_name("product_code_w").text
                    img = browser.find_elements_by_xpath("//img[@class='ty-pict cm-image']")
                    for image in img[1:]:
                        data_image = [id_image,id,image.get_attribute("src")]
                        writer_image.writerow(data_image)
                        id_image += 1
                    if len(img) < 2:
                        print(f"Page:{page_number} ignore item {i}")
                        i += 1
                        continue
                    url_image = img[1].get_attribute('src')
                    category_id = 4
                    collection = ""
                    main_stone_type = ""
                    main_stone_color = ""
                    stone_shape = ""
                    sub_stone_type = ""
                    secondary_stone_color = ""
                    gender = ""
                    gift_giving_occasions = ""
                    gift_for = ""
                    weight_of_gold = ""
                    gold_age = ""
                    style=""
                    wire_size=""
                    face_size=""
                    machine_thickness = ""
                    brand_origin = ""
                    origin_of_the_apparatus = ""
                    assembled_at = ""
                    watch_movement_type = ""
                    glass_type = ""
                    wire_material = ""
                    shell_material = ""
                    face_shape = ""
                    water_resistance = ""
                    needle_number = ""
                    watch_stones_attached = ""
                    chronometer_certification = ""
                    main_function = ""
                    product_info = browser.find_elements_by_class_name("ty-product-feature")
                    for detail in product_info:
                        info = detail.find_element_by_class_name("ty-product-feature__label").text
                        if info == "Th????ng hi???u:":
                            supplier_id = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "B??? s??u t???p:":
                            collection = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ph??? (n???u c??):":
                            sub_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ph??? (n???u c??):":
                            secondary_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ch??nh:":
                            main_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info =="H??nh d???ng ????:":
                            stone_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ch??nh:":
                            main_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Gi???i t??nh:":
                            gender = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "D???p t???ng qu??:":
                            gift_giving_occasion = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_giving_occasionn = gift_giving_occasion.split("\n")
                            for item in gift_giving_occasionn[:]:
                                if item == gift_giving_occasionn[-1]:
                                    gift_giving_occasions = gift_giving_occasions + item
                                else:
                                    gift_giving_occasions = gift_giving_occasions + item + ','
                        if info == "Qu?? t???ng cho ng?????i th??n:":
                            gift_for_who = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_for_x = gift_for_who.split("\n")
                            for item in gift_for_x[:]:
                                if item == gift_for_x[-1]:
                                    gift_for = gift_for + item
                                else:
                                    gift_for = gift_for + item + ','
                        if info == "Tr???ng l?????ng v??ng tham kh???o (ph??n v??ng):":
                            weight_of_gold = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Tu???i v??ng:":
                            gold_age = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Phong c??ch:":
                            style = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c d??y:":
                            wire_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c m???t:":
                            face_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? d??y v??? m??y:":
                            machine_thickness = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t X??? Th????ng Hi???u:":
                            brand_origin = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t x??? b??? m??y:":
                            origin_of_the_apparatus = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "L???p r??p t???i:":
                            assembled_at = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m??y ?????ng h???:":
                            watch_movement_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m???t k??nh:":
                            glass_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u d??y:":
                            wire_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u v???:":
                            shell_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "H??nh d???ng m???t:":
                            face_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? ch???u n?????c:":
                            water_resistance = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "S??? Kim:":
                            needle_number = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "???? G???n K??m ?????ng H???:":
                            watch_stones_attached = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???ng nh???n Chronometer:":
                            chronometer_certification = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???c n??ng ch??nh:":
                            main_function = detail.find_element_by_class_name("ty-product-feature__value").text
                    quantity = randint(5,10)
                    price = browser.find_element_by_class_name("ty-price-num").text
                    item = (id,product_code,url_image,name,price,category_id,supplier_id,quantity,collection,main_stone_type,main_stone_color,stone_shape,sub_stone_type,secondary_stone_color,gender,gift_giving_occasions,gift_for,weight_of_gold,gold_age,style,wire_size,face_size,machine_thickness, brand_origin,origin_of_the_apparatus,assembled_at,watch_movement_type,glass_type,wire_material,shell_material,face_shape,water_resistance,needle_number,watch_stones_attached,chronometer_certification,main_function)
                    print(f"?????ng h??? Page:{page_number} get item {i} with data: {item}")
                    data_product.append(item)
                    i += 1
                    id += 1
                    if i == 17:
                        browser.close()
                    sleep(2)
                writer_product.writerows(data_product)
                # print(f"Data page {page_number} is: {data_product}")
    id = id
    id_image = id_image
    sleep(2)
    print("done crawl clock")

def crawl_necklace():
    global id, id_image
    print("start crawl necklace")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")

    with open("Result\products.csv", "a+", encoding='utf-8', newline='') as product:
        writer_product = csv.writer(product)
        
        with open("Result\images.csv", "a+", encoding='utf-8', newline='') as image:
            writer_image = csv.writer(image)
            for page_number in range(1,12):
                url = "https://www.pnj.com.vn/day-chuyen/day-chuyen-vang-bac/page-"+ str(page_number)+"/"
                print(url)
                browser = webdriver.Chrome(executable_path='.\Driver\chromedriver.exe', chrome_options=options)
                browser.get(url)
                browser.maximize_window()

                data_product = []
                links = [link.get_attribute("href") for link in browser.find_elements_by_class_name("product-title")]
                i = 1
                for link in links:
                    browser.get(link)
                    name = browser.find_element_by_class_name("ty-product-block-title").text
                    product_code = browser.find_element_by_class_name("product_code_w").text
                    img = browser.find_elements_by_xpath("//img[@class='ty-pict cm-image']")
                    for image in img[1:]:
                        data_image = [id_image,id,image.get_attribute("src")]
                        writer_image.writerow(data_image)
                        id_image += 1
                    if len(img) < 2:
                        print(f"Page:{page_number} ignore item {i}")
                        i += 1
                        continue
                    url_image = img[1].get_attribute('src')
                    category_id = 5
                    collection = ""
                    main_stone_type = ""
                    main_stone_color = ""
                    stone_shape = ""
                    sub_stone_type = ""
                    secondary_stone_color = ""
                    gender = ""
                    gift_giving_occasions = ""
                    gift_for = ""
                    weight_of_gold = ""
                    gold_age = ""
                    style=""
                    wire_size=""
                    face_size=""
                    machine_thickness = ""
                    brand_origin = ""
                    origin_of_the_apparatus = ""
                    assembled_at = ""
                    watch_movement_type = ""
                    glass_type = ""
                    wire_material = ""
                    shell_material = ""
                    face_shape = ""
                    water_resistance = ""
                    needle_number = ""
                    watch_stones_attached = ""
                    chronometer_certification = ""
                    main_function = ""
                    product_info = browser.find_elements_by_class_name("ty-product-feature")
                    for detail in product_info:
                        info = detail.find_element_by_class_name("ty-product-feature__label").text
                        if info == "Th????ng hi???u:":
                            supplier_id = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "B??? s??u t???p:":
                            collection = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ph??? (n???u c??):":
                            sub_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ph??? (n???u c??):":
                            secondary_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ch??nh:":
                            main_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info =="H??nh d???ng ????:":
                            stone_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ch??nh:":
                            main_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Gi???i t??nh:":
                            gender = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "D???p t???ng qu??:":
                            gift_giving_occasion = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_giving_occasionn = gift_giving_occasion.split("\n")
                            for item in gift_giving_occasionn[:]:
                                if item == gift_giving_occasionn[-1]:
                                    gift_giving_occasions = gift_giving_occasions + item
                                else:
                                    gift_giving_occasions = gift_giving_occasions + item + ','
                        if info == "Qu?? t???ng cho ng?????i th??n:":
                            gift_for_who = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_for_x = gift_for_who.split("\n")
                            for item in gift_for_x[:]:
                                if item == gift_for_x[-1]:
                                    gift_for = gift_for + item
                                else:
                                    gift_for = gift_for + item + ','
                        if info == "Tr???ng l?????ng v??ng tham kh???o (ph??n v??ng):":
                            weight_of_gold = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Tu???i v??ng:":
                            gold_age = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Phong c??ch:":
                            style = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c d??y:":
                            wire_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c m???t:":
                            face_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? d??y v??? m??y:":
                            machine_thickness = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t X??? Th????ng Hi???u:":
                            brand_origin = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t x??? b??? m??y:":
                            origin_of_the_apparatus = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "L???p r??p t???i:":
                            assembled_at = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m??y ?????ng h???:":
                            watch_movement_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m???t k??nh:":
                            glass_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u d??y:":
                            wire_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u v???:":
                            shell_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "H??nh d???ng m???t:":
                            face_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? ch???u n?????c:":
                            water_resistance = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "S??? Kim:":
                            needle_number = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "???? G???n K??m ?????ng H???:":
                            watch_stones_attached = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???ng nh???n Chronometer:":
                            chronometer_certification = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???c n??ng ch??nh:":
                            main_function = detail.find_element_by_class_name("ty-product-feature__value").text
                    quantity = randint(5,10)
                    price = browser.find_element_by_class_name("ty-price-num").text
                    item = (id,product_code,url_image,name,price,category_id,supplier_id,quantity,collection,main_stone_type,main_stone_color,stone_shape,sub_stone_type,secondary_stone_color,gender,gift_giving_occasions,gift_for,weight_of_gold,gold_age,style,wire_size,face_size,machine_thickness, brand_origin,origin_of_the_apparatus,assembled_at,watch_movement_type,glass_type,wire_material,shell_material,face_shape,water_resistance,needle_number,watch_stones_attached,chronometer_certification,main_function)
                    print(f"D??y chuy???n Page:{page_number} get item {i} with data: {item}")
                    data_product.append(item)
                    i += 1
                    id += 1
                    if i == 17:
                        browser.close()
                    sleep(2)
                writer_product.writerows(data_product)
                # print(f"Data page {page_number} is: {data_product}")
    id = id
    id_image = id_image
    sleep(2)
    print("done crawl necklace")

def crawl_pendant():
    global id, id_image
    print("start crawl pendant")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")

    with open("Result\products.csv", "a+", encoding='utf-8', newline='') as product:
        writer_product = csv.writer(product)
        
        with open("Result\images.csv", "a+", encoding='utf-8', newline='') as image:
            writer_image = csv.writer(image)
            for page_number in range(1,12):
                url = "https://www.pnj.com.vn/day-chuyen/mat-day-chuyen/page-"+ str(page_number)+"/"
                print(url)
                if page_number == 7:
                    print(f"Ignore page {page_number} url: {url}")
                    continue
                browser = webdriver.Chrome(executable_path='.\Driver\chromedriver.exe', chrome_options=options)
                browser.get(url)
                browser.maximize_window()

                data_product = []
                links = [link.get_attribute("href") for link in browser.find_elements_by_class_name("product-title")]
                i = 1
                for link in links:
                    browser.get(link)
                    name = browser.find_element_by_class_name("ty-product-block-title").text
                    product_code = browser.find_element_by_class_name("product_code_w").text
                    img = browser.find_elements_by_xpath("//img[@class='ty-pict cm-image']")
                    for image in img[1:]:
                        data_image = [id_image,id,image.get_attribute("src")]
                        writer_image.writerow(data_image)
                        id_image += 1
                    if len(img) < 2:
                        print(f"Page:{page_number} ignore item {i}")
                        i += 1
                        continue
                    url_image = img[1].get_attribute('src')
                    category_id = 6
                    collection = ""
                    main_stone_type = ""
                    main_stone_color = ""
                    stone_shape = ""
                    sub_stone_type = ""
                    secondary_stone_color = ""
                    gender = ""
                    gift_giving_occasions = ""
                    gift_for = ""
                    weight_of_gold = ""
                    gold_age = ""
                    style=""
                    wire_size=""
                    face_size=""
                    machine_thickness = ""
                    brand_origin = ""
                    origin_of_the_apparatus = ""
                    assembled_at = ""
                    watch_movement_type = ""
                    glass_type = ""
                    wire_material = ""
                    shell_material = ""
                    face_shape = ""
                    water_resistance = ""
                    needle_number = ""
                    watch_stones_attached = ""
                    chronometer_certification = ""
                    main_function = ""
                    product_info = browser.find_elements_by_class_name("ty-product-feature")
                    for detail in product_info:
                        info = detail.find_element_by_class_name("ty-product-feature__label").text
                        if info == "Th????ng hi???u:":
                            supplier_id = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "B??? s??u t???p:":
                            collection = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ph??? (n???u c??):":
                            sub_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ph??? (n???u c??):":
                            secondary_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ch??nh:":
                            main_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info =="H??nh d???ng ????:":
                            stone_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ch??nh:":
                            main_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Gi???i t??nh:":
                            gender = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "D???p t???ng qu??:":
                            gift_giving_occasion = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_giving_occasionn = gift_giving_occasion.split("\n")
                            for item in gift_giving_occasionn[:]:
                                if item == gift_giving_occasionn[-1]:
                                    gift_giving_occasions = gift_giving_occasions + item
                                else:
                                    gift_giving_occasions = gift_giving_occasions + item + ','
                        if info == "Qu?? t???ng cho ng?????i th??n:":
                            gift_for_who = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_for_x = gift_for_who.split("\n")
                            for item in gift_for_x[:]:
                                if item == gift_for_x[-1]:
                                    gift_for = gift_for + item
                                else:
                                    gift_for = gift_for + item + ','
                        if info == "Tr???ng l?????ng v??ng tham kh???o (ph??n v??ng):":
                            weight_of_gold = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Tu???i v??ng:":
                            gold_age = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Phong c??ch:":
                            style = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c d??y:":
                            wire_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c m???t:":
                            face_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? d??y v??? m??y:":
                            machine_thickness = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t X??? Th????ng Hi???u:":
                            brand_origin = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t x??? b??? m??y:":
                            origin_of_the_apparatus = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "L???p r??p t???i:":
                            assembled_at = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m??y ?????ng h???:":
                            watch_movement_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m???t k??nh:":
                            glass_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u d??y:":
                            wire_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u v???:":
                            shell_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "H??nh d???ng m???t:":
                            face_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? ch???u n?????c:":
                            water_resistance = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "S??? Kim:":
                            needle_number = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "???? G???n K??m ?????ng H???:":
                            watch_stones_attached = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???ng nh???n Chronometer:":
                            chronometer_certification = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???c n??ng ch??nh:":
                            main_function = detail.find_element_by_class_name("ty-product-feature__value").text
                    quantity = randint(5,10)
                    price = browser.find_element_by_class_name("ty-price-num").text
                    item = (id,product_code,url_image,name,price,category_id,supplier_id,quantity,collection,main_stone_type,main_stone_color,stone_shape,sub_stone_type,secondary_stone_color,gender,gift_giving_occasions,gift_for,weight_of_gold,gold_age,style,wire_size,face_size,machine_thickness, brand_origin,origin_of_the_apparatus,assembled_at,watch_movement_type,glass_type,wire_material,shell_material,face_shape,water_resistance,needle_number,watch_stones_attached,chronometer_certification,main_function)
                    print(f"M???t d??y chuy???n Page:{page_number} get item {i} with data: {item}")
                    data_product.append(item)
                    i += 1
                    id += 1
                    if i == 17:
                        browser.close()
                    sleep(2)
                writer_product.writerows(data_product)
                # print(f"Data page {page_number} is: {data_product}")
    id = id
    id_image = id_image
    sleep(2)
    print("done crawl pendant")

def crawl_neck_cord():
    global id, id_image
    print("start crawl neck cord")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")

    with open("Result\products.csv", "a+", encoding='utf-8', newline='') as product:
        writer_product = csv.writer(product)
        
        with open("Result\images.csv", "a+", encoding='utf-8', newline='') as image:
            writer_image = csv.writer(image)
            for page_number in range(1,12):
                url = "https://www.pnj.com.vn/day-co/page-"+ str(page_number)+"/"
                print(url)
                browser = webdriver.Chrome(executable_path='.\Driver\chromedriver.exe', chrome_options=options)
                browser.get(url)
                browser.maximize_window()

                data_product = []
                links = [link.get_attribute("href") for link in browser.find_elements_by_class_name("product-title")]
                i = 1
                for link in links:
                    browser.get(link)
                    name = browser.find_element_by_class_name("ty-product-block-title").text
                    product_code = browser.find_element_by_class_name("product_code_w").text
                    img = browser.find_elements_by_xpath("//img[@class='ty-pict cm-image']")
                    for image in img[1:]:
                        data_image = [id_image,id,image.get_attribute("src")]
                        writer_image.writerow(data_image)
                        id_image += 1
                    if len(img) < 2:
                        print(f"Page:{page_number} ignore item {i}")
                        i += 1
                        continue
                    url_image = img[1].get_attribute('src')
                    category_id = 7
                    collection = ""
                    main_stone_type = ""
                    main_stone_color = ""
                    stone_shape = ""
                    sub_stone_type = ""
                    secondary_stone_color = ""
                    gender = ""
                    gift_giving_occasions = ""
                    gift_for = ""
                    weight_of_gold = ""
                    gold_age = ""
                    style=""
                    wire_size=""
                    face_size=""
                    machine_thickness = ""
                    brand_origin = ""
                    origin_of_the_apparatus = ""
                    assembled_at = ""
                    watch_movement_type = ""
                    glass_type = ""
                    wire_material = ""
                    shell_material = ""
                    face_shape = ""
                    water_resistance = ""
                    needle_number = ""
                    watch_stones_attached = ""
                    chronometer_certification = ""
                    main_function = ""
                    product_info = browser.find_elements_by_class_name("ty-product-feature")
                    for detail in product_info:
                        info = detail.find_element_by_class_name("ty-product-feature__label").text
                        if info == "Th????ng hi???u:":
                            supplier_id = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "B??? s??u t???p:":
                            collection = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ph??? (n???u c??):":
                            sub_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ph??? (n???u c??):":
                            secondary_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ch??nh:":
                            main_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info =="H??nh d???ng ????:":
                            stone_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ch??nh:":
                            main_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Gi???i t??nh:":
                            gender = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "D???p t???ng qu??:":
                            gift_giving_occasion = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_giving_occasionn = gift_giving_occasion.split("\n")
                            for item in gift_giving_occasionn[:]:
                                if item == gift_giving_occasionn[-1]:
                                    gift_giving_occasions = gift_giving_occasions + item
                                else:
                                    gift_giving_occasions = gift_giving_occasions + item + ','
                        if info == "Qu?? t???ng cho ng?????i th??n:":
                            gift_for_who = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_for_x = gift_for_who.split("\n")
                            for item in gift_for_x[:]:
                                if item == gift_for_x[-1]:
                                    gift_for = gift_for + item
                                else:
                                    gift_for = gift_for + item + ','
                        if info == "Tr???ng l?????ng v??ng tham kh???o (ph??n v??ng):":
                            weight_of_gold = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Tu???i v??ng:":
                            gold_age = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Phong c??ch:":
                            style = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c d??y:":
                            wire_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c m???t:":
                            face_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? d??y v??? m??y:":
                            machine_thickness = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t X??? Th????ng Hi???u:":
                            brand_origin = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t x??? b??? m??y:":
                            origin_of_the_apparatus = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "L???p r??p t???i:":
                            assembled_at = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m??y ?????ng h???:":
                            watch_movement_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m???t k??nh:":
                            glass_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u d??y:":
                            wire_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u v???:":
                            shell_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "H??nh d???ng m???t:":
                            face_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? ch???u n?????c:":
                            water_resistance = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "S??? Kim:":
                            needle_number = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "???? G???n K??m ?????ng H???:":
                            watch_stones_attached = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???ng nh???n Chronometer:":
                            chronometer_certification = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???c n??ng ch??nh:":
                            main_function = detail.find_element_by_class_name("ty-product-feature__value").text
                    quantity = randint(5,10)
                    price = browser.find_element_by_class_name("ty-price-num").text
                    item = (id,product_code,url_image,name,price,category_id,supplier_id,quantity,collection,main_stone_type,main_stone_color,stone_shape,sub_stone_type,secondary_stone_color,gender,gift_giving_occasions,gift_for,weight_of_gold,gold_age,style,wire_size,face_size,machine_thickness, brand_origin,origin_of_the_apparatus,assembled_at,watch_movement_type,glass_type,wire_material,shell_material,face_shape,water_resistance,needle_number,watch_stones_attached,chronometer_certification,main_function)
                    print(f"D??y c??? Page:{page_number} get item {i} with data: {item}")
                    data_product.append(item)
                    i += 1
                    id += 1
                    if i == 17:
                        browser.close()
                    sleep(2)
                writer_product.writerows(data_product)
                # print(f"Data page {page_number} is: {data_product}")
    id = id
    id_image = id_image
    sleep(2)
    print("done crawl neck cord")

def crawl_accessory():
    global id, id_image
    print("start crawl accessory")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")

    with open("Result\products.csv", "a+", encoding='utf-8', newline='') as product:
        writer_product = csv.writer(product)
        
        with open("Result\images.csv", "a+", encoding='utf-8', newline='') as image:
            writer_image = csv.writer(image)
            for page_number in range(1,12):
                url = "https://www.pnj.com.vn/charm/page-"+ str(page_number)+"/"
                print(url)
                browser = webdriver.Chrome(executable_path='.\Driver\chromedriver.exe', chrome_options=options)
                browser.get(url)
                browser.maximize_window()

                data_product = []
                links = [link.get_attribute("href") for link in browser.find_elements_by_class_name("product-title")]
                i = 1
                for link in links:
                    browser.get(link)
                    name = browser.find_element_by_class_name("ty-product-block-title").text
                    product_code = browser.find_element_by_class_name("product_code_w").text
                    img = browser.find_elements_by_xpath("//img[@class='ty-pict cm-image']")
                    for image in img[1:]:
                        data_image = [id_image,id,image.get_attribute("src")]
                        writer_image.writerow(data_image)
                        id_image += 1
                    if len(img) < 2:
                        print(f"Page:{page_number} ignore item {i}")
                        i += 1
                        continue
                    url_image = img[1].get_attribute('src')
                    category_id = 8
                    collection = ""
                    main_stone_type = ""
                    main_stone_color = ""
                    stone_shape = ""
                    sub_stone_type = ""
                    secondary_stone_color = ""
                    gender = ""
                    gift_giving_occasions = ""
                    gift_for = ""
                    weight_of_gold = ""
                    gold_age = ""
                    style=""
                    wire_size=""
                    face_size=""
                    machine_thickness = ""
                    brand_origin = ""
                    origin_of_the_apparatus = ""
                    assembled_at = ""
                    watch_movement_type = ""
                    glass_type = ""
                    wire_material = ""
                    shell_material = ""
                    face_shape = ""
                    water_resistance = ""
                    needle_number = ""
                    watch_stones_attached = ""
                    chronometer_certification = ""
                    main_function = ""
                    product_info = browser.find_elements_by_class_name("ty-product-feature")
                    for detail in product_info:
                        info = detail.find_element_by_class_name("ty-product-feature__label").text
                        if info == "Th????ng hi???u:":
                            supplier_id = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "B??? s??u t???p:":
                            collection = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ph??? (n???u c??):":
                            sub_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ph??? (n???u c??):":
                            secondary_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "M??u ???? ch??nh:":
                            main_stone_color = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info =="H??nh d???ng ????:":
                            stone_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i ???? ch??nh:":
                            main_stone_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Gi???i t??nh:":
                            gender = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "D???p t???ng qu??:":
                            gift_giving_occasion = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_giving_occasionn = gift_giving_occasion.split("\n")
                            for item in gift_giving_occasionn[:]:
                                if item == gift_giving_occasionn[-1]:
                                    gift_giving_occasions = gift_giving_occasions + item
                                else:
                                    gift_giving_occasions = gift_giving_occasions + item + ','
                        if info == "Qu?? t???ng cho ng?????i th??n:":
                            gift_for_who = detail.find_element_by_class_name("ty-product-feature__value").text
                            gift_for_x = gift_for_who.split("\n")
                            for item in gift_for_x[:]:
                                if item == gift_for_x[-1]:
                                    gift_for = gift_for + item
                                else:
                                    gift_for = gift_for + item + ','
                        if info == "Tr???ng l?????ng v??ng tham kh???o (ph??n v??ng):":
                            weight_of_gold = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Tu???i v??ng:":
                            gold_age = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Phong c??ch:":
                            style = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c d??y:":
                            wire_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "K??ch th?????c m???t:":
                            face_size = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? d??y v??? m??y:":
                            machine_thickness = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t X??? Th????ng Hi???u:":
                            brand_origin = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Xu???t x??? b??? m??y:":
                            origin_of_the_apparatus = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "L???p r??p t???i:":
                            assembled_at = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m??y ?????ng h???:":
                            watch_movement_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Lo???i m???t k??nh:":
                            glass_type = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u d??y:":
                            wire_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???t li???u v???:":
                            shell_material = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "H??nh d???ng m???t:":
                            face_shape = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "????? ch???u n?????c:":
                            water_resistance = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "S??? Kim:":
                            needle_number = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "???? G???n K??m ?????ng H???:":
                            watch_stones_attached = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???ng nh???n Chronometer:":
                            chronometer_certification = detail.find_element_by_class_name("ty-product-feature__value").text
                        if info == "Ch???c n??ng ch??nh:":
                            main_function = detail.find_element_by_class_name("ty-product-feature__value").text
                    quantity = randint(5,10)
                    price = browser.find_element_by_class_name("ty-price-num").text
                    item = (id,product_code,url_image,name,price,category_id,supplier_id,quantity,collection,main_stone_type,main_stone_color,stone_shape,sub_stone_type,secondary_stone_color,gender,gift_giving_occasions,gift_for,weight_of_gold,gold_age,style,wire_size,face_size,machine_thickness, brand_origin,origin_of_the_apparatus,assembled_at,watch_movement_type,glass_type,wire_material,shell_material,face_shape,water_resistance,needle_number,watch_stones_attached,chronometer_certification,main_function)
                    print(f"Ph??? ki???n Page:{page_number} get item {i} with data: {item}")
                    data_product.append(item)
                    i += 1
                    id += 1
                    if i == 17:
                        browser.close()
                    sleep(2)
                writer_product.writerows(data_product)
                # print(f"Data page {page_number} is: {data_product}")
    id = id
    id_image = id_image
    sleep(2)
    print("done crawl accessory")

def main():
    print(f"Start Crawl at: {datetime.now()}")
    print("---------------------------------------------------------------------------------------------------------")
    start_time = datetime.now()
    crawl_rings()
    crawl_earring()
    crawl_accessory()
    crawl_clock()
    crawl_neck_cord()
    crawl_necklace()
    crawl_pendant()
    crawl_shake_bracelet()
    end_time = datetime.now()
    print("---------------------------------------------------------------------------------------------------------")
    print(f"Crawl Successfully at: {datetime.now()}")
    print(f"Total crawl time: {end_time - start_time}")

if __name__ == '__main__':
    main()