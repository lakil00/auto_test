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
        
    def get(self, url, headers={}, cookies={}, allow_redirects=False):
        """
        run a GET with given url, headers, cookies.
        """
        url = self.settings.BASE_URL+url
        header = self.settings.HEADERS
        if headers:
            header = copy.deepcopy(self.settings.HEADERS)
            header.update(headers)
        self.settings.verbose_print('requesting %s...' % url)
        return requests.get(url, headers=header, allow_redirects=allow_redirects, cookies=cookies)
        
        
    def verify_redirection(self, redirections, headers={}, cookies={}):
        """
        verifies whether input redirections are working fine.
        <redirections> are list of pairs, such as [('src','dest'),] url.
        """
        for source, dest in redirections:
            res = self.get(source, headers=headers, cookies=cookies)
            self.settings.verbose_print('%d - %s' % (res.status_code, res.headers['Location']))
            self.assertIn(res.status_code, [301, 302], 'Redirection Not returned')
            self.assertEqual(res.headers['Location'], dest, 'Redirection location is wrong:%s found, %s expected' % (res.headers['Location'], dest))
            
    def verify_remove_redirection(self, remove_redirections, headers={}, cookies={}):
        """
        verify whether given redirections are removed.
        remove_redirections must be a list of pairs such as [('src', 'dest'),] url
        """
        for source, dest in remove_redirections: 
            res = self.get(source, headers=headers, cookies=cookies)
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
            
            
    def verify_samsung_com_content_targeting(self, base_url, dest_url=None):
        """
        this is only for samsung.com content targeting test case. 
        since samsung.com has a fixed logic of content targeting, this only requires a base_url.
        first verify with the cookie attached.
        second, verify without cookie but with X-F-F header + Accept-Lang header.
        """
        
        if not dest_url:
            dest_url = base_url.lower()
        
        #cookie <site_cd>
        cookie1 = ['ae_ar', 'ae', 'africa_en', 'africa_fr', 'africa_pt', 'ar', 'at', 'au', 'be_fr', 'be', 'bg', 
                   'br', 'ca_fr', 'ca', 'ch_fr', 'ch', 'cl', 'cn', 'co', 'cz', 'de', 'dk', 'ee', 'eg', 'es', 'fi', 
                   'fr', 'gr', 'hk_en', 'hk', 'hr', 'hu', 'id', 'ie', 'il', 'in', 'iran', 'it', 'jp', 'kz_ru', 'latin', 
                   'latin_en', 'levant', 'lt', 'lv', 'mx', 'my', 'n_africa', 'nl', 'no', 'nz', 'pe', 'ph', 'pk', 'pl', 
                   'pt', 'ro', 'rs', 'ru', 'sa', 'si', 'se', 'sec', 'sg', 'sk', 'th', 'tr', 'tw', 'ua_ru', 'ua', 'uk', 'us', 've', 'vn', 'za',]
        for cookie in cookie1:
            url = self.settings.BASE_URL+base_url
            dest = '/%s%s' % (cookie, dest_url)
            self.settings.verbose_print('requesting %s with cookie %s: %s...' % (url, 'site_cd', cookie))
            res = requests.get(url, headers=self.settings.HEADERS, cookies={'site_cd': cookie})
            self.settings.verbose_print('%d - %s' % (res.status_code, res.url))
            self.assertGreaterEqual(len(res.history), 1, 'Redirection Not returned')
            self.assertIn(dest, [x.headers['Location'] for x in res.history], 
                          'Redirection location is wrong:%s expected with cookie %s but %s found' % (dest, cookie, res.url)
                          )
        
        #TODO: this conditions are coming from metadata, but this may require to be updated from time to time. don't forget to make it better i.e. automate.
        conditions = [('MX', [(None, '/mx'+dest_url),]),
                    ('US', [(None, '/us'+dest_url),]),
                    ('CA', [('*fr*', '/ca_fr'+dest_url), ('*en*', '/ca'+dest_url), (None, '/ca'+dest_url),]),
                    ('AR UY PY', [(None, '/ar'+dest_url),]),
                    ('BR', [(None, '/br'+dest_url),]),
                    ('CO', [(None, '/co'+dest_url),]),
#                     ('CL BO', [(None, '/cl'+dest_url),]), #this is original, but BO is now in latin too. so remove BO
                    ('CL', [(None, '/cl'+dest_url),]),                    
                    ('PE', [(None, '/pe'+dest_url),]),
                    ('BO CR EC SV GT HN NI PA DO CU', [(None, '/latin'+dest_url),]),
#                     ('AN AW BB BM HT JM MQ TT MF KY AG SR AN BZ LC GY GP', [(None, '/latin_en'+dest_url),]), #removing AN, seems it is not found in samsung.com and it is written twice!
                    ('AW BB BM HT JM MQ TT MF KY AG SR BZ LC GY GP', [(None, '/latin_en'+dest_url),]),
                    ('AT', [(None, '/at'+dest_url),]),
                    ('BE', [('*fr*', '/be_fr'+dest_url), ('*nl*', '/be'+dest_url), (None, '/be'+dest_url),]),
                    ('NL', [(None, '/nl'+dest_url),]),
                    ('CZ', [(None, '/cz'+dest_url),]),
                    ('SK', [(None, '/sk'+dest_url),]),
                    ('HU', [(None, '/hu'+dest_url),]),
                    ('PL', [(None, '/pl'+dest_url),]),
                    ('PT', [(None, '/pt'+dest_url),]),
                    ('SE', [(None, '/se'+dest_url),]),
                    ('FI', [(None, '/fi'+dest_url),]),
                    ('NO', [(None, '/no'+dest_url),]),
                    ('DK', [(None, '/dk'+dest_url),]),
                    ('TR', [(None, '/tr'+dest_url),]),
                    ('ES', [(None, '/es'+dest_url),]),
                    ('IT MT', [(None, '/it'+dest_url),]),
                    ('GB', [(None, '/uk'+dest_url),]),
                    ('IE', [(None, '/ie'+dest_url),]),
                    ('FR', [(None, '/fr'+dest_url),]),
                    ('CH', [('*fr*', '/ch_fr'+dest_url), ('*de*', '/ch'+dest_url), (None, '/ch'+dest_url),]),
                    ('GR', [(None, '/gr'+dest_url),]),
                    ('CN', [(None, '/cn'+dest_url),]),
                    ('JP', [(None, '/jp'+dest_url),]),
                    ('HK', [('*en*', '/hk_en'+dest_url), ('*zh*', '/hk'+dest_url), (None, '/hk'+dest_url),]),
                    ('TW', [(None, '/tw'+dest_url),]),
                    ('KR', [(None, '/sec'+dest_url),]),
                    ('AU', [(None, '/au'+dest_url),]),
                    ('SG', [(None, '/sg'+dest_url),]),
                    ('PH', [(None, '/ph'+dest_url),]),
                    ('MY', [(None, '/my'+dest_url),]),
#                     ('IN NP BD LK', [(None, '/in'+dest_url),]), #removed NP BD LK, since it is set as global (global setup line is missing NP BD LK)
                    ('IN', [(None, '/in'+dest_url),]),
                    ('ID', [(None, '/id'+dest_url),]),
                    ('TH', [(None, '/th'+dest_url),]),
                    ('VN', [(None, '/vn'+dest_url),]),
                    ('NZ', [(None, '/nz'+dest_url),]),
                    ('IR', [(None, '/iran'+dest_url),]),
                    ('EE', [(None, '/ee'+dest_url),]),
                    ('LV', [(None, '/lv'+dest_url),]),
                    ('LT', [(None, '/lt'+dest_url),]),
                    ('BG', [(None, '/bg'+dest_url),]),
                    ('RS', [(None, '/rs'+dest_url),]),
                    ('HR', [(None, '/hr'+dest_url),]),
                    ('UA', [('*ru*', '/ua_ru'+dest_url), ('*uk*', '/ua'+dest_url), (None, '/ua'+dest_url),]),
                    ('DE', [(None, '/de'+dest_url),]),
                    ('RU', [(None, '/ru'+dest_url),]),
                    ('IL', [(None, '/il'+dest_url),]),
                    ('KZ', [(None, '/kz_ru'+dest_url),]),
                    ('RO', [(None, '/ro'+dest_url),]),
                    ('SI', [(None, '/si'+dest_url),]),
                    ('VE', [(None, '/ve'+dest_url),]),
                    ('PS IQ LB SY JO', [(None, '/levant'+dest_url),]),
                    ('CI MR', [(None, '/africa_fr'+dest_url),]),
                    ('GW CV', [(None, '/africa_pt'+dest_url),]),
                    ('SA LY SD', [(None, '/sa'+dest_url),]),
                    ('EG ER SO', [(None, '/eg'+dest_url),]),
                    ('PK AF', [(None, '/pk'+dest_url),]),
                    ('AE KW OM QA BH YE', [('*en*', '/ae'+dest_url), ('*ar*', '/ae_ar'+dest_url), (None, '/ae'+dest_url),]),
                    ('ZA ZM ZW SZ NA MW BW', [(None, '/za'+dest_url),]),
                    ('KE NG ET GH UG TZ GM LR SL', [(None, '/africa_en'+dest_url),]),
                    ('AO MZ', [(None, '/africa_pt'+dest_url),]),
                    ('MA DZ TN', [(None, '/n_africa'+dest_url),]),
                    ('SN CD CM CI TG TD RW ML BJ NE DJ GA CG BI BF KM CF GN RE MU MG YT SC', [(None, '/africa_fr'+dest_url),]), 
                    ('LU', [(None, '/be_fr'+dest_url),])
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
