from flask import Flask, jsonify,request

from app.forms.book import SearchForm
from app.web.helper import is_isbn_or_key
from app.web.yushu_book import YuShuBook

from . import web
@web.route('/book/search/<q>/<page>')
def search(q,page):
    """
    :param q:
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    print(isbn_or_key)
    if isbn_or_key=='isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)

#get请求，通过?page=某个值传参
@web.route('/book/search2/')
def search2():
    """
    :param q:
    :param page:
    :return:
    """
    q = request.args['q']
    isbn_or_key = is_isbn_or_key(q)
    print(isbn_or_key)
    if isbn_or_key=='isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)


#在之前的基础上添加校验层
@web.route('/book/search3/')
def search3():
    """
    :param q:
    :param page:
    :return:
    """
    #校验
    form = SearchForm(request.args)
    #是否通过
    if form.validate():
        q = form.q.data.strip()
        result = YuShuBook.search_by_isbn(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
