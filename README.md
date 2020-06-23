# 爬虫——高德找房

步骤：分析自如页面——》爬取——》存储——》显示。

## 爬取

1. soup.find_all()
    获取页内所有元素，eg:'a'; id='name'; class_='cname'
2. soup.find()
    获取仅有的一个元素，eg:同上
    返回soup，用get_text()获取文本
3. soup.select()
    css选择器；获取所有元素，eg: 'head > title'; '.class'; '#id'; 'a\[href\]'
    select返回一个list;需[0].string获取文本
