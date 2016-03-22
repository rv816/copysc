from copysc.copyscreen import convert_clipboard

def test_copyscreen():
    link = 'http://screencloud.net/v/lOss'
    converted = convert_clipboard(link=link)
    assert converted == 'http://sc-cdn.scaleengine.net/i/4a481a8c65e1100b7e87fa90f3d71236.png'
