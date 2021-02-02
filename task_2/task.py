import httplib2
import base64
import hashlib

FILE_NAME = "img.jpg"
FILE_NAME_BASE64 = "file64"
URL = "https://camo.githubusercontent.com/888e388801f947dec7c3d843942c277af25fe2b1aed1821542c4e711f210312a/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f632f63332f507974686f6e2d6c6f676f2d6e6f746578742e7376672f37363870782d507974686f6e2d6c6f676f2d6e6f746578742e7376672e706e67"


def download_img(
        url: str,
        file_name: str
):
    h = httplib2.Http('.cache')
    response, content = h.request(url)
    with open(file_name, 'wb')as file:
        file.write(content)


def download_img_base64(
        url: str,
):
    h = httplib2.Http('.cache')
    response, content = h.request(url)
    b64_string = base64.b64encode(content)
    name_file = hashlib.md5(b64_string).hexdigest()
    with open(name_file, 'wb')as file:
        file.write(b64_string)
        print(f'Name file base64 {name_file}')
    return name_file


def convert_base64(
        file_name: str = FILE_NAME,
):
    with open(file_name, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
        name_file = hashlib.md5(b64_string).hexdigest()
        print(name_file)
        with open(name_file, "wb") as file_64:
            file_64.write(b64_string)


def convert_now(file_name, new_file_name):
    with open(file_name, "rb") as img_file:
        with open(new_file_name, "wb") as img_file_new:
            s = base64.b64decode(img_file.read())
            img_file_new.write(s)
        print(f"jpg img name {new_file_name}")


if __name__ == '__main__':
    print(f"""
    1 - t По заданной ссылке загрузить изображение jpg из интернета, закодировать его в base64 и сохранить в бинарном файле с названием, полученным по алгоритму md5 из содержимого бинарного файла.
    Б. Преобразовать файл из пункта А в обычный jpg файл 
    """
          )
    base64_img = download_img_base64(url=URL)
    convert_now(file_name=base64_img, new_file_name=FILE_NAME)