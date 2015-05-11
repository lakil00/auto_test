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
        self.verify_redirection(redirections, headers={'X-Forwarded-For': '23.15.13.10'}) #call from KR

        
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
            redirections = [
                            ('/%s/business/home' % site_cd, '/%s/business/' % site_cd),
                            ('/%s/business/home/' % site_cd, '/%s/business/' % site_cd),
                            ('/%s/business/index.html' % site_cd, '/%s/business/' % site_cd),
                            ('/%s/business/resource/foo-bar' % site_cd, '/%s/business/insights/foo-bar' % site_cd),
                            ('/%s/business/resource' % site_cd, '/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/index.html' % site_cd, '/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/bli-report' % site_cd, '/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/solution-brief' % site_cd, '/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/article' % site_cd, '/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/installation-guide' % site_cd, '/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/bli-report/' % site_cd, '/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/solution-brief/' % site_cd, '/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/article/' % site_cd, '/%s/business/insights/' % site_cd),
                            ('/%s/business/resource/installation-guide/' % site_cd, '/%s/business/insights/' % site_cd),
                            ('/%s/business/support' % site_cd.upper(), '/%s/business/support/' % site_cd),
                            ('/%s/business/insights' % site_cd.upper(), '/%s/business/insights/' % site_cd),
                            ('/%s/business/step' % site_cd.upper(), '/%s/business/step/' % site_cd),
                            ('/%s/business/ebc' % site_cd.upper(), '/%s/business/ebc/' % site_cd),
                            ('/%s/business/countrysite' % site_cd.upper(), '/%s/business/countrysite/' % site_cd),
                            ('/%s/business/support/foo-bar' % site_cd.upper(), '/%s/business/support/foo-bar' % site_cd),
                            ('/%s/business/insights/foo-bar' % site_cd.upper(), '/%s/business/insights/foo-bar' % site_cd),
                            ('/%s/business/step/foo-bar' % site_cd.upper(), '/%s/business/step/foo-bar' % site_cd),
                            ('/%s/business/ebc/foo-bar' % site_cd.upper(), '/%s/business/ebc/foo-bar' % site_cd),
                            ('/%s/business/countrysite/foo-bar' % site_cd.upper(), '/%s/business/countrysite/foo-bar' % site_cd),]
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
            
class TestF_CS_1122047(basetest.BaseTest):
    """
    add country to content targeting
    SI (slovenia) => /si
    MT (Malta) => /it
    """
    
    def test_slovenia(self):
        self.verify_redirection([('/galaxys6', '/si/galaxys6')], {'X-Forwarded-For': settings.IP['SI']})
        
    def test_malta(self):
        self.verify_redirection([('/galaxys6', '/it/galaxys6')], {'X-Forwarded-For': settings.IP['MT']})
        

class TestF_CS_1129428(basetest.BaseTest):
    """
    add content targeting, /solvefortomorrow
    """
    def test_content(self):
        self.verify_samsung_com_content_targeting('/solvefortomorrow')
        self.verify_samsung_com_content_targeting('/Solvefortomorrow/')
        
class TestF_CS_1130670(basetest.BaseTest):
    """
    setup TTL 30 for /us/price/*
    """
    
    def test_cache_ttl(self):
        self.verify_cache('/us/price/samsungB2CEcomPrice.json', '30m')
        
class TestF_CS_1132136(basetest.BaseTest):
    """
    /global/galaxy* URL must redirected to  lower character if there is any upper case.
    """
    
    def test_lower_case(self):
        self.verify_redirection([('/global/Galaxy', 'http://www.samsung.com/global/galaxy'),
                                 ('/global/galaxy/GalaxyS6/', 'http://www.samsung.com/global/galaxy/galaxys6/')])
        
class TestF_CS_1137246(basetest.BaseTest):
    """
    /sec/business => /sec/business/home with redirection cid, redirectId
    """
    
    def test_redirections(self):
        origin = ['/sec/business','/sec/business/']
        querystring = [('cid=100&redirectionId=abc','redirectionId=abc&cid=100'), ('cid=100','cid=100'), 
                       ('redirectionId=abc','redirectionId=abc')]
        redirections = [('%s?%s' % (x,y[0]), '%s?%s' % ('http://www.samsung.com/sec/business/home',y[1])) for x in origin for y in querystring]
        
        self.verify_redirection(redirections)
        
class TestF_CS_1137446(basetest.BaseTest):
    """
    /global/business/mobile/ should be redirected to local pages;
    based on cookie site_cd, or country code + accept lang.
    """
    def test_site_cd(self):
        dests = [('ie', '/ie/business/business-products/mobile-devices/',), 
                ('uk', '/uk/business/business-products/mobile-devices/',), 
                ('sg', '/sg/business/business-products/mobile-device/',), 
                ('ph', '/ph/business/business-products/mobile-devices/',), 
                ('it', '/it/business/business-products/mobile-devices/',), 
                ('es', '/es/business/business-products/mobile-devices/',), 
                ('hu', '/hu/business/business-products/mobile-devices/',), 
                ('de', '/de/business/business-products/mobile-devices/',), 
                ('se', '/se/business/business-products/mobile-devices/',), 
                ('dk', '/dk/business/business-products/mobile-devices/',), 
                ('fi', '/fi/business/business-products/mobile-devices/',), 
                ('no', '/no/business/business-products/mobile-devices/',), 
                ('fr', '/fr/business/business-products/mobile-devices/',), 
                ('pt', '/pt/business/business-products/mobile-devices/',), 
                ('pl', '/pl/business/business-products/mobile-devices/',), 
                ('gr', '/gr/business/',), 
                ('cz', '/cz/business/business-products/mobile-devices/',), 
                ('sk', '/sk/business/business-products/mobile-devices/',), 
                ('ro', '/ro/business/business-products/mobile-phones/',), 
                ('bg', '/bg/business/',), 
                ('at', '/at/business/business-products/mobile-devices/',), 
                ('ch', '/ch/business/business-products/mobile-devices/',), 
                ('ch_fr', '/ch_fr/business/business-products/mobile-devices/',), 
                ('be', '/be/business/business-products/mobile-devices/',), 
                ('be_fr', '/be_fr/business/business-products/mobile-devices/',), 
                ('nl', '/nl/business/business-products/mobile-devices/',), 
                ('lv', '/lv/business/',), 
                ('lt', '/lt/business/',), 
                ('ee', '/ee/business/',), 
                ('rs', '/rs/business/business-products/mobile-devices/',), 
                ('hr', '/hr/business/business-products/mobile-devices/',), 
                ('si', '/si/business/',), 
                ('iran', '/iran/business/',), 
                ('ca_fr', '/ca_fr/business/business-products/mobile-devices/',), 
                ('ca', '/ca/business/business-products/mobile-devices/',), 
                ('mx', '/mx/business/business-products/mobile-devices/',), 
                ('br', '/br/business/',), 
                ('latin', '/latin/business/business-products/mobile-devices/',), 
                ('latin_en', '/latin_en/business/business-products/mobile-devices/',), 
                ('ve', '/ve/business/business-products/mobile-devices/',), 
                ('co', '/co/business/business-products/mobile-devices/',), 
                ('ar', '/ar/business/business-products/mobile-devices/',), 
                ('cl', '/cl/business/business-products/mobile-devices/',), 
                ('pe', '/pe/business/business-products/mobile-devices/',), 
                ('au', '/au/business/business-products/mobile-devices/',), 
                ('nz', '/nz/business/business-products/mobile-devices/',), 
                ('id', '/id/business/business-products/mobile-devices/',), 
                ('th', '/th/business/business-products/mobile-devices/',), 
                ('vn', '/vn/business/business-products/mobile-devices/',), 
                ('my', '/my/business/business-products/mobile-device/',), 
                ('ru', '/ru/business/business-products/mobile-devices/',), 
                ('ua', '/ua/business/business-products/mobile-devices/',), 
                ('ua_ru', '/ua_ru/business/business-products/mobile-devices/',), 
                ('kz_ru', '/kz_ru/business/business-products/mobile-devices/',), 
                ('in', '/in/business/business-products/mobile-devices/',), 
                ('ae', '/ae/business/business-products/mobile-devices/',), 
                ('ae_ar', '/ae_ar/business/business-products/mobile-devices/',), 
                ('il', '/il/business/business-products/mobile-device/',), 
                ('sa', '/sa/business/business-products/mobile-phones/',), 
                ('sa_en', '/sa_en/business/business-products/mobile-phones/',), 
                ('tr', '/tr/business/business-products/mobile-devices/',), 
                ('levant', '/levant/business/',), 
                ('pk', '/pk/business/business-products/mobile-devices/',), 
                ('eg', '/eg/business/',), 
                ('n_africa', '/n_africa/business/business-products/mobile-devices/',), 
                ('africa_en', '/africa_en/business/business-products/mobile-devices/',), 
                ('africa_fr', '/africa_fr/business/business-products/mobile-devices/',), 
                ('africa_pt', '/africa_pt/business/business-products/mobile-devices/',), 
                ('za', '/za/business/business-products/mobile-devices/',), 
                ('sec', '/sec/business/',), 
                ('us', '/us/business/',), ]
        
        for site_cd, dest in dests:
            self.verify_redirection([('/global/business/mobile', dest),
                                     ('/global/business/mobile/', dest),
                                     ('/global/business/mobile/test-url', dest)], cookies={'site_cd': site_cd})
            
    def test_geoip(self):
        src1 = '/global/business/mobile'
        src2 = src1 + '/'
        dests = [('ie', '/ie/business/business-products/mobile-devices/',), 
                ('gb', '/uk/business/business-products/mobile-devices/',), 
                ('sg', '/sg/business/business-products/mobile-device/',), 
                ('ph', '/ph/business/business-products/mobile-devices/',), 
                ('it', '/it/business/business-products/mobile-devices/',), 
                ('es', '/es/business/business-products/mobile-devices/',), 
                ('hu', '/hu/business/business-products/mobile-devices/',), 
                ('de', '/de/business/business-products/mobile-devices/',), 
                ('se', '/se/business/business-products/mobile-devices/',), 
                ('dk', '/dk/business/business-products/mobile-devices/',), 
                ('fi', '/fi/business/business-products/mobile-devices/',), 
                ('no', '/no/business/business-products/mobile-devices/',), 
                ('fr', '/fr/business/business-products/mobile-devices/',), 
                ('pt', '/pt/business/business-products/mobile-devices/',), 
                ('pl', '/pl/business/business-products/mobile-devices/',), 
                ('gr', '/gr/business/',), 
                ('cz', '/cz/business/business-products/mobile-devices/',), 
                ('sk', '/sk/business/business-products/mobile-devices/',), 
                ('ro', '/ro/business/business-products/mobile-phones/',), 
                ('bg', '/bg/business/',), 
                ('at', '/at/business/business-products/mobile-devices/',), 
                ('ch', '/ch/business/business-products/mobile-devices/',), 
                ('be', '/be/business/business-products/mobile-devices/',), 
                ('nl', '/nl/business/business-products/mobile-devices/',), 
                ('lv', '/lv/business/',), 
                ('lt', '/lt/business/',), 
                ('ee', '/ee/business/',), 
                ('rs', '/rs/business/business-products/mobile-devices/',), 
                ('hr', '/hr/business/business-products/mobile-devices/',), 
                ('si', '/si/business/',), 
                ('ca', '/ca/business/business-products/mobile-devices/',), 
                ('mx', '/mx/business/business-products/mobile-devices/',), 
                ('br', '/br/business/',), 
                ('ve', '/ve/business/business-products/mobile-devices/',), 
                ('co', '/co/business/business-products/mobile-devices/',), 
                ('ar', '/ar/business/business-products/mobile-devices/',), 
                ('cl', '/cl/business/business-products/mobile-devices/',), 
                ('pe', '/pe/business/business-products/mobile-devices/',), 
                ('au', '/au/business/business-products/mobile-devices/',), 
                ('nz', '/nz/business/business-products/mobile-devices/',), 
                ('id', '/id/business/business-products/mobile-devices/',), 
                ('th', '/th/business/business-products/mobile-devices/',), 
                ('vn', '/vn/business/business-products/mobile-devices/',), 
                ('my', '/my/business/business-products/mobile-device/',), 
                ('ru', '/ru/business/business-products/mobile-devices/',), 
                ('ua', '/ua/business/business-products/mobile-devices/',),  
                ('in', '/in/business/business-products/mobile-devices/',), 
                ('ae', '/ae/business/business-products/mobile-devices/',), 
                ('il', '/il/business/business-products/mobile-device/',), 
                ('sa', '/sa/business/business-products/mobile-phones/',), 
                ('tr', '/tr/business/business-products/mobile-devices/',), 
                ('pk', '/pk/business/business-products/mobile-devices/',), 
                ('eg', '/eg/business/',),  
                ('za', '/za/business/business-products/mobile-devices/',), 
                ('kr', '/sec/business/',), 
                ('us', '/us/business/',), 
                ('ir', '/iran/business/',),]
        
        for site_cd, dest in dests:
            if site_cd.upper() in settings.IP.keys():
                self.verify_redirection([(src1, dest), (src2, dest)],
                                        headers = {"X-Forwarded-For": settings.IP[site_cd.upper()]})
        # 'ch_fr', 'be_fr', 'ca_fr'
        dests = [('BE', '/be_fr/business/business-products/mobile-devices/'),
                ('CH', '/ch_fr/business/business-products/mobile-devices/'),
                ('CA', '/ca_fr/business/business-products/mobile-devices/')]
        for country, dest in dests:
            self.verify_redirection([(src1, dest), (src2, dest)], 
                                    headers={"X-Forwarded-For": settings.IP[country], "Accept-Language": "fr-FR"})
            
        # 'latin', 
        countries = 'BO CR EC SV GT HN NI PA DO CU'.split(' ')
        dest = '/latin/business/business-products/mobile-devices/'
        for country in countries:
            self.verify_redirection([(src1, dest), (src2, dest), (src1+'/test-url', dest)], 
                                    headers={"X-Forwarded-For": settings.IP[country]})
        'latin_en'
        countries = 'AW BB BM HT JM MQ TT MF KY AG SR BZ LC GY GP'.split(' ')
        dest_en = '/latin_en/business/business-products/mobile-devices/' 
        for country in countries:
            self.verify_redirection([(src1, dest_en), (src2, dest_en)], 
                                    headers={"X-Forwarded-For": settings.IP[country]})

        # 'ua_ru', 'kz_ru' 
        dests = [('UA', '/ua_ru/business/business-products/mobile-devices/'),
                ('KZ', '/kz_ru/business/business-products/mobile-devices/')]
        for country, dest in dests:
            self.verify_redirection([(src1, dest), (src2, dest)], 
                                    headers={"X-Forwarded-For": settings.IP[country], "Accept-Language": "ru-RS"})
        
        # ('ae_ar', 
        dest = '/ae_ar/business/business-products/mobile-devices/'
        self.verify_redirection([(src1, dest), (src2, dest)], 
                                    headers={"X-Forwarded-For": settings.IP['AE'], "Accept-Language": "ar_AR"}) 

        # 'sa_en'
        dest = '/sa_en/business/business-products/mobile-phones/'
        self.verify_redirection([(src1, dest), (src2, dest)], 
                                    headers={"X-Forwarded-For": settings.IP['SA'], "Accept-Language": "en_US"})         

        # 'levant', 
        dest = '/levant/business/'
        countries = 'PS IQ LB SY JO'.split(' ')
        for country in countries:
            self.verify_redirection([(src1, dest), (src2, dest)], 
                                    headers={"X-Forwarded-For": settings.IP[country]})
            
        'n_africa'
        countries = 'MA DZ TN'.split(' ')
        dest = '/n_africa/business/business-products/mobile-devices/'
        for country in countries:
            self.verify_redirection([(src1, dest), (src2, dest)], 
                                    headers={"X-Forwarded-For": settings.IP[country]})
        'africa_en'
        countries = 'KE NG ET GH UG TZ GM LR SL'.split(' ')
        dest = '/africa_en/business/business-products/mobile-devices/'
        for country in countries:
            self.verify_redirection([(src1, dest), (src2, dest)], 
                                    headers={"X-Forwarded-For": settings.IP[country]})
        
        # 'africa_fr'
        countries = 'CI MR SN CD CM CI TG TD RW ML BJ NE DJ GA CG BI BF KM CF GN RE MU MG YT SC'.split(' ')
        dest = '/africa_fr/business/business-products/mobile-devices/'
        for country in countries:
            self.verify_redirection([(src1, dest), (src2, dest)], 
                                    headers={"X-Forwarded-For": settings.IP[country]})
        
        # 'africa_pt'
        countries = 'AO MZ GW CV'.split(' ')
        dest = '/africa_pt/business/business-products/mobile-devices/'
        for country in countries:
            self.verify_redirection([(src1, dest), (src2, dest)], 
                                    headers={"X-Forwarded-For": settings.IP[country]})


class TestF_CS_1142775(basetest.BaseTest):
    """
    Luxembourg users will be redirected to /be_fr/
    in / and content targetting
    """
    def test_luxembourg(self):
        self.verify_redirection([('/', '/be_fr/'),
                                 ('/solvefortomorrow', '/be_fr/solvefortomorrow')], 
                                headers={'X-Forwarded-For': settings.IP['LU']})
     
        
class TestF_CS_1141355(basetest.BaseTest):
    """
    maintain the querystring when redirect from /{site_cd} => /{site_cd}/home
    """
    
    def test_maintainquerystring(self):
        org_redirections = [
                            ('/ar','http://www.samsung.com/ar/home'),
                        ('/br','http://www.samsung.com/br/home'),
                        ('/ca','http://www.samsung.com/ca/home'),
                        ('/ca_fr','http://www.samsung.com/ca_fr/home'),
                        ('/cl','http://www.samsung.com/cl/home'),
                        ('/co','http://www.samsung.com/co/home'),
                        ('/latin','http://www.samsung.com/latin/home'),
                        ('/latin_en','http://www.samsung.com/latin_en/home'),
                        ('/mx','http://www.samsung.com/mx/home'),
                        ('/pe','http://www.samsung.com/pe/home'),
                        ('/ve','http://www.samsung.com/ve/home'),
                        ('/au','/au/home'),
                        ('/cn','http://www.samsung.com/cn/home'),
                        ('/hk','http://www.samsung.com/hk/home'),
                        ('/hk_en','http://www.samsung.com/hk_en/home'),
                        ('/id','http://www.samsung.com/id/home'),
                        ('/in','http://www.samsung.com/in/home'),
                        ('/jp','/jp/home'),
                        ('/my','http://www.samsung.com/my/home'),
                        ('/nz','/nz/home'),
                        ('/ph','http://www.samsung.com/ph/home'),
                        ('/sec','http://www.samsung.com/sec/home/'),
                        ('/sg','http://www.samsung.com/sg/home'),
                        ('/th','http://www.samsung.com/th/home'),
                        ('/tw','http://www.samsung.com/tw/home'),
                        ('/vn','http://www.samsung.com/vn/home'),
                        ('/ae','http://www.samsung.com/ae/home'),
                        ('/ae_ar','http://www.samsung.com/ae_ar/home'),
                        ('/africa_en','http://www.samsung.com/africa_en/home'),
                        ('/africa_fr','http://www.samsung.com/africa_fr/home'),
                        ('/africa_pt','http://www.samsung.com/africa_pt/home'),
                        ('/eg','http://www.samsung.com/eg/home'),
                        ('/il','http://www.samsung.com/il/home'),
                        ('/iran','http://www.samsung.com/iran/home'),
                        ('/kz_ru','http://www.samsung.com/kz_ru/home'),
                        ('/levant','http://www.samsung.com/levant/home'),
                        ('/n_africa','http://www.samsung.com/n_africa/home'),
                        ('/ru','http://www.samsung.com/ru/home'),
                        ('/sa','http://www.samsung.com/sa/home'),
                        ('/sa_en','http://www.samsung.com/sa_en/home'),
                        ('/ua','http://www.samsung.com/ua/home'),
                        ('/ua_ru','http://www.samsung.com/ua_ru/home'),
                        ('/za','http://www.samsung.com/za/home'),
                        ('/at','http://www.samsung.com/at/home'),
                        ('/be','http://www.samsung.com/be/home'),
                        ('/be_fr','http://www.samsung.com/be_fr/home'),
                        ('/bg','http://www.samsung.com/bg/home'),
                        ('/ch','http://www.samsung.com/ch/home'),
                        ('/ch_fr','http://www.samsung.com/ch_fr/home'),
                        ('/cz','http://www.samsung.com/cz/home'),
                        ('/de','/de/home'),
                        ('/dk','http://www.samsung.com/dk/home'),
                        ('/ee','http://www.samsung.com/ee/home'),
                        ('/es','/es/home'),
                        ('/fi','http://www.samsung.com/fi/home'),
                        ('/fr','/fr/home'),
                        ('/gr','http://www.samsung.com/gr/home'),
                        ('/hr','http://www.samsung.com/hr/home'),
                        ('/hu','http://www.samsung.com/hu/home'),
                        ('/ie','http://www.samsung.com/ie/home'),
                        ('/it','/it/home'),
                        ('/lt','http://www.samsung.com/lt/home'),
                        ('/lv','http://www.samsung.com/lv/home'),
                        ('/nl','http://www.samsung.com/nl/home'),
                        ('/no','http://www.samsung.com/no/home'),
                        ('/pk','http://www.samsung.com/pk/home'),
                        ('/pl','http://www.samsung.com/pl/home'),
                        ('/pt','http://www.samsung.com/pt/home'),
                        ('/ro','http://www.samsung.com/ro/home'),
                        ('/rs','http://www.samsung.com/rs/home'),
                        ('/se','http://www.samsung.com/se/home'),
                        ('/si','http://www.samsung.com/si/home'),
                        ('/sk','http://www.samsung.com/sk/home'),
                        ('/tr','http://www.samsung.com/tr/home'),
                        ('/uk','/uk/home'),]
        redirections = [(x[0]+'?cid=100',x[1]+'?cid=100') for x in org_redirections]
        self.verify_redirection(redirections)
        redirections = [(x[0]+'?redirectionId=91a0',x[1]+'?redirectionId=91a0') for x in org_redirections]
        self.verify_redirection(redirections)
        redirections = [(x[0]+'?cid=100&redirectionId=91a0',x[1]+'?cid=100&redirectionId=91a0') for x in org_redirections]
        self.verify_redirection(redirections)
        
class TestF_CS_1144762(basetest.BaseTest):
    """
    /global/business/enterprise-communication/* redirection
    """
    def test_redirection_ent_comm_cookie(self):
        base_url = '/global/business/enterprise-communications'
        site_cds= [('ie', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('uk', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('sg', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ph', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('it', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('es', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('hu', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('de', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('se', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('dk', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('fi', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('no', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('fr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('pt', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('pl', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('gr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('cz', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('sk', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ro', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('bg', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('at', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ch', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ch_fr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('be', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('be_fr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('nl', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('lv', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('lt', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ee', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('rs', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('hr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('si', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('iran', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ca_fr', 'http://www.samsung.com/us/business/business-communication-systems/wireless-enterprise-solutions/'),
                    ('ca', 'http://www.samsung.com/us/business/business-communication-systems/wireless-enterprise-solutions/'),
                    ('mx', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('br', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('latin', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('latin_en', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ve', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('co', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ar', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('cl', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('pe', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('au', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('nz', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('id', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('th', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('vn', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('my', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ru', 'http://www.samsung.com/ru/business/business-products/enterprise-communications/'),
                    ('ua', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ua_ru', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('kz_ru', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('in', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ae', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ae_ar', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('il', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('sa', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('sa_en', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('tr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('levant', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('pk', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('eg', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('n_africa', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('africa_en', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('africa_fr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('africa_pt', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('za', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('sec', '/sec/business/'),
                    ('us', '/us/business/'),]
        for site_cd, dest in site_cds:
            settings.verbose_print('site_cd %s' % site_cd)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], 
                                    cookies = {'site_cd': site_cd})
    
    def test_redirection_ent_comm_geo(self):
        base_url = '/global/business/enterprise-communications'
        countries = [('ie', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('gb', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('sg', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ph', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('it', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('es', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('hu', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('de', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('se', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('dk', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('fi', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('no', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('fr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('pt', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('pl', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('gr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('cz', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('sk', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ro', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('bg', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('at', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ch', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('be', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('nl', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('lv', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('lt', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ee', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('rs', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('hr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('SI', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('IR', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ca', 'http://www.samsung.com/us/business/business-communication-systems/wireless-enterprise-solutions/'),
                    ('mx', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('br', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ve', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('co', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ar', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('cl', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('pe', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('au', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('nz', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('id', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('th', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('vn', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('my', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ru', 'http://www.samsung.com/ru/business/business-products/enterprise-communications/'),
                    ('ua', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('kz', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('in', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('ae', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('il', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('sa', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('tr', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('pk', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('eg', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('za', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('kr', 'http://www.samsung.com/sec/business/'),
                    ('us', 'http://www.samsung.com/us/business/'),
                    ('CI', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('PS', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ('CR', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                    ]
        for country, dest in countries:
            settings.verbose_print('country %s' % country)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP[country.upper()]})
            
        
                # 'ch_fr', 'be_fr', 'ca_fr'
        dests = [('BE', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                ('CH', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                ('CA', 'http://www.samsung.com/us/business/business-communication-systems/wireless-enterprise-solutions/')]
        for country, dest in dests:
            settings.verbose_print('country %s' % country)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP[country.upper()], "Accept-Language": "fr-FR"})
            
        # 'latin', 
        countries = 'BO CR EC SV GT HN NI PA DO CU'.split(' ')
        dest = 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'
        for country in countries:
            settings.verbose_print('country %s' % country)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP[country.upper()],"X-Forwarded-For": settings.IP[country]})
        'latin_en'
        countries = 'AW BB BM HT JM MQ TT MF KY AG SR BZ LC GY GP'.split(' ')
        dest = 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/' 
        for country in countries:
            settings.verbose_print('country %s' % country)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP[country.upper()],})

        # 'ua_ru', 'kz_ru' 
        dests = [('UA', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'),
                ('KZ', 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/')]
        for country, dest in dests:
            settings.verbose_print('country %s' % country)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP[country.upper()], "Accept-Language": "ru-RS"})
        
        # ('ae_ar', 
        dest = 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'
        settings.verbose_print('country ae_ar')
        self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP['AE'],"Accept-Language": "ar_AR"}) 

        # 'sa_en'
        dest = 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'
        settings.verbose_print('country sa')
        self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP['SA'],"Accept-Language": "en_US"})         

        # 'levant', 
        dest = 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'
        countries = 'PS IQ LB SY JO'.split(' ')
        for country in countries:
            settings.verbose_print('country %s' % country)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP[country.upper()],})
            
        'n_africa'
        countries = 'MA DZ TN'.split(' ')
        dest = 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'
        for country in countries:
            settings.verbose_print('country %s' % country)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP[country.upper()],})
        'africa_en'
        countries = 'KE NG ET GH UG TZ GM LR SL'.split(' ')
        dest = 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'
        for country in countries:
            settings.verbose_print('country %s' % country)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP[country.upper()],})
        
        # 'africa_fr'
        countries = 'CI MR SN CD CM CI TG TD RW ML BJ NE DJ GA CG BI BF KM CF GN RE MU MG YT SC'.split(' ')
        dest = 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'
        for country in countries:
            settings.verbose_print('country %s' % country)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP[country.upper()],})
        
        # 'africa_pt'
        countries = 'AO MZ GW CV'.split(' ')
        dest = 'http://www.samsung.com/uk/business/business-products/wireless-enterprise/'
        for country in countries:
            settings.verbose_print('country %s' % country)
            self.verify_redirection([(base_url, dest),
                                     (base_url+'/test-url', dest),
                                     (base_url+'/test-url?abc=1000', dest)], headers={'X-Forwarded-For': settings.IP[country.upper()],})
                    
            
class TestF_CS_1147451(basetest.BaseTest):
    """
    /galaxy/foo-bar will go to /global/galaxy/foo-bar
    """
    
    def test_redirection(self):
        self.verify_redirection([('/galaxy/test-url', '/global/galaxy/test-url'),
                                 ('/Galaxy/Talbot/', '/global/galaxy/Talbot/'),
                                 ('/galaXy/foo-bar/?q=system', '/global/galaxy/foo-bar/?q=system'),
                                 ])
        
class TestF_CS_1153295(basetest.BaseTest):
    """
    redirection for /global/galaxy with upper case and querystrings handled.
    """
    
    def test_redirection(self):
        normal_redirections = [('/global/galaxy/galaxys6/galaxy-s6-edge/m_index.html','http://www.samsung.com/global/galaxy/galaxys6/galaxy-s6-edge/'),
                        ('/global/galaxy/galaxys6/galaxy-s6/m_index.html','http://www.samsung.com/global/galaxy/galaxys6/galaxy-s6/'),
                        ('/global/galaxy/galaxys6/m_index.html','http://www.samsung.com/global/galaxy/'),
                        ('/global/galaxy/galaxys6/wearables/m_index.html','http://www.samsung.com/global/galaxy/wearables/note4/'),
                        ('/global/galaxy/galaxys6/accessories/m_index.html','http://www.samsung.com/global/galaxy/galaxys6/accessories/'),
                        ('/global/galaxy/worldtour2015/m_index.html','http://www.samsung.com/global/galaxy/worldtour2015/'),
                        ('/global/galaxy/unpacked2015/m_index.html','http://www.samsung.com/global/galaxy/unpacked2015/'),
                        ('/global/galaxy/scarpet2015/m_index.html','http://www.samsung.com/global/galaxy/scarpet2015/'),]
#                         ('/global/galaxy/galaxy-story/m_index.html','http://www.samsung.com/global/galaxy/galaxystory/brandstory/'),]
        redirections = normal_redirections + [(x[0].upper(), x[1]) for x in normal_redirections] + [(x[0]+'?pid=100', x[1]+'?pid=100') for x in normal_redirections]
        self.verify_redirection(redirections)
        
class TestF_CS_1158754(basetest.BaseTest):
    """
    redirection for /global/galaxy/galaxystory/brandstory/ and others.
    also upper case and querystrings handled.
    """
    
    def test_redirections(self):
        normal_redirections = [('/global/galaxy/galaxystory/brandstory/', 'http://www.samsung.com/global/galaxy/galaxystory/brand-story/'),
                        ('/global/galaxy/galaxy-story/', 'http://www.samsung.com/global/galaxy/galaxystory/brand-story/'),
                        ('/global/galaxy/galaxy-story/m_index.html', 'http://www.samsung.com/global/galaxy/galaxystory/brand-story/'),
                        ('/global/galaxy/galaxys6/wearable/', 'http://www.samsung.com/global/galaxy/wearables/note4/'),
                        ('/global/galaxy/galaxys6/wearable/m_index.html', 'http://www.samsung.com/global/galaxy/wearables/note4/'),]
        redirections = normal_redirections + [(x[0].upper(), x[1]) for x in normal_redirections] + [(x[0]+'?pid=100', x[1]+'?pid=100') for x in normal_redirections]
        self.verify_redirection(redirections)
        
        
class TestF_CS_1180497(basetest.BaseTest):
    """
    /suhd content targeting.
    """
    
    def test_content_targeting(self):
        urls = ['/suhd', '/suhd/', '/SUHD', '/SUHD?abc=100', '/suhd/?abc=100']
        for url in urls:
            self.verify_samsung_com_content_targeting(url)
        
 
if __name__ == "__main__":
    unittest.main()
