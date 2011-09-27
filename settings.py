#Settings

#BASE_URL - URL of the SFX server:
BASE_URL = 'http://sfx.scholarsportal.info/brock'

#QUERY_STRING = Probably doesn't need to change
QUERY_STRING = '?url_ver=Z39.88-2004&url_ctx_fmt=infofi/fmt:kev:mtx:ctx&ctx_enc=info:ofi/enc:UTF-8&ctx_ver=Z39.88-2004&rfr_id=info:sid/sfxit.com:azlist&svc.fulltext=yes&sfx.ignore_date_threshold=1&sfx.response_type=simplexml&rft.object_id='

#Debug level
# 3 - Absolutely everything, you probably just want to pipe this into a log file
# 2 - Verbose
# 1 - Minimal
# 0 - Absolutely nothing
DEBUG = 2

#Must ISSN - To make life a bit easier, require an item to have an issn before attemping
# to resolve it
# SFX has 'journal' items that don't have ISSNs, making it a nightmare to handle them in a
# catalogue
MUST_ISSN = True

#INPUT_FILE - Lines of SFX data, locally created, usually made from 'Advance Export'
#             details in readme
INPUT_FILE = 'data_in/sfx_export.txt'

#OUTPUT_FILE - Pickled SFX_Resolved_Objects from resolution, stickly middle level thing
#              probably don't have to change much
OUTPUT_FILE = 'data_middle/working.p'

#FINAL_FILE - File with ERM ready data, ready to load into the ERM
FINAL_FILE = 'data_done/finished_data.txt'

#CHAR CONSTANTS
#Break SFX input data on this character, almost always \t
SEP_CHAR = '\t'
ERM_SEP_CHAR = '|'

#Relative path to webpy for Web Interface
#Will be in version 1.0
#WEB_PY_PATH = '\\..\webpy'
