import random

from . import string

# 测试数据
test_text = str(random.randint(100000, 200000))
test_value = random.randint(0, 9999)
test_value2 = True
test_value3 = test_text


def test_shuffle():
    """
    测试shuffle

    :return: None
    """
    assert (
        all(i in string.shuffle(test_text) for i in tuple(test_text)) is True
    )  # 检测打乱了之后字母一致
    assert len(string.shuffle(test_text)) == len(test_text)  # 检测打乱了之后长度一致

    assert isinstance(string.shuffle(test_text, show_seed=True)[1], int)  # 展示种子


def test_drop():
    """
    测试drop

    :return: None
    """
    assert len(string.drop(test_text, how_many=0.5)) == ((len(test_text)) * 0.5)  # 去除一半
    assert len(string.drop(test_text, how_many=2)) == (len(test_text) - 2)  # 去除两个

    assert isinstance(
        string.drop(test_text, how_many=0.5, show_seed=True)[1], int
    )  # 展示种子
