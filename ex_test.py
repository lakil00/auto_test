# encoding: utf-8
'''
Created on Dec 10, 2014

@author: yju
'''
import basetest
import unittest
import requests
import settings
# import copy



class TestF_CS_1032136(basetest.BaseTest):
    """
    B2B - given countries' /business/index.html must be 301 to /business/
    """

    def test_redirection_business_index_html(self):
        countries = ['ph', 'sg', 'at', 'be', 'be_fr', 'bg', 'ch_fr', 'ch', 'cz', 'de', 'dk', 'ee', 'es', 'fi', 'fr', \
                      'gr', 'hr', 'hu', 'it', 'lt', 'lv', 'nl', 'no', 'pl', 'pt', 'ro', 'rs', 'se', 'sk', 'cn', 'hk', 'tw', 'hk_en', 'ie']
        redirections = [('/%s/business/index.html' % x, '/%s/business/' % x) for x in countries]
        self.verify_redirection(redirections)
            
class TestF_CS_1023117(basetest.BaseTest):
    """
    b2b section redirection for SI and IRAN. 
    """
    
    countries = ['si', 'iran']
    
    def test_redirection(self):
        pre_redirections = [('/business/home', '/business/'),
                        ('/business/home/', '/business/'),
                        ('/business/resource/*', '/business/insights/*'),
                        ('/business/resource', '/business/insights/'),
                        ('/business/resource/index.html', '/business/insights/'),
                        ('/business/resource/bli-report', '/business/insights/'),
                        ('/business/resource/solution-brief', '/business/insights/'),
                        ('/business/resource/article', '/business/insights/'),
                        ('/business/resource/installation-guide', '/business/insights/'),
                        ('/business/resource/bli-report/', '/business/insights/'),
                        ('/business/resource/solution-brief/', '/business/insights/'),
                        ('/business/resource/article/', '/business/insights/'),
                        ('/business/resource/installation-guide/', '/business/insights/')]
        redirections = [('/%s%s' % (country, pre_source), '/%s%s' %(country, pre_dest)) for country in self.countries for pre_source, pre_dest in pre_redirections]
        self.verify_redirection(redirections)
                
    def test_uppercase_code(self):
        pre_redirections = [('/business/support', '/business/support/'),
                        ('/business/insights', '/business/insights/'),
                        ('/business/step', '/business/step/'),
                        ('/business/ebc', '/business/ebc/'),
                        ('/business/countrysite', '/business/countrysite/'),
                        ('/business/support/*', '/business/support/*'),
                        ('/business/insights/*', '/business/insights/*'),
                        ('/business/step/*', '/business/step/*'),
                        ('/business/ebc/*', '/business/ebc/*'),
                        ('/business/countrysite/*', '/business/countrysite/*'),]
        redirections = [('/%s%s' % (country.upper(), pre_source), '/%s%s' % (country, pre_dest)) for country in self.countries for pre_source, pre_dest in pre_redirections]
        self.verify_redirection(redirections)
                
    def test_redirection_index_html(self):
        redirections = [('/%s/business/index.html' % country, '/%s/business/' % country) for country in self.countries]
        self.verify_redirection(redirections)
            
    def test_remove_redirection(self):
        urls = ['/business/', ]
        for country in self.countries:
            for url_item in urls:
                url = settings.BASE_URL+'/%s%s' % (country, url_item)
                settings.verbose_print('requesting %s...' % url)
                res = requests.get(url,headers=settings.HEADERS, allow_redirects=False)
                settings.verbose_print('%d - %s' %(res.status_code, res.url))
                self.assertNotIn(res.status_code, [301, 302], 'Unexpected redirection found')
                

class TestF_CS_1013642(basetest.BaseTest):
    """
    this is for new country expansion, SI. redirections required.
    """
    
    def test_redirection(self):
        redirections = [('/si/support/supportMain.do', 'http://www.samsung.com/si/support/'),
                        ('/si/support/usefulsoftware/ASPS/JSP', 'http://www.samsung.com/si/support/usefulsoftware/KIES'),
                        ('/si/support/usefulsoftware/FOTA/JSP', 'http://www.samsung.com/si/support/usefulsoftware/FOTA'),
                        ('/si/support/usefulsoftware/KIES/JSP', 'http://www.samsung.com/si/support/usefulsoftware/KIES'),
                        ('/si/support/usefulsoftware/KIESAIR/JSP', 'http://www.samsung.com/si/support/usefulsoftware/KIES'),
                        ('/si/support/usefulsoftware/supportUsefulSwMain.do', 'http://www.samsung.com/si/support/'),
                        ('/si/support/usefulsoftware/supportUsefulSwMobile.do', 'http://www.samsung.com/si/support/category/mobile/mobiledevice/smartphone/'),
                        ('/si/support/usefulsoftware/supportUsefulSwNotebook.do', 'http://www.samsung.com/si/support/category/pcperipheralsprinter/notebooknetbook/'),
                        ('/si/support/usefulsoftware/supportUsefulSwPrinter.do', 'http://www.samsung.com/si/support/category/pcperipheralsprinter/printer/'),
                        ('/si/support/usefulsoftware/SWUP/JSP', 'http://www.samsung.com/si/support/usefulsoftware/FOTA'),
                        ('/si/samsung-apps/*.do*', 'http://content.samsung.com/si/main.do'),]
        self.verify_redirection(redirections)

            
class TestF_CS_1029729(basetest.BaseTest):
    """
    checking the content targeting with querystring cid
    """
    
    def test_content_targeting(self):
        redirections = [('/gearcircle/?cid=499', '/sec/gearcircle/?cid=499'),
                        ('/gearcircle/', '/sec/gearcircle/'),]
        self.verify_redirection(redirections, {'X-Forward-For': '23.15.13.10'}) #call from KR

        
class TestF_CS_1033640(basetest.BaseTest):
    """
    redirection for business/index.htm
    """
    
    def test_redirection(self):
        countries = ['ph', 'sg', 'at', 'be', 'be_fr', 'bg', 'ch_fr', 'ch', 'cz', 'de', 'dk', 'ee', 'es', 'fi', 'fr', \
                      'gr', 'hr', 'hu', 'it', 'lt', 'lv', 'nl', 'no', 'pl', 'pt', 'ro', 'rs', 'se', 'sk', 'cn', 'hk', 'tw', 'hk_en', 'ie', 'iran', 'si']
        redirections = [('/%s/business/index.htm' % x, '/%s/business/' % x) for x in countries]
        self.verify_redirection(redirections)

            
class TestF_CS_1034542(basetest.BaseTest):
    """
    remove a redirection
    """
    
    def test_remove_redirection(self):
        remove_redirections = [('/bg/smartswitch', '/bg/support/smartswitch'),
                               ('/bg/smartswitch/', '/bg/support/smartswitch'),]
        for source, dest in remove_redirections:
            url = settings.BASE_URL + source
            settings.verbose_print('requesting %s...' % url) 
            res = requests.get(url, headers=settings.HEADERS, allow_redirects=False)
            if res.status_code in [301,302]:
                settings.verbose_print('%d - %s' % (res.status_code, res.headers['Location']))
                self.assertNotEqual(res.headers['Location'], dest, 'Redirection is not removed for %s' % source)
            else:
                settings.verbose_print('%d - %s' % (res.status_code, res.url))

class TestF_CS_1045250(basetest.BaseTest):
    """
    contents targeting for /ces2015
    """
    
    def test_content_targeting(self):
        base_url = '/ces2015'
        self.verify_samsung_com_content_targeting(base_url)
        
class TestF_CS_1045245(basetest.BaseTest):
    """
    contents targeting for /citizenship
    """
    
    def test_content_targeting(self):
        base_url = '/citizenship'
        self.verify_samsung_com_content_targeting(base_url)
        
class TestF_CS_1046952(basetest.BaseTest):
    """
    cache is no-store for the given URL /geonews
    """

    def test_nostore(self):
        url = '/geonews'
        self.verify_cache(url, 'no-store')
    
    def test_nostore2(self):
        self.verify_cache('/geonews/', 'no-store')

class TestF_CS_1047074(basetest.BaseTest):
    """
    remove redirection for /za/promotion/ces2015 => /za/offers/ces2015
    """
    
    def test_remove_redirection(self):
        remove_redirections = [('/za/promotions/ces2015', '/za/offer/ces2015')]
        self.verify_remove_redirection(remove_redirections)

class TestF_CS_1047848(basetest.BaseTest):
    """
    remove redirection for /rs/smartswitch
    """
    
    def test_remove_redirection(self):
        remove_redirections = [('/rs/smartswitch/', '/rs/support/smartswitch/')]
        self.verify_remove_redirection(remove_redirections)
        
class TestF_CS_1048647(basetest.BaseTest):
    """
    set TTL as 1h for /us/support/answer/*
    """
    
    def test_check_ttl(self):
        self.verify_cache('/us/support/answer/foo-bar', '1h')
        
class TestF_CS_1050658(basetest.BaseTest):
    """
    remove redirection for /hr/smartswitch
    """
    
    def test_remove_redirection(self):
        self.verify_remove_redirection([('/hr/smartswitch/', '/hr/support/smartswitch'),])
        
class TestF_CS_1052807(basetest.BaseTest):
    """
    update Redirections for /sec/ next generation.
    some are geo IP based, some are cookie based, some are mobile device,
    also m.samsung.com redirections
    """
    
    def test_updated_redirection(self):
        #geo IP is KR
        geo_header = {'X-Forwarded-For': self.settings.IP['KR']}
        self.verify_update_redirection([('/','/sec/', '/sec/home'),], headers=geo_header)
        self.verify_remove_redirection([('/hospitality','/sec/hospitality'),], headers=geo_header)
        self.verify_remove_redirection([('/hospitality/','/sec/hospitality'),], headers=geo_header)
        
        #in mobile device
        mobile_header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG-SM-G900A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.6 Chrome/28.0.1500.94 Mobile Safari/537.36'}
        self.verify_update_redirection([('/sec/index.html','http://m.samsung.com/sec/', 'http://www.samsung.com/sec/home'),], headers=mobile_header)
        
        #cookie 'site_cd' == 'sec'
        self.verify_update_redirection([('/', '/sec/', '/sec/home'),], cookies={'site_cd': 'sec'})
        
    def test_new_redirections(self):
        redirections = [('/sec', 'http://www.samsung.com/sec/home'),
                        ('/sec/', 'http://www.samsung.com/sec/home'),
                        ('/sec/index.html', 'http://www.samsung.com/sec/home'),
                        ('/sec/business', 'http://www.samsung.com/sec/business/home'),
                        ('/sec/business/', 'http://www.samsung.com/sec/business/home'),
                        ('/sec/business/index.html', 'http://www.samsung.com/sec/business/home'),
                        ('/sec/function/ipredirection/ipredirectionLocalList.do', 'http://www.samsung.com/sec/function/ipredirection/ipredirectionLocalList.html'),
                        ('/sec/consumer/foo/bar/index.idx?pagetype=type', '/sec/consumer/foo/bar/'),
                        ('/sec/consumer/foo/bar/productcompare?q=abc', '/sec/consumer/comparison?q=abc'),
                        ('/sec/consumer/foo/bar/topic/*', '/sec/consumer/foo/bar'),
                        ('/sec/function/espsearch/searchResult_mobile_p3.do?keywords=abc', '/sec/search/?q=abc'),
                        ('/sec/function/search/espsearchResult?input_keyword=abc&keywords=param', '/sec/search/?q=param'),
                        ('/sec/function/search/espsearchResult?input_keyword=abc&keywords=param&b2b=y', '/sec/business/search/?q=param'),
                        ('/sec/support/search/totalsearch?keywords=abc&input_keyword=param', '/sec/search/?q=param'),
                        ('/sec/info/contactus', 'http://www.samsung.com/sec/info/contactus.html'),
                        ('/sec/promotions', 'http://local.sec.samsung.com/comLocal/event/promotion/eventList.do'),
                        ('/sec/promotions/', 'http://local.sec.samsung.com/comLocal/event/promotion/eventList.do'),
                        ('/sec/promotions/index.html', 'http://local.sec.samsung.com/comLocal/event/promotion/eventList.do'),
                        ('/sec/support/detail/supportPrdDetail.do?q=abc', 'http://www.samsung.com/sec/support/'),
                        ('/sec/support/download/foo-bar.do?q=abc', 'http://www.samsung.com/sec/support/'),
                        ('/sec/support/downloads', 'http://www.samsung.com/sec/support/'),
                        ('/sec/support/firmware/foo-bar.do?q=abc', 'http://www.samsung.com/sec/support/'),
                        ('/sec/support/howtoguide/foo-bar.do?q=abc', 'http://www.samsung.com/sec/support/'),
                        ('/sec/support/location/foo-bar.do?q=abc', 'http://local.sec.samsung.com/comLocal/sec/dps/centerMain.do'),
                        ('/sec/support/main/supportMain.do', 'http://www.samsung.com/sec/support/'),
                        ('/sec/support/mobilesoftwaremanual/kiesTutorial.do', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=kies'),
                        ('/sec/support/mobilesoftwaremanual/mobilesoftwaremanual.do*', 'http://www.samsung.com/sec/support/'),
                        ('/sec/support/newsalert/supportNewsAlertMain.do', 'http://www.samsung.com/sec/support/newsalert'),
                        ('/sec/support/retail/foo-bar.do?q=abc', 'http://local.sec.samsung.com/comLocal/sec/dps/shopMain.do'),
                        ('/sec/support/supportMain.do', 'http://www.samsung.com/sec/support/'),
                        ('/sec/support/troubleshootingguides/foo-bar.do?q=abc', 'http://www.samsung.com/sec/support/'),
                        ('/sec/support/usefulsoftware/ASPS/JSP', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=kies'),
                        ('/sec/support/usefulsoftware/FOTA/JSP', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=fota'),
                        ('/sec/support/usefulsoftware/KIES/JSP', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=kies'),
                        ('/sec/support/usefulsoftware/KIESAIR/JSP', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=kies'),
                        ('/sec/support/usefulsoftware/supportUsefulSwMain.do', 'http://www.samsung.com/sec/support/'),
                        ('/sec/support/usefulsoftware/supportUsefulSwMobile.do', 'http://www.samsung.com/sec/support/category/mobile/mobiledevice/smartphone/'),
                        ('/sec/support/usefulsoftware/supportUsefulSwNotebook.do', 'http://www.samsung.com/sec/support/category/pcperipheralsprinter/notebooknetbook/'),
                        ('/sec/support/usefulsoftware/supportUsefulSwPrinter.do', 'http://www.samsung.com/sec/support/category/pcperipheralsprinter/printer/'),
                        ('/sec/support/usefulsoftware/SWUP/JSP', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=fota'),
                        ('/sec/support/warranty/warrantyInformation.do?page=POLICY.WARRANTY', 'http://www.samsung.com/sec/support/warranty/'),
                        ('/sec/samsung-apps/foo-bar.do?q=abc', 'http://www.samsung.com/sec/apps/mobile/'),
                        ('/sec/consumer/foo/bar/index.idx?pagetype=type_p2?q=abc', '/sec/consumer/foo/bar/'),
                        ('/sec/function/espsearch/searchResult_mobile_all_p3.do?menu=abc&keywords=param', '/sec/search/?q=param'),
                        ('/sec/consumer/accessories/', 'http://www.samsung.com/sec/home'),
                        ('/sec/support/pcApplication/UPGRADE/', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=upgrade'),
                        ('/sec/support/pcApplication/sidesync/', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=sidesync'),
                        ('/sec/support/pcApplication/smartswitch/', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=smartswitch'),
                        ('/sec/support/pcApplication/CONTENTVIEWER', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=contentviewer'),
                        ('/sec/support/pcApplication/PMP/', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=pmp'),
                        ('/sec/support/pcApplication/FOTA/', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=fota'),
                        ('/sec/support/pcApplication/USB/', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=usb'),
                        ('/sec/support/location/supportServiceLocation.do?page=SERVICE.LOCATION', 'http://local.sec.samsung.com/comLocal/sec/dps/centerMain.do'),
                        ('/sec/support/location/supportServiceLocation.do?page=SHOP.LOCATION', 'http://local.sec.samsung.com/comLocal/sec/dps/shopMain.do'),
                        ('/sec/support/download/supportDownloadMain.do', 'http://www.samsung.com/sec/support/'),
                        ('/sec/shopping_guide/index.do', 'http://local.sec.samsung.com/comLocal/ssg/Main/mainShop.do'),
                        ('/sec/socialmedia', 'http://local.sec.samsung.com/comLocal/socialmedia.do'),
                        ('/sec/friendslike/index.do', 'http://store.samsung.com/sec/ng/friendsstore'),
                        ('/sec/support/innovation.do', 'http://local.sec.samsung.com/comLocal/innovation.main.land'),
                        ('/sec/promotion/eventAllList.do', 'http://local.sec.samsung.com/comLocal/event/promotion/eventList.do'),
                        ('/sec/mypage/regProduct.do', 'http://local.sec.samsung.com/comLocal/mypage/myProducts.do'),
                        ('/sec/SmartAcademy/index.html', 'http://store.samsung.com/sec/ng/smartAcademy'),
                        ('/sec/SmartAcademy', 'http://store.samsung.com/sec/ng/smartAcademy'),
                        ('/sec/smartstudio/', 'http://local.sec.samsung.com/comLocal/smartstudio/main.jsp'),
                        ]
        self.verify_redirection(redirections)
        
        
class TestF_CS_1064600(basetest.BaseTest):
    """
    set TTL as 4h for /us/support/search/espsearch.us* and /us/support/search/supportAutoComplete*
    """
    
    def test_check_ttl(self):
        self.verify_cache('/us/support/search/espsearch.us?q=abc', '4h')
        self.verify_cache('/us/support/search/supportAutoComplete?q=abc', '4h')
        
class TestF_CS_1067363(basetest.BaseTest):
    """
    remove redirection /za/promotions -> /za/offers
    """
    
    def test_remove_redirection(self):
        self.verify_remove_redirection([('/za/promotions/foo-bar/', '/za/offers/foo-bar/')])
        
class TestF_CS_1067364(basetest.BaseTest):
    """
    set redirection for /sec/support/guarantee.do
    """
    
    def test_redirection(self):
        self.verify_redirection([('/sec/support/guarantee.do', 'http://local.sec.samsung.com/comLocal/service/support/internationalGuarantee.do')])
        
class TestF_CS_1071824(basetest.BaseTest):
    """
    /us makes redirection loop hole, so we set /us => /us/
    """
    
    def test_redirection(self):
        self.verify_redirection([('/us', 'http://www.samsung.com/us/')])
        
class TestF_CS_1072200(basetest.BaseTest):
    """
    b2b global 4 subdirectories redirection test.
    """
    
    def test_compresser_redirection(self):
        redirections = [('/global/business/compressor/compressor/recipro-compressor', '/global/business/compressor/recipro-compressor'),
                        ('/global/business/compressor/compressor/rotary-compressor', '/global/business/compressor/rotary-compressor'),
                        ('/global/business/compressor/compressor/scroll-compressor', '/global/business/compressor/scroll-compressor'),
                        ('/global/business/compressor/compressor/recipro-compressor/', '/global/business/compressor/recipro-compressor'),
                        ('/global/business/compressor/compressor/rotary-compressor/', '/global/business/compressor/rotary-compressor'),
                        ('/global/business/compressor/compressor/scroll-compressor/', '/global/business/compressor/scroll-compressor'),
                        ('/global/business/compressor/compressor/recipro-compressor/foo?subsubtype=bar', '/global/business/compressor/recipro-compressor/bar/foo'),
                        ('/global/business/compressor/compressor/rotary-compressor/foobar?subsubtype=bar2', '/global/business/compressor/rotary-compressor/bar2/foobar'),
                        ('/global/business/compressor/compressor/scroll-compressor/foo-bar?subsubtype=bar3', '/global/business/compressor/scroll-compressor/bar3/foo-bar'),
                        ('/global/function/search/espsearchResult_global?input_keyword=king&keywords=queen&b2b=CPS', '/global/business/gsearch/?q=queen&b2b=CPS'),
                        ('/global/function/search/espsearchResult_global?input_keyword=king&keywords=&b2b=CPS', '/global/business/gsearch/?q=king&b2b=CPS'),
                        ]
        self.verify_redirection(redirections)
        
    def test_fiberobtics_redirection(self):
        redirections = [('/global/business/fiberoptics/optical-fiber/single-mode', '/global/business/fiberoptics/single-mode'),
                        ('/global/business/fiberoptics/optical-cable/application', '/global/business/fiberoptics/application'),
                        ('/global/business/fiberoptics/optical-fiber/single-mode/foo-bar?subsubtype=quiche', '/global/business/fiberoptics/single-mode/quiche/foo-bar'),
                        ('/global/business/fiberoptics/optical-cable/application/foobar?subsubtype=briand', '/global/business/fiberoptics/application/briand/foobar'),
                        ('/global/business/fiberoptics/solution', '/global/business/fiberoptics/fiberoptics-solutions'),
                        ('/global/business/fiberoptics/solution/skilled', '/global/business/fiberoptics/fiberoptics-solutions/skilled'),
                        ('/global/business/fiberoptics/resource/spanked', '/global/business/fiberoptics/insights/spanked'),
                        ('/global/business/fiberoptics/resource', '/global/business/fiberoptics/insights/'),
                        ('/global/function/search/espsearchResult_global?input_keyword=*&keywords=*&b2b=FOB', '/global/business/gsearch/?q=*&b2b=FOB'),
                        ]
        self.verify_redirection(redirections)
        
    def test_networks_redirection(self):
        redirections = [('/global/business/networks/product/lte', '/global/business/networks/lte'),
                        ('/global/business/networks/product/multi-standard', '/global/business/networks/multi-standard'),
                        ('/global/business/networks/product/wcdma', '/global/business/networks/wcdma'),
                        ('/global/business/networks/product/gsm', '/global/business/networks/gsm'),
                        ('/global/business/networks/product/cdma', '/global/business/networks/cdma'),
                        ('/global/business/networks/product/wimax', '/global/business/networks/wimax'),
                        ('/global/business/networks/product/core-network', '/global/business/networks/core-network'),
                        ('/global/business/networks/product/services', '/global/business/networks/services'),
                        ('/global/business/networks/product/lte/', '/global/business/networks/lte'),
                        ('/global/business/networks/product/multi-standard/', '/global/business/networks/multi-standard'),
                        ('/global/business/networks/product/wcdma/', '/global/business/networks/wcdma'),
                        ('/global/business/networks/product/gsm/', '/global/business/networks/gsm'),
                        ('/global/business/networks/product/cdma/', '/global/business/networks/cdma'),
                        ('/global/business/networks/product/wimax/', '/global/business/networks/wimax'),
                        ('/global/business/networks/product/core-network/', '/global/business/networks/core-network'),
                        ('/global/business/networks/product/services/', '/global/business/networks/services'),
                        ('/global/business/networks/product/lte/jingle', '/global/business/networks/lte/lte/jingle'),
                        ('/global/business/networks/product/multi-standard/vi-test', '/global/business/networks/multi-standard/multi-standard/vi-test'),
                        ('/global/business/networks/product/wcdma/quiche', '/global/business/networks/wcdma/wcdma/quiche'),
                        ('/global/business/networks/product/gsm/wonder', '/global/business/networks/gsm/gsm/wonder'),
                        ('/global/business/networks/product/cdma/webble', '/global/business/networks/cdma/cdma/webble'),
                        ('/global/business/networks/product/wimax/fire-ball', '/global/business/networks/wimax/wimax/fire-ball'),
                        ('/global/business/networks/product/core-network/seven-seas', '/global/business/networks/core-network/core-network/seven-seas'),
                        ('/global/business/networks/product/services/cant', '/global/business/networks/services/services/cant'),
                        ('/global/business/networks/resource/knock-off-yours', '/global/business/networks/insights/knock-off-yours'),
                        ('/global/business/networks/resource', '/global/business/networks/insights/'),
                        ('/global/business/networks/resource/', '/global/business/networks/insights/'),
                        ('/global/business/networks/news/great-newsie', '/global/business/networks/insights/'),
                        ('/global/function/search/espsearchResult_global?input_keyword=king&keywords=queen&b2b=TCS', '/global/business/gsearch/?q=queen&b2b=NWS'),
                        ('/global/function/search/espsearchResult_global?input_keyword=king&keywords=&b2b=TCS', '/global/business/gsearch/?q=king&b2b=NWS'),
                        ]
        self.verify_redirection(redirections)
        
    def test_settopbox_redirection(self):
        redirections = [('/global/business/set-top-box/resource/clinic', '/global/business/set-top-box/insights/clinic'),
                        ('/global/business/set-top-box/resource', '/global/business/set-top-box/insights/'),
                        ('/global/function/search/espsearchResult_global?input_keyword=king&keywords=queen&b2b=STB', '/global/business/gsearch/?q=queen&b2b=STB'),]
        self.verify_redirection(redirections)
        
class TestF_CS_1081599(basetest.BaseTest):
    """
    /sec/ Korea next generation redirections (some additional redirections from existing ones)
    """
    def test_redirections(self):
        redirections = [('/sec/consumer/accessories', 'http://www.samsung.com/sec/home'), 
                        ('/sec/support/pcApplication/UPGRADE', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=upgrade'), 
                        ('/sec/support/pcApplication/sidesync', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=sidesync'), 
                        ('/sec/support/pcApplication/smartswitch', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=smartswitch'), 
                        ('/sec/support/pcApplication/CONTENTVIEWER/', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=contentviewer'), 
                        ('/sec/support/pcApplication/PMP', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=pmp'), 
                        ('/sec/support/pcApplication/FOTA', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=fota'), 
                        ('/sec/support/pcApplication/USB', 'http://local.sec.samsung.com/comLocal/support/down/kies_main.do?kind=usb'), 
                        ('/sec/smartstudio', 'http://local.sec.samsung.com/comLocal/smartstudio/main.jsp'), 
                        ('/sec/SmartAcademy/', 'http://store.samsung.com/sec/ng/smartAcademy'), 
                        ('/sec/socialmedia/', 'http://local.sec.samsung.com/comLocal/socialmedia.do'), 
                        ('/sec/aboutsamsung/information/philosophy/principle.html', 'http://www.samsung.com/sec/aboutsamsung/movie/companymovie.html'), 
                        ('/sec/article/display-brandstory', 'http://www.samsung.com/sec/consumer/it/display/'), 
                        ('/sec/article/display-brandstory/', 'http://www.samsung.com/sec/consumer/it/display/'), 
                        ('/sec/galaxys4zoom/', 'http://www.samsung.com/sec/home'),
                        ('/sec/galaxys4zoom', 'http://www.samsung.com/sec/home'), ]
        self.verify_redirection(redirections)

        
if __name__ == "__main__":
    unittest.main()
