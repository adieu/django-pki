# Generated by the windmill services transformer
from windmill.authoring import WindmillTestClient

def test_ViewsWithoutLogin():
    client = WindmillTestClient(__name__)

    client.open(url=u'http://127.0.0.1:8000/admin/logout/')
    client.waits.forPageLoad(timeout=u'8000')
    client.open(url=u'http://127.0.0.1:8000/pki/download/ca/1/')
    client.waits.forPageLoad(timeout=u'8000')
    client.asserts.assertNode(xpath=u"//form[@id='login-form']/div[4]")
    client.open(url=u'http://127.0.0.1:8000/pki/download/cert/1/')
    client.waits.forPageLoad(timeout=u'8000')
    client.asserts.assertNode(xpath=u"//form[@id='login-form']/div[4]")