'''
Created on Dec 18, 2014

@author: yju
'''
import unittest
import settings
import requests
import copy

class BaseTest(unittest.TestCase):
    """
    this is a base class for the unit testing.
    this will include some routine methods which can be used in the child class. 
    """
    
    def setUp(self):
        """
        print the case name and description for each test case running.
        """
        case_id = self.__class__.__name__.replace('Test','').replace('_','-')
        print '\n%s - %s' % (case_id, self.__doc__[1:-1].replace('\t',''), )
        self.settings = settings # TODO: this must be given by runner later.
        
    def verify_redirection(self, redirections, headers={}, cookies={}):
        """
        verifies whether input redirections are working fine.
        <redirections> are list of pairs, such as [('src','dest'),] url.
        """
        header = self.settings.HEADERS
        if headers:
            header = copy.deepcopy(self.settings.HEADERS)
            header.update(headers)
        for source, dest in redirections:
            url = self.settings.BASE_URL+source
            self.settings.verbose_print('requesting %s...' % url)
            res = requests.get(url, headers=header, allow_redirects=False, cookies=cookies)
            self.settings.verbose_print('%d - %s' % (res.status_code, res.headers['Location']))
            self.assertIn(res.status_code, [301, 302], 'Redirection Not returned')
            self.assertEqual(res.headers['Location'], dest, 'Redirection location is wrong:%s found, %s expected' % (res.headers['Location'], dest))
            
    def verify_remove_redirection(self, remove_redirections, headers={}, cookies={}):
        """
        verify whether given redirections are removed.
        remove_redirections must be a list of pairs such as [('src', 'dest'),] url
        """
        header = self.settings.HEADERS
        if headers:
            header = copy.deepcopy(self.settings.HEADERS)
            header.update(headers)
        for source, dest in remove_redirections:
            url = settings.BASE_URL + source
            settings.verbose_print('requesting %s...' % url) 
            res = requests.get(url, headers=header, allow_redirects=False, cookies=cookies)
            if res.status_code in [301,302]:
                settings.verbose_print('%d - %s' % (res.status_code, res.headers['Location']))
                self.assertNotEqual(res.headers['Location'], dest, 'Redirection is not removed for %s' % source)
            else:
                settings.verbose_print('%d - %s' % (res.status_code, res.url))
                
    def verify_update_redirection(self, updated_redirections, headers={}, cookies={}):
        """
        verify whether the given triples are correctly updated.
        updated_redirections are list of triples, such as [('src', 'old-dest', 'new-dest'),] 
        """
        for source, old_dest, new_dest in updated_redirections:
            self.verify_remove_redirection([(source, old_dest),], headers=headers, cookies=cookies)
            self.verify_redirection([(source, new_dest),], headers=headers, cookies=cookies)
                
    def verify_cache(self, source, ttl, cookies={}):
        """
        this will try verifying url TTL from edge server.
        since the X-Check-Caheable and cache-key TTL is not a definitive answer,
        this test will be only a peripheral test.
        """
        headers = self.settings.HEADERS
        if 'Pragma' not in headers.keys():
            headers = copy.deepcopy(self.settings.HEADERS)
            headers['Pragma'] = 'akamai-x-check-cacheable, akamai-x-get-cache-key'
        else:
            pragma = [x.strip() for x in headers['Pragma'].split(',')]
            required = ['akamai-x-check-cacheable', 'akamai-x-get-cache-key']
            intersection = list(set(required)-set(pragma))
            if len(intersection) != 0: # some header missing!
                headers = copy.deepcopy(self.settings.HEADERS)
                headers['Pragma'] = pragma + intersection
            
        if ttl == 'no-store':
            url = settings.BASE_URL + source
            settings.verbose_print('requesting %s...' % url) 
            res = requests.get(url, headers=headers, allow_redirects=False, cookies=cookies)
            settings.verbose_print('%d - %s' % (res.status_code, res.url))
            if res.status_code == 200:
                self.assertEqual(res.headers['X-Check-Cacheable'], 'NO', 'cache no-store expected but X-Check-Cacheable is not NO')
        else:
            url = settings.BASE_URL + source
            settings.verbose_print('requesting %s...' % url) 
            res = requests.get(url, headers=headers, allow_redirects=False, cookies=cookies)
            settings.verbose_print('%d - %s' % (res.status_code, res.url))
            cache_ttl = res.headers['X-Cache-Key'].split('/')[4]
            self.assertNotEqual(res.headers['X-Check-Cacheable'], 'NO', 'cacheable expected but X-Check-Cacheable is NO')
            self.assertEqual(cache_ttl, ttl, 'cache TTL %s expected but %s found' % (ttl, cache_ttl))
            
            
    def verify_samsung_com_content_targeting(self, base_url):
        """
        this is only for samsung.com content targeting test case. 
        since samsung.com has a fixed logic of content targeting, this only requires a base_url.
        first verify with the cookie attached.
        second, verify without cookie but with X-F-F header + Accept-Lang header.
        """
        
        #cookie <site_cd>
        cookie1 = ['ae_ar', 'ae', 'africa_en', 'africa_fr', 'africa_pt', 'ar', 'at', 'au', 'be_fr', 'be', 'bg', 
                   'br', 'ca_fr', 'ca', 'ch_fr', 'ch', 'cl', 'cn', 'co', 'cz', 'de', 'dk', 'ee', 'eg', 'es', 'fi', 
                   'fr', 'gr', 'hk_en', 'hk', 'hr', 'hu', 'id', 'ie', 'il', 'in', 'iran', 'it', 'jp', 'kz_ru', 'latin', 
                   'latin_en', 'levant', 'lt', 'lv', 'mx', 'my', 'n_africa', 'nl', 'no', 'nz', 'pe', 'ph', 'pk', 'pl', 
                   'pt', 'ro', 'rs', 'ru', 'sa', 'si', 'se', 'sec', 'sg', 'sk', 'th', 'tr', 'tw', 'ua_ru', 'ua', 'uk', 'us', 've', 'vn', 'za',]
        for cookie in cookie1:
            url = self.settings.BASE_URL+base_url
            dest = '/%s%s' % (cookie, base_url.lower())
            self.settings.verbose_print('requesting %s with cookie %s: %s...' % (url, 'site_cd', cookie))
            res = requests.get(url, headers=self.settings.HEADERS, cookies={'site_cd': cookie})
            self.settings.verbose_print('%d - %s' % (res.status_code, res.url))
            self.assertGreaterEqual(len(res.history), 1, 'Redirection Not returned')
            self.assertIn(dest, [x.headers['Location'] for x in res.history], 
                          'Redirection location is wrong:%s expected with cookie %s but %s found' % (dest, cookie, res.url)
                          )
        
        #TODO: this conditions are coming from metadata, but this may require to be updated from time to time. don't forget to make it better i.e. automate.
        conditions = [('MX', [(None, '/mx'+base_url),]),
                    ('US', [(None, '/us'+base_url),]),
                    ('CA', [('*fr*', '/ca_fr'+base_url), ('*en*', '/ca'+base_url), (None, '/ca'+base_url),]),
                    ('AR UY PY', [(None, '/ar'+base_url),]),
                    ('BR', [(None, '/br'+base_url),]),
                    ('CO', [(None, '/co'+base_url),]),
#                     ('CL BO', [(None, '/cl'+base_url),]), #this is original, but BO is now in latin too. so remove BO
                    ('CL', [(None, '/cl'+base_url),]),                    
                    ('PE', [(None, '/pe'+base_url),]),
                    ('BO CR EC SV GT HN NI PA DO CU', [(None, '/latin'+base_url),]),
#                     ('AN AW BB BM HT JM MQ TT MF KY AG SR AN BZ LC GY GP', [(None, '/latin_en'+base_url),]), #removing AN, seems it is not found in samsung.com and it is written twice!
                    ('AW BB BM HT JM MQ TT MF KY AG SR BZ LC GY GP', [(None, '/latin_en'+base_url),]),
                    ('AT', [(None, '/at'+base_url),]),
                    ('BE', [('*fr*', '/be_fr'+base_url), ('*nl*', '/be'+base_url), (None, '/be'+base_url),]),
                    ('NL', [(None, '/nl'+base_url),]),
                    ('CZ', [(None, '/cz'+base_url),]),
                    ('SK', [(None, '/sk'+base_url),]),
                    ('HU', [(None, '/hu'+base_url),]),
                    ('PL', [(None, '/pl'+base_url),]),
                    ('PT', [(None, '/pt'+base_url),]),
                    ('SE', [(None, '/se'+base_url),]),
                    ('FI', [(None, '/fi'+base_url),]),
                    ('NO', [(None, '/no'+base_url),]),
                    ('DK', [(None, '/dk'+base_url),]),
                    ('TR', [(None, '/tr'+base_url),]),
                    ('ES', [(None, '/es'+base_url),]),
                    ('IT MT', [(None, '/it'+base_url),]),
                    ('GB', [(None, '/uk'+base_url),]),
                    ('IE', [(None, '/ie'+base_url),]),
                    ('FR', [(None, '/fr'+base_url),]),
                    ('CH', [('*fr*', '/ch_fr'+base_url), ('*de*', '/ch'+base_url), (None, '/ch'+base_url),]),
                    ('GR', [(None, '/gr'+base_url),]),
                    ('CN', [(None, '/cn'+base_url),]),
                    ('JP', [(None, '/jp'+base_url),]),
                    ('HK', [('*en*', '/hk_en'+base_url), ('*zh*', '/hk'+base_url), (None, '/hk'+base_url),]),
                    ('TW', [(None, '/tw'+base_url),]),
                    ('KR', [(None, '/sec'+base_url),]),
                    ('AU', [(None, '/au'+base_url),]),
                    ('SG', [(None, '/sg'+base_url),]),
                    ('PH', [(None, '/ph'+base_url),]),
                    ('MY', [(None, '/my'+base_url),]),
#                     ('IN NP BD LK', [(None, '/in'+base_url),]), #removed NP BD LK, since it is set as global (global setup line is missing NP BD LK)
                    ('IN', [(None, '/in'+base_url),]),
                    ('ID', [(None, '/id'+base_url),]),
                    ('TH', [(None, '/th'+base_url),]),
                    ('VN', [(None, '/vn'+base_url),]),
                    ('NZ', [(None, '/nz'+base_url),]),
                    ('IR', [(None, '/iran'+base_url),]),
                    ('EE', [(None, '/ee'+base_url),]),
                    ('LV', [(None, '/lv'+base_url),]),
                    ('LT', [(None, '/lt'+base_url),]),
                    ('BG', [(None, '/bg'+base_url),]),
                    ('RS', [(None, '/rs'+base_url),]),
                    ('HR', [(None, '/hr'+base_url),]),
                    ('UA', [('*ru*', '/ua_ru'+base_url), ('*uk*', '/ua'+base_url), (None, '/ua'+base_url),]),
                    ('DE', [(None, '/de'+base_url),]),
                    ('RU', [(None, '/ru'+base_url),]),
                    ('IL', [(None, '/il'+base_url),]),
                    ('KZ', [(None, '/kz_ru'+base_url),]),
                    ('RO', [(None, '/ro'+base_url),]),
                    ('SI', [(None, '/si'+base_url),]),
                    ('VE', [(None, '/ve'+base_url),]),
                    ('PS IQ LB SY JO', [(None, '/levant'+base_url),]),
                    ('CI MR', [(None, '/africa_fr'+base_url),]),
                    ('GW CV', [(None, '/africa_pt'+base_url),]),
                    ('SA LY SD', [(None, '/sa'+base_url),]),
                    ('EG ER SO', [(None, '/eg'+base_url),]),
                    ('PK AF', [(None, '/pk'+base_url),]),
                    ('AE KW OM QA BH YE', [('*en*', '/ae'+base_url), ('*ar*', '/ae_ar'+base_url), (None, '/ae'+base_url),]),
                    ('ZA ZM ZW SZ NA MW BW', [(None, '/za'+base_url),]),
                    ('KE NG ET GH UG TZ GM LR SL', [(None, '/africa_en'+base_url),]),
                    ('AO MZ', [(None, '/africa_pt'+base_url),]),
                    ('MA DZ TN', [(None, '/n_africa'+base_url),]),
                    ('SN CD CM CI TG TD RW ML BJ NE DJ GA CG BI BF KM CF GN RE MU MG YT SC', [(None, '/africa_fr'+base_url),]), 
                    ('LU', [(None, '/be_fr'+base_url),])
                    ]
        for countries, condition in conditions:
            for country in countries.split(' '):
                header = {'X-Forwarded-For': settings.IP[country]}
                for lang, dest in condition:
                    if lang:
                        header.update({'Accept-Language': lang})
                    elif 'Accept-Language' in header.keys():
                        header.pop('Accept-Language')
                    url = self.settings.BASE_URL+base_url
                    self.settings.verbose_print('requesting %s from %s...' % (url, country) )
                    res = requests.get(url, headers=dict(self.settings.HEADERS.items() + header.items()) )
                    self.settings.verbose_print('%d - %s' % (res.status_code, res.url))
                    self.assertGreaterEqual(len(res.history), 1, 'Redirection Not returned')
                    self.assertIn(dest.lower(), [x.headers['Location'] for x in res.history], 
                                  'Redirection location is wrong:%s expected with cookie %s but %s found' % (dest.lower(), cookie, res.url)
                                  )
