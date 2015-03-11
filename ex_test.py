# encoding: utf-8
'''
Created on Dec 10, 2014

@author: yju
'''
import basetest
import unittest
import requests
import settings
import random
import string
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
        self.verify_update_redirection([('/','/sec/', '/sec/home/'),], headers=geo_header)
        self.verify_remove_redirection([('/hospitality','/sec/hospitality'),], headers=geo_header)
        self.verify_remove_redirection([('/hospitality/','/sec/hospitality'),], headers=geo_header)
        
        #in mobile device
        mobile_header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG-SM-G900A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.6 Chrome/28.0.1500.94 Mobile Safari/537.36'}
        self.verify_update_redirection([('/sec/index.html','http://m.samsung.com/sec/', 'http://www.samsung.com/sec/home/'),], headers=mobile_header)
        
        #cookie 'site_cd' == 'sec'
        self.verify_update_redirection([('/', '/sec/', '/sec/home/'),], cookies={'site_cd': 'sec'})
        
    def test_new_redirections(self):
        redirections = [('/sec', 'http://www.samsung.com/sec/home/'),
                        ('/sec/', 'http://www.samsung.com/sec/home/'),
                        ('/sec/index.html', 'http://www.samsung.com/sec/home/'),
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
                        ('/sec/consumer/accessories/', 'http://www.samsung.com/sec/home/'),
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
        redirections = [('/sec/consumer/accessories', 'http://www.samsung.com/sec/home/'), 
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
                        ('/sec/galaxys4zoom/', 'http://www.samsung.com/sec/home/'),
                        ('/sec/galaxys4zoom', 'http://www.samsung.com/sec/home/'), ]
        self.verify_redirection(redirections)

class TestF_CS_1083968(basetest.BaseTest):
    """
    partial removal of /galaxy from content targeting.
    only US, CA, CA_FR, PL, TH will be still using content targeting for /galaxy
    """
    
    def test_galaxy_removal(self):
        self.partial_removal_of_content_targeting('/galaxy')
        self.partial_removal_of_content_targeting('/galaxy/')
        self.partial_removal_of_content_targeting('/gaLaXy/')
        self.partial_removal_of_content_targeting('/Galaxy')
        
    def test_possible_marginal_cases(self):
        self.verify_redirection([('/galaxy/?cid=100&ask=tom', '/global/galaxy/?cid=100&ask=tom'),
                                 ('/galaxy?q=200', '/global/galaxy/?q=200')
                                 ], {'X-Forwarded-For': self.settings.IP['FR']})
        self.verify_redirection([('/galaxy/?cid=100&ask=tom', '/global/galaxy/?cid=100&ask=tom'),
                                 ('/galaxy?q=200', '/global/galaxy/?q=200')
                                 ], {'X-Forwarded-For': self.settings.IP['US']})
        
    
    def partial_removal_of_content_targeting(self, base_url):
        #test with site_cd cookie.
        cookie1 = ['ae_ar', 'ae', 'africa_en', 'africa_fr', 'africa_pt', 'ar', 'at', 'au', 'be_fr', 'be', 'bg', 
                   'br', 'ch_fr', 'ch', 'cl', 'cn', 'co', 'cz', 'de', 'dk', 'ee', 'eg', 'es', 'fi', 
                   'fr', 'gr', 'hk_en', 'hk', 'hr', 'hu', 'id', 'ie', 'il', 'in', 'iran', 'it', 'jp', 'kz_ru', 'latin', 
                   'latin_en', 'levant', 'lt', 'lv', 'mx', 'my', 'n_africa', 'nl', 'no', 'nz', 'pe', 'ph', 'pk',  
                   'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sec', 'sg', 'sk', 'tr', 'tw', 'ua_ru', 'ua', 'uk', 've', 'vn', 'za',]
        for cookie in cookie1:
            url = self.settings.BASE_URL+base_url
            dest = '/global/galaxy/'
            self.settings.verbose_print('requesting %s with cookie %s: %s...' % (url, 'site_cd', cookie))
            res = requests.get(url, headers=self.settings.HEADERS, allow_redirects=False, cookies={'site_cd': cookie})
            self.settings.verbose_print('%d - %s' % (res.status_code, res.headers['Location']))
            self.assertIn(res.status_code, [301, 302], 'Redirection Not returned')
            self.assertEqual(res.headers['Location'], dest, 
                             'Redirection location is wrong:%s expected with cookie %s but %s found' % (dest, cookie, res.headers['Location'])
                             )
        #most of countries now go to /global/galaxy with the querystring attached.
        countries = ['MX', 'AR', 'UY', 'PY', 'BR', 'CO', 'CL', 'PE', 'BO', 'CR', 'EC', 'SV', 'GT', 'HN', 'NI', 'PA', 'DO', 'CU', 
                     'AW', 'BB', 'BM', 'HT', 'JM', 'MQ', 'TT', 'MF', 'KY', 'AG', 'SR', 'BZ', 'LC', 'GY', 'GP', 'AT', 'BE', 'NL', 
                     'CZ', 'SK', 'HU', 'PT', 'SE', 'FI', 'NO', 'DK', 'TR', 'ES', 'IT', 'GB', 'IE', 'FR', 'CH', 'GR', 'CN', 'JP', 
                     'HK', 'TW', 'KR', 'AU', 'SG', 'PH', 'MY', 'IN', 'ID', 'VN', 'NZ', 'IR', 'EE', 'LV', 'LT', 'BG', 'RS', 'HR', 
                     'UA', 'DE', 'RU', 'IL', 'KZ', 'RO', 'VE', 'PS', 'IQ', 'LB', 'SY', 'JO', 'CI', 'MR', 'GW', 'CV', 'SA', 'LY', 
                     'SD', 'EG', 'ER', 'SO', 'PK', 'AF', 'AE', 'KW', 'OM', 'QA', 'BH', 'YE', 'ZA', 'ZM', 'ZW', 'SZ', 'NA', 'MW', 
                     'BW', 'KE', 'NG', 'ET', 'GH', 'UG', 'TZ', 'GM', 'LR', 'SL', 'AO', 'MZ', 'MA', 'DZ', 'TN', 'SN', 'CD', 'CM', 
                     'CI', 'TG', 'TD', 'RW', 'ML', 'BJ', 'NE', 'DJ', 'GA', 'CG', 'BI', 'BF', 'KM', 'CF', 'GN', 'RE', 'MU', 'MG', 'YT', 'SC',
                     'US', 'CA', 'PL', 'TH']
        for country in countries:
            add_query = bool(random.getrandbits(1))
            qstring = ''
            if add_query:
                key = ''.join(random.choice(string.ascii_letters) for i in range(5))
                value = ''.join(random.choice(string.ascii_letters) for i in range(5))
                qstring = '?%s=%s' % (key, value)
            url = self.settings.BASE_URL+base_url+qstring
            dest = '/global/galaxy/'+qstring
            self.settings.verbose_print('requesting %s from %s...' % (url, country))
            res = requests.get(url, headers=dict(self.settings.HEADERS.items() + {'X-Forwarded-For': self.settings.IP[country]}.items()), allow_redirects=False,)
            self.settings.verbose_print('%d - %s' % (res.status_code, res.headers['Location']))
            self.assertIn(res.status_code, [301, 302], 'Redirection Not returned')
            self.assertEqual(res.headers['Location'], dest, 
                             'Redirection location is wrong:%s expected with country %s but found %s' % (dest, country, res.headers['Location'],) 
                             )
        
                    
class TestF_CS_1084157(basetest.BaseTest):
    """
    removing the cookie <PreferBandwith> - which is only set when IE7.0 in /uk and under.
    """
    
    def test_remove_cookie(self):
        # we test /uk with no IE, /uk with IE, non /uk with IE and no IE
        # all of them will return no PreferBandwidth cookie
        targets = [('/uk/home', 'MSIE 7.0'), ('/uk/home', 'MSIE 8.0'), ('/uk/home', 'Mozilla/5.0'),
                   ('/sec/home/', 'MSIE 7.0'), ('/sec/home/', 'MSIE 8.0'), ('/sec/home/', 'Mozilla/5.0'),]
        for path, agent in targets:
            url = self.settings.BASE_URL + path
            self.settings.verbose_print('requesting %s with %s' %(url, agent,))
            res = requests.get(url, headers=dict(self.settings.HEADERS.items() + [('X-Forwarded-For',agent)]),)
            self.assertNotIn('PreferBandwidth', res.cookies.keys(),
                              'Cookie PreferBandwidth is not removed in %s with %s' % (url, agent))

class TestF_CS_1081042(basetest.BaseTest):
    """
    set no-cache on /us/support/email/product, /us/support/email/product/foo-bar
    """
    
    def test_check_ttl(self):
        self.verify_cache('/us/support/email/product', 'no-store')
        self.verify_cache('/us/support/email/product/foo-bar', 'no-store')
        
class TestF_CS_1090976(basetest.BaseTest):
    """
    redirection as 
    www.samsung.com/printer/recycle 
    www.samsung.com/printer/star 
    -> https://support-prc.samsung.com/star_b2b/pages/home.aspx 
    """
        
    def test_redirection_check(self):
        redirections = [('/printer/recycle', 'https://support-prc.samsung.com/star_b2b/pages/home.aspx'),
                        ('/printer/star', 'https://support-prc.samsung.com/star_b2b/pages/home.aspx'),
                        ('/printer/recycle/', 'https://support-prc.samsung.com/star_b2b/pages/home.aspx'),
                        ('/printer/star/', 'https://support-prc.samsung.com/star_b2b/pages/home.aspx'),]
        self.verify_redirection(redirections)
        no_redirection = [('/printer/recycle/foo-bar', 'https://support-prc.samsung.com/star_b2b/pages/home.aspx'),
                          ('/printer/star/amber', 'https://support-prc.samsung.com/star_b2b/pages/home.aspx')
                          ]
        self.verify_remove_redirection(no_redirection)

class TestF_CS_1092321(basetest.BaseTest):
    """
    we change existing redirections to /sec/home to /sec/home/.
    this will reduce one redirection for each client, and it will reduce one request to origin.
    """
    
    def test_redirection_sec_home(self):
        updated_redirections = [('/sec', 'http://www.samsung.com/sec/home', 'http://www.samsung.com/sec/home/',),
                                ('/sec/', 'http://www.samsung.com/sec/home', 'http://www.samsung.com/sec/home/',),
                                ('/sec/index.html', 'http://www.samsung.com/sec/home', 'http://www.samsung.com/sec/home/',),
                                ('/sec/consumer/accessories/', 'http://www.samsung.com/sec/home', 'http://www.samsung.com/sec/home/',),
                                ('/sec/consumer/accessories', 'http://www.samsung.com/sec/home', 'http://www.samsung.com/sec/home/',),
                                ('/sec/galaxys4zoom/', 'http://www.samsung.com/sec/home', 'http://www.samsung.com/sec/home/',),
                                ('/sec/galaxys4zoom', 'http://www.samsung.com/sec/home', 'http://www.samsung.com/sec/home/',),]
        self.verify_update_redirection(updated_redirections)
    
    def test_redirection_with_cookie(self):
        self.verify_redirection([('/', '/sec/home/')], cookies={'site_cd': 'sec'})
        
    def test_redirection_with_geoip(self):
        redirections = [('/', '/sec/home/')]
        self.verify_redirection(redirections, headers={'X-Forwarded-For': self.settings.IP['KR']})
    
    def test_redirection_with_mobile(self):
        redirections = [('/sec/index.html', 'http://www.samsung.com/sec/home/')]
        self.verify_redirection(redirections, headers={'User-Agent': self.settings.UA_STRING['iPhone']})
        
class TestF_CS_1096351(basetest.BaseTest):
    """
    cache no-store for /us/support/myAccountServiceStatus.do
    """
    
    def test_no_cache(self):
        self.verify_cache('/us/support/myAccountServiceStatus.do', 'no-store')
        
class TestF_CS_1098631(basetest.BaseTest):
    """
    contents targeting for /suhdtv, /galaxys6, /galaxys6edge
    """
    
    def test_content_targeting(self):
        self.verify_samsung_com_content_targeting('/suhdtv')
        self.verify_samsung_com_content_targeting('/galaxys6')
        self.verify_samsung_com_content_targeting('/galaxys6edge')
        self.verify_samsung_com_content_targeting('/suhdtv/')
        self.verify_samsung_com_content_targeting('/galaxys6/')
        self.verify_samsung_com_content_targeting('/galaxys6edge/')
        
class TestF_CS_1103785(basetest.BaseTest):
    """
    adding verification of case-insensitiveness and new content targeting
    "/unpack2015episode1"
    """
    
    def test_content_targeting(self):
        self.verify_samsung_com_content_targeting('/SuhdTV')
        self.verify_samsung_com_content_targeting('/GalaxyS6')
        self.verify_samsung_com_content_targeting('/galaxys6EDGE')
        self.verify_samsung_com_content_targeting('/sUHDtv/')
        self.verify_samsung_com_content_targeting('/GALAXYs6/')
        self.verify_samsung_com_content_targeting('/galaxyS6edge/')
#         self.verify_samsung_com_content_targeting('/unpack2015episode1')
#         self.verify_samsung_com_content_targeting('/Unpack2015episode1')
#         self.verify_samsung_com_content_targeting('/uNpack2015episode1/')
        
class TestF_CS_1106136(basetest.BaseTest):
    """
    changing the /unpack2015episode1 to /unpacked2015episode1.
    """
    
    def test_content_targeting(self):
        self.verify_samsung_com_content_targeting('/unpacked2015episode1')
        self.verify_samsung_com_content_targeting('/Unpacked2015episode1')
        self.verify_samsung_com_content_targeting('/uNpacked2015episode1/')
        
    def test_content_targeting2(self):
        self.verify_samsung_com_content_targeting('/unpacked2015')
        self.verify_samsung_com_content_targeting('/Unpacked2015')
        self.verify_samsung_com_content_targeting('/uNpacked2015/')
        
class TestF_CS_1107795(basetest.BaseTest):
    """
    redirection test for /{site_cd}/promotion/galaxy 
    to /{site_cd}/promotions/galaxy
    """
    
    def test_redirection_on_all_site_cd(self):
        site_cds = ['ae_ar', 'ae', 'africa_en', 'africa_fr', 'africa_pt', 'ar', 'at', 'au', 'be_fr', 'be', 'bg', 
                   'br', 'ca_fr', 'ca', 'ch_fr', 'ch', 'cl', 'cn', 'co', 'cz', 'de', 'dk', 'ee', 'eg', 'es', 'fi', 
                   'fr', 'gr', 'hk_en', 'hk', 'hr', 'hu', 'id', 'ie', 'il', 'in', 'iran', 'it', 'jp', 'kz_ru', 'latin', 
                   'latin_en', 'levant', 'lt', 'lv', 'mx', 'my', 'n_africa', 'nl', 'no', 'nz', 'pe', 'ph', 'pk', 'pl', 
                   'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sec', 'sg', 'sk', 'th', 'tr', 'tw', 'ua_ru', 'ua', 'uk',
                   'us', 've', 'vn', 'za',]
        redirections = [('/%s/promotion/galaxy' % x, 'http://www.samsung.com/%s/promotions/galaxy/' % x) for x in site_cds]
        redirections_with_slash = [('/%s/promotion/galaxy/' % x, 'http://www.samsung.com/%s/promotions/galaxy/' % x) for x in site_cds]
        self.verify_redirection(redirections)
        self.verify_redirection(redirections_with_slash)
        
class TestF_CS_1110489(basetest.BaseTest):
    """
    redirection on /sec/consumer/it/display/signageTV (case insensitive)
    """
    
    def test_redirections(self):
        org = 'signagetv'
        redirections = []
        for i in range(512):
            case = '{0:09b}'.format(i)
            result = ''
            for j in range(9):
                result += (org[j] if case[j]== '0' else org[j].upper())
            redirections.append(('/sec/consumer/it/display/%s' % result, '/sec/consumer/it/display/signagetv/'))
            if i != 0:
                redirections.append(('/sec/consumer/it/display/%s/' % result, '/sec/consumer/it/display/signagetv/'))
#         redirections = [('/sec/consumer/it/display/signageTV/', '/sec/consumer/it/display/signagetv/'),
#                         ('/sec/consumer/it/display/SignAgeTV', '/sec/consumer/it/display/signagetv/'),
#                         ('/sec/consumer/it/display/signagetv', '/sec/consumer/it/display/signagetv/'),
#                         ('/sec/consumer/it/display/signAgetv/', '/sec/consumer/it/display/signagetv/'),]
        self.verify_redirection(redirections)

class TestF_CS_1116980(basetest.BaseTest):
    """
    new redirection sets for 36 countries. + no-store setup for B2B section.
    """
    
    def test_b2bredirections(self):
        site_cds = ['ca_fr', 'ca', 'mx', 'br', 'latin', 'latin_en', 've', 'co', 
                   'ar', 'cl', 'pe', 'au', 'nz', 'id', 'th', 'vn', 'my', 'ru', 'ua', 
                   'ua_ru', 'kz_ru', 'in', 'ae', 'ae_ar', 'il', 'sa', 'sa_en', 'tr', 
                   'levant', 'pk', 'eg', 'n_africa', 'africa_en', 'africa_fr', 
                   'africa_pt', 'za',]
        for site_cd in site_cds:
            redirections = [('/%s/business' % site_cd, 'http://www.samsung.com/%s/business/home' % site_cd),
                            ('/%s/business/' % site_cd, 'http://www.samsung.com/%s/business/home' % site_cd),
                            ('/%s/business/index.html' % site_cd, 'http://www.samsung.com/%s/business/home' % site_cd),
                            ('/%s/business/home' % site_cd, 'http://www.samsung.com/%s/business/' % site_cd),
                            ('/%s/business/home/' % site_cd, 'http://www.samsung.com/%s/business/' % site_cd),
                            ('/%s/business/index.html' % site_cd, 'http://www.samsung.com/%s/business/' % site_cd),
                            ('/%s/business/resource/foo-bar' % site_cd, 'http://www.samsung.com/%s/business/insights/foo-bar' % site_cd),
                            ('/%s/business/resource' % site_cd, 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/index.html' % site_cd, 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/bli-report' % site_cd, 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/solution-brief' % site_cd, 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/article' % site_cd, 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/installation-guide' % site_cd, 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/bli-report/' % site_cd, 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/solution-brief/' % site_cd, 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/article/' % site_cd, 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/installation-guide/' % site_cd, 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/support' % site_cd.upper(), 'http://www.samsung.com/%s/business/support/' % site_cd),
                            ('/%s/business/insights' % site_cd.upper(), 'http://www.samsung.com/%s/business/insights/' % site_cd),
                            ('/%s/business/step' % site_cd.upper(), 'http://www.samsung.com/%s/business/step/' % site_cd),
                            ('/%s/business/ebc' % site_cd.upper(), 'http://www.samsung.com/%s/business/ebc/' % site_cd),
                            ('/%s/business/countrysite' % site_cd.upper(), 'http://www.samsung.com/%s/business/countrysite/' % site_cd),
                            ('/%s/business/support/foo-bar' % site_cd.upper(), 'http://www.samsung.com/%s/business/support/foo-bar' % site_cd),
                            ('/%s/business/insights/foo-bar' % site_cd.upper(), 'http://www.samsung.com/%s/business/insights/foo-bar' % site_cd),
                            ('/%s/business/step/foo-bar' % site_cd.upper(), 'http://www.samsung.com/%s/business/step/foo-bar' % site_cd),
                            ('/%s/business/ebc/foo-bar' % site_cd.upper(), 'http://www.samsung.com/%s/business/ebc/foo-bar' % site_cd),
                            ('/%s/business/countrysite/foo-bar' % site_cd.upper(), 'http://www.samsung.com/%s/business/countrysite/foo-bar' % site_cd),]
            self.verify_redirection(redirections)
        
    def test_remove_cache(self):
        site_cds = ['ae_ar', 'ae', 'africa_en', 'africa_fr', 'africa_pt', 'ar', 'at', 'au', 'be_fr', 'be', 'bg', 
                   'br', 'ca_fr', 'ca', 'ch_fr', 'ch', 'cl', 'cn', 'co', 'cz', 'de', 'dk', 'ee', 'eg', 'es', 'fi', 
                   'fr', 'gr', 'hk_en', 'hk', 'hr', 'hu', 'id', 'ie', 'il', 'in', 'iran', 'it', 'jp', 'kz_ru', 'latin', 
                   'latin_en', 'levant', 'lt', 'lv', 'mx', 'my', 'n_africa', 'nl', 'no', 'nz', 'pe', 'ph', 'pk', 'pl', 
                   'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sec', 'sg', 'sk', 'th', 'tr', 'tw', 'ua_ru', 'ua', 'uk',
                   'us', 've', 'vn', 'za',]
        urls = ['/%s/business/my-business/cust-userloging',
                '/%s/business/my-business/recentlyInsights',
                '/%s/business/my-business/myProfile',
                '/%s/data-business/mybusiness/recently-product',
                '/%s/data-business/mybusiness/recently-solution',
                '/%s/data-business/mybusiness/recently-insights',
                '/%s/data-business/mybusiness/clipped-insights',
                '/%s/data-business/mybusiness/clipped-insights-delete',
                '/%s/business/my-business/save-myprofile',
                '/%s/business/my-business/checkB2BUser',
                '/%s/business/my-business/edit-myprofile',
                '/%s/business/my-business/deleteProfile',
                '/%s/business/my-business/partnerportal/sso',
                '/%s/business/my-business/partnerportal/ssotest',
                '/%s/business/my-business/partnerportal/checkticket',]
        test_urls = [x % y for x in urls for y in site_cds]
        
        for test_url in test_urls:
            self.verify_cache(test_url, 'no-store')
        

if __name__ == "__main__":
    unittest.main()
